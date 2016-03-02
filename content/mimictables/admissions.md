+++
date = "2015-09-01T19:34:46-04:00"
title = "ADMISSIONS"
linktitle = "ADMISSIONS"
weight = 10
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"
+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Define a patient's hospital admission, HADM\_ID.

**Number of rows:** 58976

**Links to:**

* PATIENTS on `SUBJECT_ID`

# Brief summary

The ADMISSIONS table gives information regarding a patient's admission to the hospital. Since each unique hospital visit for a patient is assigned a unique `HADM_ID`, the ADMISSIONS table can be considered as a definition table for `HADM_ID`. Information available includes timing information for admission and discharge, demographic information, the source of the admission, and so on.

# Important considerations

* The data is sourced from the admission, discharge and transfer database from the hospital (often referred to as 'ADT' data).
* Organ donor accounts are sometimes created for patients who died in the hospital. These are distinct hospital admissions with very short, sometimes negative lengths of stay. Furthermore, their `DEATHTIME` is frequently the same as the earlier patient admission's `DEATHTIME`.
* All text data, except for that in the `INSURANCE` column, is stored in upper case.

# Table columns

Name | Postgres data type
---- | ----
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
ADMITTIME | TIMESTAMP(0)
DISCHTIME | TIMESTAMP(0)
DEATHTIME | TIMESTAMP(0)
ADMISSION\_TYPE | VARCHAR(50)
ADMISSION\_LOCATION | VARCHAR(50)
DISCHARGE\_LOCATION | VARCHAR(50)
INSURANCE | VARCHAR(255)
LANGUAGE | VARCHAR(10)
RELIGION | VARCHAR(50)
MARITAL\_STATUS | VARCHAR(50)
ETHNICITY | VARCHAR(200)
EDREGTIME | TIMESTAMP(0)
EDOUTTIME | TIMESTAMP(0)
DIAGNOSIS | VARCHAR(300)
HOSPITAL\_EXPIRE_FLAG | TINYINT
HAS\_IOEVENTS_DATA | TINYINT
HAS\_CHARTEVENTS_DATA | TINYINT

# Detailed description

The `ADMISSIONS` table defines all `HADM_ID` present in the database, covering an admission period between 1 June 2001 and 10 October 2012.

## `SUBJECT_ID`, `HADM_ID`

Each row of this table contains a unique `HADM_ID`, which represents a single patient's admission to the hospital. `HADM_ID` ranges from 1000000 - 1999999. It is possible for this table to have duplicate `SUBJECT_ID`, indicating that a single patient had multiple admissions to the hospital. The ADMISSIONS table can be linked to the PATIENTS table using `SUBJECT_ID`.

## `ADMITTIME`, `DISCHTIME`, `DEATHTIME`

`ADMITTIME` provides the date and time the patient was admitted to the hospital, while `DISCHTIME` provides the date and time the patient was discharged from the hospital. If applicable, `DEATHTIME` provides the time of in-hospital death for the patient. Note that `DEATHTIME` is only present if the patient died in-hospital, and is almost always the same as the patient's `DISCHTIME`. However, there can be some discrepancies due to typographical errors.

## `ADMISSION_TYPE`

`ADMISSION_TYPE` describes the type of the admission: 'ELECTIVE', 'URGENT', 'NEWBORN' or 'EMERGENCY'. Emergency/urgent indicate unplanned medical care, and are often collapsed into a single category in studies. Elective indicates a previously planned hospital admission. Newborn indicates that the `HADM_ID` pertains to the patient's birth.

## `ADMISSION_LOCATION`

`ADMISSION_LOCATION` provides information about the previous location of the patient prior to arriving at the hospital. There are 9 possible values:

* EMERGENCY ROOM ADMIT
* TRANSFER FROM HOSP/EXTRAM
* TRANSFER FROM OTHER HEALT
* CLINIC REFERRAL/PREMATURE
* ** INFO NOT AVAILABLE **
* TRANSFER FROM SKILLED NUR
* TRSF WITHIN THIS FACILITY
* HMO REFERRAL/SICK
* PHYS REFERRAL/NORMAL DELI

The truncated text occurs in the raw data.

## `INSURANCE`, `LANGUAGE`, `RELIGION`, `MARITAL_STATUS`, `ETHNICITY`

The `INSURANCE`, `LANGUAGE`, `RELIGION`, `MARITAL_STATUS`, `ETHNICITY` columns describe patient demographics. These columns occur in the ADMISSIONS table as they are originally sourced from the admission, discharge, and transfers (ADT) data from the hospital database. The values occasionally change between hospital admissions (`HADM_ID`) for a single patient (`SUBJECT_ID`). This is reasonable for some fields (e.g. `MARITAL_STATUS`, `RELIGION`), but less reasonable for others (e.g. `ETHNICITY`).

## `EDREGTIME`, `EDOUTTIME`

Time that the patient was registered and discharged from the emergency department.

## `DIAGNOSIS`

The `DIAGNOSIS` column provides a preliminary, free text diagnosis for the patient on hospital admission. The diagnosis is usually assigned by the admitting clincian and does not use a systematic ontology. As of MIMIC-III v1.0 there were 15,693 distinct diagnoses for 58,976 admissions. The diagnoses can be very informative (e.g. chronic kidney failure) or quite vague (e.g. weakness). Final diagnoses for hospital admissions are coded and can be found in the DIAGNOSES_ICD table.
