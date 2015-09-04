+++
date = "2015-09-01T19:34:46-04:00"
title = "DIAGNOSES_ICD"
linktitle = "DIAGNOSES_ICD"
weight = 12
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains ICD diagnoses for patients, most notably ICD-9 diagnoses.

**Number of rows:** 651,047

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
SEQUENCE | INT
CODE | VARCHAR(20)
DESCRIPTION | VARCHAR(50)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `SEQUENCE`

`SEQUENCE` provides the order in which the ICD diagnoses relate to the patient. ICD diagnoses are ordered by priority - and the order does have an impact on the reimbursement for treatment.

## `CODE`

`CODE` contains the actual code corresponding to the diagnosis assigned to the patient for the given row. Note that all codes, as of MIMIC III v1.0, are ICD-9 codes.

## `DESCRIPTION`

`DESCRIPTION` is a brief summary of the diagnosis represented by the given code.

# Important considerations

* All ICD codes in MIMIC III v1.0 are ICD-9 based. The Beth Israel Deaconess Medical Center will begin using ICD-10 codes in 2015.