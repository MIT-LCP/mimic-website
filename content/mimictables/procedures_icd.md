+++
date = "2015-09-01T19:34:46-04:00"
title = "PROCEDURES_ICD"
linktitle = "PROCEDURES_ICD"
weight = 33
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains ICD procedures for patients, most notably ICD-9 procedures.

**Number of rows:** 240,095

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ICD\_PROCEDURES on `ICD9_CODE`

# Important considerations

* In MIMIC-III v1.0, only ICD-9 codes are used for recording procedures.

# Table columns

Name | PostgreSQL data type  | Modifiers
---- | ---- | ----
ROW\_ID     | INT               | not null
SUBJECT\_ID     | INT               | not null
HADM\_ID        | INT               | not null
SEQ\_NUM        | INT              |
ICD9\_CODE      | VARCHAR(10)           |

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `SEQ_NUM`

`PROC_SEQ_NUM` provides the order in which the procedures were performed.

## `ICD9_CODE`

`CODE` provides the code for the given procedure.

