+++
date = "2015-09-01T19:34:46-04:00"
title = "Diagnoses_ICD"
linktitle = "Diagnoses_ICD"
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

	SUBJECT_ID INT, 
	HADM_ID INT, 
	SEQUENCE INT, 
	CODE VARCHAR(20), 
	DESCRIPTION VARCHAR(50)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`


Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.
## `SEQUENCE`

## `CODE`

## `DESCRIPTION`


# Important considerations