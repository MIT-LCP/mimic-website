+++
date = "2015-09-01T19:34:46-04:00"
title = "NOTEEVENTS"
linktitle = "NOTEEVENTS"
weight = 28
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# The noteevents table

**Table source:** Hospital database.

**Table purpose:** Contains all notes for patients.

**Number of rows:** 2,083,180

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* CAREGIVERS on `CGID`

# Important considerations

* `TEXT` is often large and contains many newline characters: it may be easier to read if viewed in a distinct program rather than the one performing the queries.
* Echo reports, ECG reports, and radiology reports are available for both inpatient and outpatient stays. If a patient is an outpatient, there will not be an `HADM_ID` associated with the note. If the patient is an inpatient, but was not admitted to the ICU for that particular hospital admission, then there will *not* be an `HADM_ID` associated with the note.
* Echos are generated using templates and in some cases there may be discrepancies in severity.  For example one report may contain: "Mild PA systolic hypertension. Severe PA systolic hypertension." indicating that the caregiver may not have removed the appropriate item from the template.

# Table columns

Name | Postgres data type
---- | ----
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
CHARTDATE | TIMESTAMP(0)
CHARTTIME | TIMESTAMP(0)
STORETIME | TIMESTAMP(0)
CATEGORY | VARCHAR(50)
DESCRIPTION | VARCHAR(300)
CGID | INT
ISERROR | CHAR(1)
TEXT | TEXT

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `CHARTDATE`, `CHARTTIME`, `STORETIME`

`CHARTDATE` records the date at which the note was charted. `CHARTDATE` will always have a time value of 00:00:00.

`CHARTTIME` records the date and time at which the note was charted. If both `CHARTDATE` and `CHARTTIME` exist, then the date portions will be identical. All records have a `CHARTDATE`. A subset are missing `CHARTTIME`. More specifically, notes with a `CATEGORY` value of 'Discharge Summary', 'ECG', and 'Echo' never have a `CHARTTIME`, only `CHARTDATE`. Other categories almost always have both `CHARTTIME` and `CHARTDATE`, but there is a small amount of missing data for `CHARTTIME` (usually less than 0.5% of the total number of notes for that category). 

`STORETIME` records the date and time at which a note was saved into the system.
Notes with a `CATEGORY` value of 'Discharge Summary', 'ECG', 'Radiology', and 'Echo' never have a `STORETIME`. All other notes have a `STORETIME`.

## `CATEGORY`, `DESCRIPTION`

`CATEGORY` and `DESCRIPTION` define the type of note recorded. For example, a `CATEGORY` of 'Discharge summary' indicates that the note is a discharge summary, and the `DESCRIPTION` of 'Report' indicates a full report while a `DESCRIPTION` of 'Addendum' indicates an addendum (additional text to be added to the previous report).

## `CGID`

`CGID` is the identifier for the caregiver who input the note.

## `ISERROR`

A '1' in the `ISERROR` column indicates that a physician has identified this note as an error. 

## `TEXT`

`TEXT` contains the note text.
