+++
date = "2015-09-01T07:32:25-04:00"
draft = true
title = "admissions"

+++

# Overview

Table source: hospital database.
Table purpose: Define a patient's hospital admission, HADM\_ID.
Number of rows: 58976
Links to: 
* PATIENTS on `SUBJECT_ID`

# Table columns

ROW\_ID BIGINT, 
SUBJECT\_ID INT, 
HADM\_ID INT, 
ADMITTIME TIMESTAMP(0), 
DISCHTIME TIMESTAMP(0), 
DEATHTIME TIMESTAMP(0), 
ADMISSION\_TYPE VARCHAR(50), 
ADMISSION\_LOCATION VARCHAR(50), 
DISCHARGE\_LOCATION VARCHAR(50), 
INSURANCE VARCHAR(255), 
LANGUAGE VARCHAR(10), 
RELIGION VARCHAR(50), 
MARITAL\_STATUS VARCHAR(50), 
ETHNICITY VARCHAR(200), 
DIAGNOSIS VARCHAR(300)

# Detailed description

The `ADMISSIONS` table defines all `HADM_ID` present in the database, which include all hospital admissions between June 1st, 2001 and October 10th, 2012.

## `SUBJECT_ID`, `HADM_ID`

Each row of this table contains a unique `HADM_ID`, which represents a single patient's admission to the hospital. `HADM_ID` can range from 1000000 - 1999999. It is possible for this table to have duplicate `SUBJECT_ID`, indicating that a single patient had multiple admissions to the hospital. The ADMISSIONS table can be linked to the PATIENTS table using `SUBJECT_ID`.

## `ADMITTIME`, `DISCHTIME`, `DEATHTIME`

`ADMITTIME` provides the date and time the patient was admitted to the hospital, while `DISCHTIME` provides the date and time the patient was discharged from the hospital. If applicable, `DEATHTIME` provides the time of in-hospital death for the patient. Note that `DEATHTIME` is only present if the patient died in-hospital, and is almost always the same as the patient's `DISCHTIME`. However, there can be some discrepancies due to typographical errors.

## `ADMISSION_TYPE`

`ADMISSION_TYPE` describes the type of the admission: 'ELECTIVE', 'URGENT', 'NEWBORN' or 'EMERGENCY'. Emergency/urgent indicate unplanned medical care, and are often collapsed into a single category in studies. Elective indicates a previously planned hospital admission. Newborn indicates that the `HADM_ID` pertains to the patient's birth.

## `ADMISSION_LOCATION`

`ADMISSION\_LOCATION` provides information about the previous location of the patient prior to arriving at the hospital. There are 9 possible values:

* EMERGENCY ROOM ADMIT
* TRANSFER FROM HOSP/EXTRAM
* TRANSFER FROM OTHER HEALT
* CLINIC REFERRAL/PREMATURE
* ** INFO NOT AVAILABLE **
* TRANSFER FROM SKILLED NUR
* TRSF WITHIN THIS FACILITY
* HMO REFERRAL/SICK
* PHYS REFERRAL/NORMAL DELI

The truncated text occurs in the raw data as well. 

## INSURANCE, LANGUAGE, RELIGION, MARITAL_STATUS, ETHNICITY

The `INSURANCE`, `LANGUAGE`, `RELIGION`, `MARITAL_STATUS`, `ETHNICITY` columns describe various demographic aspects about each patient's admission. These columns occur in the ADMISSIONS table as they are originally sourced from the admission, discharge, transfers (ADT) data from the hospital database. As a result, it is possible (though infrequent) that these values change across two distinct hospital admissions (`HADM_ID`) for a single patient (`SUBJECT_ID`). This is reasonable for some of these columns (e.g. `MARITAL_STATUS`, `RELIGION`), but less reasonable for others (e.g. `ETHNICITY`). 

## DIAGNOSIS

The `DIAGNOSIS` column provides the admitting diagnosis for the patient. The diagnosis does not use a systematic ontology: as of MIMIC III v1.0 there are 15,693 distinct diagnoses for 58,976 patients. The diagnoses can be very informative (e.g. chronic kidney failure) or quite vague (e.g. weakness).

# Important considerations

* The data is sourced from the admission, discharge and transfer database from the hospital, frequently called ADT data.
* Organ donor accounts occur sometimes for patients who died in the hospital. These are distinct hospital admissions with very short, sometimes negative lengths of stay. Furthermore, their `DEATHTIME` is frequently the same as the original patient's `DEATHTIME`.
* All text data, except for that in the `INSURANCE` column, is stored in upper case.

