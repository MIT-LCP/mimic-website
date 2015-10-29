+++
date = "2015-09-01T14:02:13-04:00"
title = "Querying MIMIC-III"
draft = false
linktitle = "Querying MIMIC-III"
weight = 2
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++

# Querying MIMIC-III

Prerequisites: *This tutorial assumes that you have an active connection to an instance of MIMIC-III running on PostgreSQL*.

## 1. Overview

This tutorial provides an introduction to the database structure and content. It also provides an idea of the types of information which can be extracted and the complexity of the data contained. By the end of this tutorial you will be able to:

* Obtain metadata from the various database objects (tables, views, etc).
* Perform basic queries on a single table. This includes counting the number of rows, and restricting the query to a subset of rows.
* Perform basic 'joins' to combine tables and extract useful information.
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

Try looking at the metadata for other tables such as ```patients``` and ```ioevents```.

## 3. Patient numbers

Ensure that the 'Query...' tab at the top of the screen is selected. SQL queries can be entered in the top panel and the results will be displayed at the bottom when the 'Execute query' button is pressed. Enter the following SQL in the box and press the 'Execute query' button.

``` sql
SELECT *
FROM patients;
```

At the bottom of the screen you will see three columns: subject_id, gender, and date of birth. 50 records are retrieved at a time and you can page through the results using the controls at the bottom of the screen.

Obtain the number of patients by performing the following query:

``` sql
SELECT COUNT(*)
FROM patients;
```

The 'gender' column identifies the gender of the patient. We can obtain the values used to indicate patient genders using the following query:

``` sql
SELECT gender
FROM patients;
```

We can see that 'M' and 'F' are the two characters used to indicate patient gender. We can use this information to obtain the number of female patients by restricting the query to retrieve results which have 'F' in the 'gender' column:

``` sql
SELECT COUNT(*)
FROM patients
WHERE gender = 'F';
```

And the numbers of male and female patients can be obtained using this query which counts how many female and male patients are in the patients table.

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

The database also contains date of death for patients who died inside the hospital in the column 'dod_hosp' and the date of death found in social security death records in 'dod_ssn'. This information from both columns is merged in the 'dod' column with priority given to 'dod_hosp'. Please note that this database contains adult and neonatal patients which will affect the mortality statistics. Categorizing patients into different age groups is carried out in the next section.

## 5. Patient age and mortality

To determine the adult mortality rate, we must first determine adult patients. We define adults as those patients who are 15 or more years old at the date of their first admission. To perform this query, we must first combine the patients and admissions tables to find patient admission dates, and their date of birth. Please note that the table naming in the query below. We have denoted 'admissions' with the alias 'a' and 'patients' with alias 'p':

``` sql
SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.hospital_expire_flag
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id;
```

Next, we find the minimum(earliest) admission date for each patient. This requires the use of the new functions, the 'MIN' function, which obtains the minimum value, and the 'PARTITION BY' function which determines the groups over which the minimum value is obtained, in this case, we determine the minimum time of admission for each patient:

``` sql
SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.hospital_expire_flag,
MIN (a.admittime)
OVER (PARTITION BY p.subject_id)
AS first_admittime
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id
ORDER BY a.hadm_id, p.subject_id;
```

A patient's age is given by the difference between their date of birth and the date of their first admission. We can obtain this by combining the above query with another query to provide the ages. Furthermore, we assign categories to different ages: >= 15 years old are adults and the rest are assigned to the 'other' category. The queries are combined using the 'WITH' keyword:

``` sql  
WITH first_admission_time AS (
SELECT p.subject_id, p.dob, p.gender, a.hadm_id, a.admittime,
MIN (a.admittime)
OVER (PARTITION BY a.hadm_id, p.subject_id)
AS first_admittime
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id
ORDER BY a.hadm_id, p.subject_id
),
age AS (
SELECT subject_id, hadm_id, dob, gender, first_admittime,
ROUND(months_between(first_admittime, dob) /12,2) first_admit_age,
CASE
WHEN (months_between(first_admittime,dob) /12) >= 15
THEN 'adult'
WHEN months_between(first_admittime,dob) <=1
THEN 'neonate'
ELSE 'middle'
END AS age_group
FROM first_admission_time
ORDER BY subject_id,hadm_id
)
SELECT *
FROM age;
```

