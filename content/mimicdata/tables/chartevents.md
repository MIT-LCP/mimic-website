+++
date = "2015-09-01T07:32:25-04:00"
draft = true
title = "chartevents"

+++


# Overview

Table source: CareVue and Metavision ICU databases.
Table purpose: Contains all charted data for all patients.
Number of rows: 
Links to: 
* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Table columns

    SUBJECT_ID NUMBER(7,0) NOT NULL,
    HADM_ID NUMBER(7,0),
    ICUSTAY_ID NUMBER(7,0),
    ITEMID NUMBER(7,0),
    CHARTTIME DATE,
    STORETIME DATE,
    CGID NUMBER(7,0),
    VALUE VARCHAR2(200 BYTE),
    VALUENUM NUMBER,
    UOM VARCHAR2(20 BYTE),
    WARNING NUMBER(1,0),
    ERROR NUMBER(1,0),
    RESULTSTATUS VARCHAR2(20 BYTE),
    STOPPED VARCHAR2(20 BYTE),
    

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `ITEMID`

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

## `CHARTTIME`, `STORETIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured. `STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

## `VALUE`, `VALUENUM`

`VALUE` contains the value measured for the concept identified by the `ITEMID`. If this value is numeric, then `VALUENUM` contains the same data in a numeric format. If this data is not numeric, `VALUENUM` is null. In some cases (e.g. scores like Glasgow Coma Scale, Richmond Sedation Agitation Scale and Code Status), `VALUENUM` contains the score and `VALUE` contains the score and text describing the meaning of the score.

## `UOM`

`UOM` is the unit of measurement for the `VALUE`, if appropriate.

## `WARNING`, `ERROR`

`WARNING` and `ERROR` are Metavision specific columns which specify if a warning for the value was raised and if an error occurred during the measurement. 

?? TODO: review metavision front end and provide more detail on the above.

## `RESULTSTATUS`, `STOPPED`

`RESULTSTATUS` and `STOPPED` are CareVue specific columns which specify the type of measurement (`RESULTSTATUS` is 'Manual' or 'Automatic') and whether the measurement was stopped.

# Important considerations