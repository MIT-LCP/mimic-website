+++
date = "2015-09-01T14:02:13-04:00"
title = "Querying MIMIC-III"
draft = false
linktitle = "Querying MIMIC-III"
weight = 3
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++

# Querying MIMIC-III

Prerequisites: *This tutorial assumes that you have an active connection to an instance of MIMIC-III running on PostgreSQL*.
Note also that all the queries are written assuming that the MIMIC-III database is on your default search path. To change this in PostgreSQL, run the following command:

```sql
set search_path to mimiciii;
```

Note in the above we have assumed MIMIC-III is installed under the schema `mimiciii` - it may be different on your system.

## 1. Overview

This tutorial provides an introduction to the structure and content of the MIMIC-III database. By the end of this tutorial you will be able to:

* Obtain metadata from the various database objects (tables, views, etc);
* Perform basic queries on a single table;
* Perform basic 'joins' to combine tables and extract useful information;
* Use database 'views' to extract high-level information.

## 2. Database metadata

Metadata for a particular table can be obtained in Postgres with ```\d+ <schema>.<tablename>```. For example, the following command prints metadata for the admissions table:

``` sql
\d+ MIMICIII.ADMISSIONS;

-- returns the following metadata

        Column        |              Type              | Modifiers | ...
----------------------+--------------------------------+-----------+ ...
 row_id               | integer                        | not null  | ...
 subject_id           | integer                        | not null  | ...
 hadm_id              | integer                        | not null  | ...
 admittime            | timestamp(0) without time zone | not null  | ...
 dischtime            | timestamp(0) without time zone | not null  | ...
 ...
```

Try looking at the metadata for other tables such as ```patients``` and ```chartevents```.

## 3. Patient numbers

Ensure that the 'Query...' tab at the top of the screen is selected. SQL queries can be entered in the top panel and the results will be displayed at the bottom when the 'Execute query' button is pressed. Enter the following SQL in the box and press the 'Execute query' button.

``` sql
SELECT *
FROM patients;
```

At the bottom of the screen you will see three columns: subject_id, gender, and date of birth. 50 records are retrieved at a time and you can page through the results using the controls at the bottom of the screen.

Obtain the number of patients with the following query:

``` sql
SELECT COUNT(*)
FROM patients;
```

The 'gender' column identifies the gender of the patient. We can obtain the distinct values used to indicate gender using the following query:

``` sql
SELECT DISTINCT(gender)
FROM patients;
```

We can see that 'M' and 'F' are the two characters used to indicate patient gender. We can use this information to obtain the number of female patients by adding a condition to select rows where the gender is 'F':

``` sql
SELECT COUNT(*)
FROM patients
WHERE gender = 'F';
```

And the numbers of male and female patients can be obtained using the following query:

``` sql
SELECT gender, COUNT(*)
FROM patients
GROUP BY gender;
```

## 4. Mortality and admissions

A flag which records whether or not a patient died in the hospital is stored in the patients table. Count the number of patients who died using the following query:

``` sql
SELECT hospital_expire_flag, COUNT(*)
FROM patients
GROUP BY hospital_expire_flag;
```

The database also contains date of death for patients who died inside the hospital in the column 'dod\_hosp' and the date of death found in social security death records in 'dod\_ssn'. This information from both columns is merged in the 'dod' column with priority given to 'dod_hosp'. Note that this database contains adult and neonatal patients which will affect the mortality statistics. Categorizing patients into different age groups is carried out in the next section.

## 5. Patient age and mortality

To determine the adult mortality rate we must first select the adult patients. We define adults as those patients who are 15 years old or above at the date of their first admission. To perform this query, we must combine the patients and admissions tables to find patient admission dates and dates of birth. We have denoted 'admissions' with the alias 'a' and 'patients' with alias 'p':

``` sql
SELECT p.subject_id, p.dob, a.hadm_id,
    a.admittime, p.hospital_expire_flag
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id;
```

Next we find the earliest admission date for each patient. This requires the use of two functions: the 'MIN' function, which obtains the minimum value, and the 'PARTITION BY' function, which determines the groups over which the minimum value is obtained. To determine the earliest admission time for each patient:

``` sql
SELECT p.subject_id, p.dob, a.hadm_id,
    a.admittime, p.hospital_expire_flag,
    MIN (a.admittime) OVER (PARTITION BY p.subject_id) AS first_admittime
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id
ORDER BY a.hadm_id, p.subject_id;
```

