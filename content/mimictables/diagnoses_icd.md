+++
date = "2015-09-01T19:34:46-04:00"
title = "DIAGNOSES_ICD"
linktitle = "DIAGNOSES_ICD"
weight = 21
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains ICD diagnoses for patients, most notably ICD-9 diagnoses.

**Number of rows:** 651,047

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ICD\_DIAGNOSES on `ICD9_CODE`

# Important considerations

* All ICD codes in MIMIC-III are ICD-9 based. The Beth Israel Deaconess Medical Center will begin using ICD-10 codes in 2015.
* The code field for the ICD-9-CM Principal and Other Diagnosis Codes is six characters in length, with the decimal point implied between the third and fourth digit for all diagnosis codes other than the V codes. The decimal is implied for V codes between the second and third digit.

# Table columns

Name | PostgreSQL data type  | Modifiers
---- | ---- | ----
ROW\_ID     | INT               | not null
SUBJECT\_ID     | INT               | not null
HADM\_ID        | INT               | not null
SEQ\_NUM        | INT               |
ICD9\_CODE      | VARCHAR(10)           |

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `SEQ_NUM`

`SEQ_NUM` provides the order in which the ICD diagnoses relate to the patient. ICD diagnoses are ordered by priority - and the order does have an impact on the reimbursement for treatment.

## `ICD9_CODE`

`ICD9_CODE` contains the actual code corresponding to the diagnosis assigned to the patient for the given row. Note that all codes, as of MIMIC-III v1.0, are ICD-9 codes.