The above query can now be combined with the **WHERE** and **COUNT** functions described earlier to determine the number of adult patients, whether or not they died, and therefore, their mortality rate.

## 6. ICU stays

In the MIMIC-III database, we define an ICU stay to be continuous if a patient is returned to an ICU room within 24 hours of being moved to a ward. Patient ICU movements are recorded in the transfers table:

``` sql  
SELECT *
FROM transfers;
```

The columns should be fairly self explanatory, click on the transfers table on the left hand side if you need more information about the columns and the data they contain. The 'prev_careunit' and 'curr_careunit' contain the names of the previous and current careunit respectively. The transfers table also contains columns 'prev_wardid' and 'curr_wardid' which contain the IDs of the previous and current careunit respectively. Ward IDs which specify the room within a ward have no corresponding key in order to protect patient health information.

The transfers table may have multiple entries per patient to provide information of all movement between various careunits of the hospital. The first entry in the transfers table for a patient who comes into the ICU will have nothing in the 'prev_careunit' column and similarly, the last entry for a patient will have nothing in the 'curr_careunit'. Patient entries that have nothing in both previous and current careunit columns signifies that patients have been transfered between units that do not fall under any of the ICUs. An example query for one patient and result from the transfers table is shown below. Note that columns 'intime', 'outtime', and 'los' have been truncated.

``` sql
SELECT *
FROM MIMICIII.transfers
WHERE HADM_ID = 112213;
```

row_id| subject_id | hadm_id | icustay_id | ...
-------- | ------------ | --------- | ------------ | ...
   54 |         12 |  112213 |            | ...
   55 |         12 |  112213 |            | ...
   56 |         12 |  112213 |     232669 | ...
   57 |         12 |  112213 |            | ...
   58 |         12 |  112213 |     232669 | ...
   59 |         12 |  112213 |            | ...
   60 |         12 |  112213 |            | ...       

<!-- talk about services -->

## 7. Services

Services is a newly added table in MIMIC-III which contains information about the transfers from being under one service to another during a patient's stay. The services table contains columns including 'prev_service' and 'curr_service' which contain the names of previous and current services respectively. 'transfertime' is the time at which the patient was moved from 'prev_service' to 'curr_service'.

## 8. Tutorial problem

How would gather useful information about patients admitted to the ICU?

The problem is problem is broken down into serveral parts and we recommend viewing the solution, which can be found below, after several attempts.

### Step 1
First start with retrieving 'subject_id', 'hadm_id', 'icustay_id', 'intime', and 'outtime' from the 'mimicIII' database 'icustayevents' table.

### Step 2
In addition to step 1, retrieve the caulcated age of patients by also using the patients table.

### Step 3
Now separate neonates from adult patients.

### Step 4
By incorporating the admissions table, find how long each stay was **BEFORE** the patients were admitted to the ICU

### Step 5
Next find the date of the patient's death if applicable.

### Step 6
Then find those deaths that occured while the patients were in the hospital

### Step 7
Find how many of those deaths occured within the ICU

## Solutions to the problems in section 8

### Solution to step 1

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
FROM MIMICIII.icustayevents ie;
```

### Solution to step 2

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round (months_between(ie.intime,pat.dob)/12 , 2) as age
FROM mimicIII.icustayevents ie
INNER join mimicIII.patients pat
  ON ie.subject_id = pat.subject_id;
  ```

### Solution to step 3

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime, ie.outtime
      , ROUND (months_between(ie.intime,pat.dob)/12, 2) as age
      , CASE
          WHEN months_between(ie.intime,pat.dob) <= 1 then 'neonate'
          WHEN months_between(ie.intime,pat.dob) > 1 and months_between(ie.intime,pat.dob) <= 15*12 then 'middle'
          ELSE 'adult' END AS ICUSTAY_AGE_GROUP