A patient's age is given by the difference between their date of birth and the date of their first admission. We can obtain this by combining the above query with another query to provide the ages. Furthermore, we assign categories to different ages: >= 15 years old are adults and the rest are assigned to other categories. Note the use of the `WITH` clause, which allows us to make a temporary view which we can query against in subsequent lines.

``` sql  

WITH first_admission_time AS
(
  SELECT
      p.subject_id, p.dob, p.gender
      , MIN (a.admittime) AS first_admittime
      , MIN( ROUND( (cast(admittime as date) - cast(dob as date)) / 365.242,2) )
          AS first_admit_age
  FROM patients p
  INNER JOIN admissions a
  ON p.subject_id = a.subject_id
  GROUP BY p.subject_id, p.dob, p.gender
  ORDER BY p.subject_id
)
SELECT
    subject_id, dob, gender
    , first_admittime, first_admit_age
    , CASE
        -- all ages > 89 in the database were replaced with 300
        WHEN first_admit_age > 89
            then '>89'
        WHEN first_admit_age >= 14
            THEN 'adult'
        WHEN first_admit_age <= 1
            THEN 'neonate'
        ELSE 'middle'
        END AS age_group
FROM first_admission_time
ORDER BY subject_id
```

The above query can now be combined with the **WHERE** and **COUNT** functions described earlier to determine the number of adult patients, whether or not they died, and therefore, their mortality rate.

``` sql  
WITH first_admission_time AS
(
  SELECT
      p.subject_id, p.dob, p.gender
      , MIN (a.admittime) AS first_admittime
      , MIN( ROUND( (cast(admittime as date) - cast(dob as date)) / 365.242,2) )
          AS first_admit_age
  FROM patients p
  INNER JOIN admissions a
  ON p.subject_id = a.subject_id
  GROUP BY p.subject_id, p.dob, p.gender
  ORDER BY p.subject_id
)
, age as
(
  SELECT
      subject_id, dob, gender
      , first_admittime, first_admit_age
      , CASE
          -- all ages > 89 in the database were replaced with 300
          -- we check using > 100 as a conservative threshold to ensure we capture all these patients
          WHEN first_admit_age > 100
              then '>89'
          WHEN first_admit_age >= 14
              THEN 'adult'
          WHEN first_admit_age <= 1
              THEN 'neonate'
          ELSE 'middle'
          END AS age_group
  FROM first_admission_time
)
select age_group, gender
  , count(subject_id) as NumberOfPatients
from age
group by age_group, gender
```

Note that no 'middle' patients show up - this reflects the fact that MIMIC-III does not contain data from paediatric patients.

## 6. ICU stays

In the MIMIC-III database, we define an ICU stay to be continuous if a patient is returned to an ICU room within 24 hours of being moved to a ward. Patient ICU movements are recorded in the transfers table:

``` sql  
SELECT *
FROM transfers;
```

The columns should be fairly self explanatory. Click on the transfers table on the left hand side if you need more information about the columns and the data they contain. The 'prev_careunit' and 'curr_careunit' contain the names of the previous and current careunit respectively. The transfers table also includes 'prev_wardid' and 'curr_wardid' columns, which contain the IDs of the previous and current careunit respectively. Ward IDs, which specify the room within a ward, have no corresponding key in order to protect patient health information.

The transfers table may have multiple entries per patient to provide detail of all movement between various careunits of the hospital. The first entry in the transfers table for a patient who comes into the ICU will have nothing in the 'prev\_careunit' column. Similarly, the last entry for a patient will have nothing in the 'curr\_careunit'. Entries that have nothing in both previous and current careunit columns indicate that the patient has been transfered between non intensive care units. An example query for one patient and result from the transfers table is shown below. Note that columns 'intime', 'outtime', and 'los' have been truncated.

``` sql
SELECT *
FROM transfers
WHERE HADM_ID = 112213;
```

| row\_id  | subject\_id | hadm\_id  | icustay\_id  |
| ------------- | ------------- | ------------- | ------------- |
| 54  | 12  | 112213 |  |
| 55  | 12  | 112213 |  |
| 56  | 12  | 112213 | 232669 |
| 57  | 12  | 112213 |  |
| 58  | 12  | 112213 | 232669 |
| 59  | 12  | 112213 |  |
| 60  | 12  | 112213 |  |

## 7. Services

Services is a newly added table in MIMIC-III which contains information about the transfers from being under one service to another during a patient's stay. The services table contains columns including 'prev\_service' and 'curr\_service' which contain the names of previous and current services respectively. 'transfertime' is the time at which the patient was moved from 'prev_service' to 'curr_service'.

