+++
date = "2015-09-01T14:02:13-04:00"
title = "BigQuery + MIMIC-III tutorial"
draft = false
linktitle = "BigQuery + MIMIC-III tutorial"
weight = 4
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++

# BigQuery


BigQuery is a columnar, distributed relational database management system. BigQuery accesses only the columns specified in the query, making it ideal for data analysis workflows.
BigQuery can be used to query a cloud based instance of MIMIC-III through the web browser.
To access MIMIC-III on BigQuery, see the [cloud data access guide](/gettingstarted/cloud).

# MIMIC-III on BigQuery

MIMIC-III is organized into three "datasets" on BigQuery. BigQuery uses datasets to organize data into subgroups. If you are familiar with the database concept of a schema, then you can understand BigQuery datasets as the logical equivalent of a schema.
The three datasets on BigQuery are:

* `mimiciii_clinical` - Almost all of MIMIC-III is stored here.
* `mimiciii_notes` - The NOTEEVENTS table is stored here.
* `mimiciii_derived` - Useful derivations which have been extracted from MIMIC-III are stored here for reuse by the community. All code to generate these views are open source and publicly available on the [google-cloud-views branch of GitHub](https://github.com/MIT-LCP/mimic-code/tree/google-cloud-views).

This tutorial will focus on querying the bulk of MIMIC-III data stored in `mimiciii_clinical`.

## 1. Overview

This tutorial provides an introduction to the structure and content of the MIMIC-III database. By the end of this tutorial you will be able to:

* Obtain metadata from the various database objects (tables, views, etc);
* Perform basic queries on a single table;
* Perform basic 'joins' to combine tables and extract useful information;
* Use database 'views' to extract high-level information.

First, navigate to BigQuery: https://console.cloud.google.com/bigquery

## 2. Database metadata

Metadata for a particular table can be obtained by clicking the table on the left sidebar on BigQuery, as below:

![Metadata for the admissions table in BigQuery](/static/img/tutorial/bq/metadata.png)

If you do not see the `mimiciii_clinical` dataset on BigQuery, you may need to [request access to MIMIC-III on BigQuery](/about/cloud), or [pin the project to your sidebar](/about/cloud#gcp-bigquery).

Try looking at the metadata for other tables such as `patients` and `chartevents`.

## 3. Patient numbers

SQL queries can be entered in the top "Query editor" panel and the results will be displayed at the bottom when the 'Run' button is pressed. Enter the following SQL in the box and press the 'Execute query' button.

``` sql
SELECT *
FROM `physionet-data.mimiciii_clinical.patients`
```

You should see the following:

![Example patients query](/static/img/tutorial/bq/patients.png)

50 records are retrieved at a time and you can page through the results using the controls at the bottom of the screen.

Obtain the number of patients with the following query:

``` sql
SELECT COUNT(*)
FROM `physionet-data.mimiciii_clinical.patients`;
```

The 'gender' column identifies the gender of the patient. We can obtain the distinct values used to indicate gender using the following query:

``` sql
SELECT DISTINCT(gender)
FROM `physionet-data.mimiciii_clinical.patients`;
```

We can see that 'M' and 'F' are the two characters used to indicate patient gender. We can use this information to obtain the number of female patients by adding a condition to select rows where the gender is 'F':

``` sql
SELECT COUNT(*)
FROM `physionet-data.mimiciii_clinical.patients`
WHERE gender = 'F';
```

And the numbers of male and female patients can be obtained using the following query:

``` sql
SELECT gender, COUNT(*)
FROM `physionet-data.mimiciii_clinical.patients`
GROUP BY gender;
```

## 4. Mortality and admissions

A flag which records whether or not a patient died in the hospital is stored in the patients table. Count the number of patients who died using the following query:

``` sql
SELECT expire_flag, COUNT(*)
FROM `physionet-data.mimiciii_clinical.patients`
GROUP BY expire_flag;
```

The database also contains date of death for patients who died inside the hospital in the column 'dod\_hosp' and the date of death found in social security death records in 'dod\_ssn'. This information from both columns is merged in the 'dod' column with priority given to 'dod_hosp'. Note that this database contains adult and neonatal patients which will affect the mortality statistics. Categorizing patients into different age groups is carried out in the next section.

## 5. Patient age and mortality

To determine the adult mortality rate we must first select the adult patients. We define adults as those patients who are 15 years old or above at the date of their first admission. To perform this query, we must combine the patients and admissions tables to find patient admission dates and dates of birth. We have denoted 'admissions' with the alias 'a' and 'patients' with alias 'p':

``` sql
SELECT p.subject_id, p.dob, a.hadm_id,
    a.admittime, p.expire_flag
FROM `physionet-data.mimiciii_clinical.admissions` a
INNER JOIN `physionet-data.mimiciii_clinical.patients` p
  ON p.subject_id = a.subject_id;
```

Next we find the earliest admission date for each patient. This requires the use of two functions: the 'MIN' function, which obtains the minimum value, and the 'PARTITION BY' function, which determines the groups over which the minimum value is obtained. To determine the earliest admission time for each patient:

``` sql
SELECT p.subject_id, p.dob, a.hadm_id,
    a.admittime, p.expire_flag,
    MIN (a.admittime) OVER (PARTITION BY p.subject_id) AS first_admittime
FROM `physionet-data.mimiciii_clinical.admissions` a
INNER JOIN `physionet-data.mimiciii_clinical.patients` p
  ON p.subject_id = a.subject_id
ORDER BY a.hadm_id, p.subject_id;
```

A patient's age is given by the difference between their date of birth and the date of their first admission.
In BigQuery, we must use special functions to do mathematical operations on datetime columns (note: as most columns in MIMIC-III have dates *and* times, they are often called `datetime` columns to differentiate them from `date` columns, which only store the date).
The reference page for [datetime operations is available on the BigQuery documentation website](https://cloud.google.com/bigquery/docs/reference/standard-sql/datetime_functions).

Let's calculate the age of patients at their time of admission:

``` sql
SELECT p.subject_id, p.dob, a.hadm_id,
    a.admittime, p.expire_flag,
    DATETIME_DIFF(admittime, dob, YEAR) as age
FROM `physionet-data.mimiciii_clinical.admissions` a
INNER JOIN `physionet-data.mimiciii_clinical.patients` p
  ON p.subject_id = a.subject_id
ORDER BY p.subject_id, a.hadm_id;
```

You should see the following:

![Ages of patients in MIMIC](/static/img/tutorial/bq/age.png)

Note at the bottom we have calculated the age for `subject_id` = 17 twice, once for each of their hospital admissions (the `hadm_id` is different between the rows).

If we examine the same patient more than once when calculating a statistic such as mortality, then our estimate will contain "repeated measures".
Unless we handle this phenomenon explicitly, our calculation will be biased.

A simple solution is to only examine the first hospitalization for each patient, which we can do with a `GROUP BY` clause.

```sql
SELECT
    p.subject_id, p.dob, p.gender
    , MIN(a.admittime) AS first_admittime
    , MIN( DATETIME_DIFF(admittime, dob, YEAR) )
        AS first_admit_age
FROM `physionet-data.mimiciii_clinical.patients` p
INNER JOIN `physionet-data.mimiciii_clinical.admissions` a
  ON p.subject_id = a.subject_id
GROUP BY p.subject_id, p.dob, p.gender
ORDER BY p.subject_id
```

Note in the above:

1. Our group is defined by columns listed after `GROUP BY`, in this case: `p.subject_id`, `p.dob`, `p.gender`. BigQuery will return a row for each unique combination of these three columns. Since we know that each patient only has one `dob` and one `gender` in the PATIENTS table, we know that this will return one row per `subject_id`.
2. We have removed `hadm_id`, as we will collapse multiple `hadm_id` into a single row.
3. We have wrapped `admittime` in a `MIN()` aggregate function. For dates, `MIN()` returns the earliest date.
4. We have wrapped age in a `MIN()` aggregate function. This tells BigQuery to extract the minimum age across all hospital admissions.

Now that we have a set of unique patients with their age, we can group them into sensible categories based upon age and calculate the mortality rate in these categories. Patients with an age >= 15 years old are adults and the rest are assigned to other categories. Note the use of the `WITH` clause, which allows us to make a temporary view which we can query against in subsequent lines.

``` sql  
WITH first_admission_time AS
(
  SELECT
      p.subject_id, p.dob, p.gender
      , MIN (a.admittime) AS first_admittime
      , MIN( DATETIME_DIFF(admittime, dob, YEAR) )
          AS first_admit_age
  FROM `physionet-data.mimiciii_clinical.patients` p
  INNER JOIN `physionet-data.mimiciii_clinical.admissions` a
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
      , MIN( DATETIME_DIFF(admittime, dob, YEAR) )
          AS first_admit_age
  FROM `physionet-data.mimiciii_clinical.patients` p
  INNER JOIN `physionet-data.mimiciii_clinical.admissions` a
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
          WHEN first_admit_age > 89
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
FROM `physionet-data.mimiciii_clinical.transfers`;
```

The columns should be fairly self explanatory. Click on the transfers table on the left hand side if you need more information about the columns and the data they contain. The 'prev_careunit' and 'curr_careunit' contain the names of the previous and current careunit respectively. The transfers table also includes 'prev_wardid' and 'curr_wardid' columns, which contain the IDs of the previous and current careunit respectively. Ward IDs, which specify the room within a ward, have no corresponding key in order to protect patient health information.

The transfers table may have multiple entries per patient to provide detail of all movement between various careunits of the hospital. The first entry in the transfers table for a patient who comes into the ICU will have nothing in the 'prev\_careunit' column. Similarly, the last entry for a patient will have nothing in the 'curr\_careunit'. Entries that have nothing in both previous and current careunit columns indicate that the patient has been transfered between non intensive care units. An example query for one patient and result from the transfers table is shown below. Note that columns 'intime', 'outtime', and 'los' have been truncated.

``` sql
SELECT *
FROM `physionet-data.mimiciii_clinical.transfers`
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

How would you gather useful information about patients admitted to the ICU? The problem can be broken down into several parts:

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
FROM `physionet-data.mimiciii_clinical.icustays` ie;
```

### Solution to step 2

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    DATETIME_DIFF(admittime, dob, YEAR) AS age
-- we use 'ie' as an alias for the icustays table
FROM `physionet-data.mimiciii_clinical.icustays` ie
-- we use 'pat' as an alias for the patients table
INNER JOIN `physionet-data.mimiciii_clinical.patients` pat
-- since subject_id is unique for every row in patients, we will get
-- one row for every row in icustays (ie)
  ON ie.subject_id = pat.subject_id;
```

### Solution to step 3

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    DATETIME_DIFF(admittime, dob, YEAR) AS age,
    CASE
        WHEN DATETIME_DIFF(admittime, dob, YEAR) <= 1
            THEN 'neonate'
        WHEN DATETIME_DIFF(admittime, dob, YEAR) <= 14
            THEN 'middle'
        -- all ages > 89 in the database were replaced with 300
        WHEN DATETIME_DIFF(admittime, dob, YEAR) > 89
            then '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP
FROM `physionet-data.mimiciii_clinical.icustays` ie
INNER JOIN `physionet-data.mimiciii_clinical.patients` pat
  ON ie.subject_id = pat.subject_id;
```

### Solution to step 4

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    DATETIME_DIFF(adm.admittime, pat.dob, YEAR) as age,
    DATETIME_DIFF(ie.intime, adm.admittime, DAY) as preiculos,
    CASE
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 1
            THEN 'neonate'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 14
            THEN 'middle'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) > 89
            THEN '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP
FROM `physionet-data.mimiciii_clinical.icustays` ie
INNER JOIN `physionet-data.mimiciii_clinical.patients` pat
  ON ie.subject_id = pat.subject_id
INNER JOIN `physionet-data.mimiciii_clinical.admissions` adm
  ON ie.hadm_id = adm.hadm_id;
```  

### Solution to step 5

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    -- patient death in hospital is stored in the admissions table
    adm.deathtime,
    DATETIME_DIFF(adm.admittime, pat.dob, YEAR) as age,
    DATETIME_DIFF(ie.intime, adm.admittime, DAY) as preiculos,
    CASE
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 1
            THEN 'neonate'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 14
            THEN 'middle'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) > 89
            THEN '>89'
        ELSE 'adult'
        END AS ICUSTAY_AGE_GROUP
FROM `physionet-data.mimiciii_clinical.icustays` ie
INNER JOIN `physionet-data.mimiciii_clinical.patients` pat
  ON ie.subject_id = pat.subject_id
INNER JOIN `physionet-data.mimiciii_clinical.admissions` adm
  ON ie.hadm_id = adm.hadm_id;
```

### Solution to step 6

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime,
    -- patient death in hospital is stored in the admissions table
    adm.deathtime,
    DATETIME_DIFF(adm.admittime, pat.dob, YEAR) as age,
    DATETIME_DIFF(ie.intime, adm.admittime, DAY) as preiculos,
    CASE
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 1
            THEN 'neonate'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 14
            THEN 'middle'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) > 89
            THEN '>89'
        ELSE 'adult'
    END AS ICUSTAY_AGE_GROUP,
    -- the "hospital_expire_flag" field in the admissions table indicates if a patient died in-hospital
    CASE
        WHEN adm.hospital_expire_flag = 1 then 'Y'
    ELSE 'N'
    END AS hospital_expire_flag
FROM `physionet-data.mimiciii_clinical.icustays` ie
INNER JOIN `physionet-data.mimiciii_clinical.patients` pat
  ON ie.subject_id = pat.subject_id
INNER JOIN `physionet-data.mimiciii_clinical.admissions` adm
  ON ie.hadm_id = adm.hadm_id;
```

### Solution to step 7

``` sql
SELECT ie.subject_id, ie.hadm_id, ie.icustay_id,
    ie.intime, ie.outtime, 
    -- patient death in hospital is stored in the admissions table
    adm.deathtime,
    DATETIME_DIFF(adm.admittime, pat.dob, YEAR) as age,
    DATETIME_DIFF(ie.intime, adm.admittime, DAY) as preiculos,
    CASE
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 1
            THEN 'neonate'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) <= 14
            THEN 'middle'
        WHEN DATETIME_DIFF(adm.admittime, pat.dob, YEAR) > 89
            THEN '>89'
        ELSE 'adult'
    END AS ICUSTAY_AGE_GROUP,
    -- the "hospital_expire_flag" field in the admissions table indicates if a patient died in-hospital
    CASE
        WHEN adm.hospital_expire_flag = 1 then 'Y'
    ELSE 'N'
    END AS hospital_expire_flag,
    -- note also that hospital_expire_flag is equivalent to "Is adm.deathtime not null?"
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
FROM `physionet-data.mimiciii_clinical.icustays` ie
INNER JOIN `physionet-data.mimiciii_clinical.patients` pat
  ON ie.subject_id = pat.subject_id
INNER JOIN `physionet-data.mimiciii_clinical.admissions` adm
  ON ie.hadm_id = adm.hadm_id;
```