FROM MIMICIII.icustayevents ie
INNER JOIN MIMICIII.patients pat
  ON ie.subject_id = pat.subject_id;
```

### Solution to step 4
``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age

      , CASE
          WHEN months_between(ie.intime,pat.dob) <= 1 THEN 'neonate'
          WHEN months_between(ie.intime,pat.dob) > 1
            AND months_between(ie.intime,pat.dob) <= 15*12 THEN 'middle'
          ELSE 'adult' end as ICUSTAY_AGE_GROUP

      , ROUND (ie.intime - adm.admittime, 2) as preICULOS
FROM MIMICIII.icustayevents ie
INNER JOIN MIMICIII.patients pat
  ON ie.subject_id = pat.subject_id
INNER JOIN MIMICIII.admissions adm
  ON ie.hadm_id = adm.hadm_id;
```  

### Solution to step 5

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age

      , case
          WHEN months_between(ie.intime,pat.dob) <= 1 THEN 'neonate'
          WHEN months_between(ie.intime,pat.dob) > 1
            AND months_between(ie.intime,pat.dob) <= 15*12 THEN 'middle'
          ELSE 'adult' end as ICUSTAY_AGE_GROUP

      , ROUND( ie.intime - adm.admittime , 2 ) AS preICULOS
      , adm.deathtime
FROM MIMICIII.icustayevents ie
INNER Join MIMICIII.patients pat
  ON ie.subject_id = pat.subject_id
INNER JOIN MIMICIII.admissions adm
  ON ie.hadm_id = adm.hadm_id;
```

### Solution to step 6

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , ROUND (months_between(ie.intime,pat.dob)/12, 2) as age

      , CASE
          WHEN months_between(ie.intime,pat.dob) <= 1 THEN 'neonate'
          WHEN months_between(ie.intime,pat.dob) > 1
              AND months_between(ie.intime,pat.dob) <= 15*12 THEN 'middle'
          ELSE 'adult' END
          AS ICUSTAY_AGE_GROUP

      , ROUND (ie.intime - adm.admittime , 2) AS preICULOS
      , adm.deathtime

      , CASE WHEN adm.discharge_location = 'DEAD/EXPIRED' THEN 'Y' ELSE 'N' END
          AS hospital_expire_flag

FROM MIMICIII.icustayevents ie
INNER join MIMICIII.patients pat
  ON ie.subject_id = pat.subject_id
INNER join MIMICIII.admissions adm
  ON ie.hadm_id = adm.hadm_id;
```

### Solution to step 7

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id, ie.intime, ie.outtime
      , ROUND (months_between(ie.intime,pat.dob)/12, 2) AS age

      , CASE
          WHEN months_between(ie.intime,pat.dob) <= 1 THEN 'neonate'
          WHEN months_between(ie.intime,pat.dob) > 1
              AND months_between(ie.intime,pat.dob) <= 15*12 THEN 'middle'
          ELSE 'adult' end as ICUSTAY_AGE_GROUP

      , ROUND ( ie.intime - adm.admittime , 2 ) as preICULOS
      , adm.deathtime

      , CASE when adm.discharge_location = 'DEAD/EXPIRED' THEN 'Y' ELSE 'N' END
          AS hospital_expire_flag
        , CASE
            WHEN adm.deathtime BETWEEN ie.intime and ie.outtime
              THEN 'Y'
            WHEN adm.deathtime <= ie.intime
            -- sometimes there are typographical errors in the death date
              THEN 'Y'
            WHEN adm.dischtime <= ie.outtime AND adm.discharge_location = 'DEAD/EXPIRED'
              THEN 'Y'
            ELSE 'N' END
          AS ICUSTAY_EXPIRE_FLAG


FROM MIMICIII.icustayevents ie
INNER JOIN .patients pat
  ON ie.subject_id = pat.subject_id
INNER join MIMICIII.admissions adm
  ON ie.hadm_id = adm.hadm_id;
```
