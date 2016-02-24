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

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains all notes for patients.

**Number of rows:**

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
CATEGORY | VARCHAR(50)
DESCRIPTION | VARCHAR(300)
CGID | INT
ISERROR | CHAR(1)
TEXT | TEXT

# Detailed Description

## `RECORD_ID`

`RECORD_ID` identifies a unique note in the database. This is almost always unique to the row. However, there are a handful of cases where the hospital admission times overlap, resulting in ambiguity regarding which admission the note is associated with. In these cases, the note is duplicated and associated with each `HADM_ID`.

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `CHARTDATE`

`CHARTDATE` records the date at which the note was charted.

## `CATEGORY`, `DESCRIPTION`

`CATEGORY` and `DESCRIPTION` define the type of note recorded. For example, a `CATEGORY` of 'Discharge' indicates that the note is a discharge note, and a `DESCRIPTION` of 'Summary' in conjunction with this indicates that the note is a discharge summary.

## `CGID`

`CGID` is the identifier for the caregiver who input the note.

## `ISERROR`

## `TEXT`

`TEXT` contains the note text.