## 8. Tutorial problem

How would gather useful information about patients admitted to the ICU? The problem can be broken down into several parts:

### Step 1
First start with retrieving 'subject_id', 'hadm_id', 'icustay_id', 'intime', and 'outtime' from the 'icustays' table.

### Step 2
Using the patients table retrieve the calculated age of patients.

### Step 3
Separate neonates from adult patients.

### Step 4
By incorporating the admissions table, find how long each stay was **BEFORE** the patients were admitted to the ICU

### Step 5
Next find the date of the patient's death if applicable.

### Step 6
Then find those deaths that occurred while the patients were in the hospital.

### Step 7
Find how many of those deaths occurred within the ICU.

## Solutions to the problems in section 8

### Solution to step 1

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime
FROM icustays ie;
```

### Solution to step 2

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) AS age
FROM icustays ie
INNER JOIN patients pat
ON ie.subject_id = pat.subject_id;
  ```

### Solution to step 3

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) AS age,
    CASE
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 1
            THEN 'neonate'
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 14
            THEN 'middle'
        -- all ages > 89 in the database were replaced with 300
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) > 100
            then '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP
FROM icustays ie
INNER JOIN patients pat
ON ie.subject_id = pat.subject_id;
```

### Solution to step 4

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) as age,
    ROUND((cast(ie.intime as date) - cast(adm.admittime as date))/365.242, 2) as preiculos,
    CASE
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 1
            THEN 'neonate'
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 14
            THEN 'middle'
        -- all ages > 89 in the database were replaced with 300
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) > 100
            THEN '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP
FROM icustays ie
INNER JOIN patients pat
ON ie.subject_id = pat.subject_id
INNER JOIN admissions adm
ON ie.hadm_id = adm.hadm_id;
```  

### Solution to step 5

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime, adm.deathtime,
    ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) as age,
    ROUND((cast(ie.intime as date) - cast(adm.admittime as date))/365.242, 2) AS preiculos,
    CASE
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 1
            THEN 'neonate'
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 14
            THEN 'middle'
        -- all ages > 89 in the database were replaced with 300
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) > 100
            THEN '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP
FROM icustays ie
INNER JOIN patients pat
ON ie.subject_id = pat.subject_id
INNER JOIN admissions adm
ON ie.hadm_id = adm.hadm_id;
```

### Solution to step 6

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime, adm.deathtime,
    ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) AS age,
    ROUND((cast(ie.intime as date) - cast(adm.admittime as date))/365.242, 2) AS preiculos,
    CASE
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 1
            THEN 'neonate'
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 14
            THEN 'middle'
        -- all ages > 89 in the database were replaced with 300
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) > 100
            THEN '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP,
    CASE
        WHEN adm.discharge_location = 'DEAD/EXPIRED' THEN 'Y'
        ELSE 'N'
        END AS hospital_expire_flag
FROM icustays ie
INNER JOIN patients pat
ON ie.subject_id = pat.subject_id
INNER JOIN admissions adm
ON ie.hadm_id = adm.hadm_id;
```

### Solution to step 7

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime, adm.deathtime,
    ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) AS age,
    ROUND((cast(ie.intime as date) - cast(adm.admittime as date))/365.242, 2) AS preiculos,
    CASE
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 1
            THEN 'neonate'
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) <= 14
            THEN 'middle'
        -- all ages > 89 in the database were replaced with 300
        WHEN ROUND((cast(ie.intime as date) - cast(pat.dob as date))/365.242, 2) > 100
            THEN '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP,
    CASE
        WHEN adm.discharge_location = 'DEAD/EXPIRED' THEN 'Y'
        ELSE 'N'
        END AS hospital_expire_flag,
    CASE
        WHEN adm.deathtime BETWEEN ie.intime and ie.outtime
            THEN 'Y'
        -- sometimes there are typographical errors in the death date, so check before intime
        WHEN adm.deathtime <= ie.intime
            THEN 'Y'
        WHEN adm.dischtime <= ie.outtime
            AND adm.discharge_location = 'DEAD/EXPIRED'
            THEN 'Y'
        ELSE 'N'
        END AS ICUSTAY_EXPIRE_FLAG
FROM icustays ie
INNER JOIN patients pat
ON ie.subject_id = pat.subject_id
INNER JOIN admissions adm
ON ie.hadm_id = adm.hadm_id;
```
