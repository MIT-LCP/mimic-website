+++
date = "2015-09-01T19:34:46-04:00"
title = "CHARTEVENTS"
linktitle = "CHARTEVENTS"
weight = 13
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"
+++

# Overview

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Contains all charted data for all patients.

**Number of rows:** 263,201,375

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Brief summary

CHARTEVENTS contains all the charted data available for a patient. During their ICU stay, the primary repository of a patient's information is their electronic chart. The electronic chart displays patients' routine vital signs and any additional information relevant to their care: ventilator settings, laboratory values, code status, mental status, and so on. As a result, the bulk of information about a patient's stay is contained in CHARTEVENTS. Furthermore, even though laboratory values are captured elsewhere (LABEVENTS), they are frequently repeated within CHARTEVENTS. This occurs because it is desirable to display the laboratory values on the patient's electronic chart, and so the values are copied from the database storing laboratory values to the database storing the CHARTEVENTS.

# Important considerations

* Some items are duplicated between the labevents and chartevents tables. In cases where there is disagreement between measurements, labevents should be taken as the ground truth.

# Table columns

Name | Postgres data type | In CareVue | In Metavision
---- | -------- | ----  | ----
ROW\_ID | INT | Y | Y
SUBJECT\_ID | NUMBER(7,0) | Y | Y
HADM\_ID | NUMBER(7,0) | Y | Y
ICUSTAY\_ID | NUMBER(7,0) | Y | Y
ITEMID | NUMBER(7,0) | Y | Y
CHARTTIME | DATE | Y | Y
STORETIME | DATE | Y | Y
CGID | NUMBER(7,0) | Y | Y
VALUE | VARCHAR2(200 BYTE) | Y | Y
VALUENUM | NUMBER | Y | Y
VALUEUOM | VARCHAR2(20 BYTE) | Y | Y
WARNING | NUMBER(1,0) | | Y
ERROR | NUMBER(1,0) | | Y
RESULTSTATUS | VARCHAR2(20 BYTE) | Y |
STOPPED | VARCHAR2(20 BYTE) | Y |


# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `ITEMID`

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

## `CHARTTIME`, `STORETIME`

`CHARTTIME` records the time at which an observation was made, and is usually the closest proxy to the time the data was actually measured. `STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

## `VALUE`, `VALUENUM`

`VALUE` contains the value measured for the concept identified by the `ITEMID`. If this value is numeric, then `VALUENUM` contains the same data in a numeric format. If this data is not numeric, `VALUENUM` is null. In some cases (e.g. scores like Glasgow Coma Scale, Richmond Sedation Agitation Scale and Code Status), `VALUENUM` contains the score and `VALUE` contains the score and text describing the meaning of the score.

## `VALUEUOM`

`VALUEUOM` is the unit of measurement for the `VALUE`, if appropriate.

## `WARNING`, `ERROR`

`WARNING` and `ERROR` are Metavision specific columns which specify if a warning for the value was raised and if an error occurred during the measurement.

<!-- ?? TODO: review metavision front end and provide more detail on the above.
 -->

## `RESULTSTATUS`, `STOPPED`

`RESULTSTATUS` and `STOPPED` are CareVue specific columns which specify the type of measurement (`RESULTSTATUS` is 'Manual' or 'Automatic') and whether the measurement was stopped.
