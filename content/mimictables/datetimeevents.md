+++
date = "2015-09-01T19:34:46-04:00"
title = "DATETIMEEVENTS"
linktitle = "DATETIMEEVENTS"
weight = 20
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# The datetimeevents table

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Contains all date formatted data.

**Number of rows:** 4,486,049

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type 
---- | ---- 
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
ICUSTAY\_ID | INT
ITEMID | INT
CHARTTIME | TIMESTAMP(0)
STORETIME | TIMESTAMP(0)
CGID | INT
VALUE | TIMESTAMP(0)
VALUEUOM | VARCHAR(50)
WARNING | SMALLINT
ERROR | SMALLINT
RESULTSTATUS | VARCHAR(50)
STOPPED | VARCHAR(50)
	
# Detailed Description

DATETIMEEVENTS contains all date measurements about a patient in the ICU. For example, the date of last dialysis would be in the DATETIMEEVENTS table, but the systolic blood pressure would not be in this table. As all dates in MIMIC-III are anonymized to protect patient confidentiality, all dates in this table have been shifted. Note that the chronology for an individual patient has been unaffected however, and quantities such as the difference between two dates remain true to reality.

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `ITEMID`

## `CHARTTIME`, `STORETIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured. `STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

## `VALUE`

## `VALUEUOM`

## `WARNING`, `ERROR`

## `RESULTSTATUS`, `STOPPED`

