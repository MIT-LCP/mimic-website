+++
date = "2015-09-01T19:34:46-04:00"
title = "Prescriptions"
linktitle = "Prescriptions"
weight = 20
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

**Table source:** Hospital provider order entry database.

**Table purpose:** Contains medication related order entries, i.e. prescriptions.

**Number of rows:** 4,156,848

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
ICUSTAY\_ID | INT
STARTTIME | TIMESTAMP(0)
ENDTIME | TIMESTAMP(0)
DRUG\_TYPE | VARCHAR(100)
DRUG | VARCHAR(100)
DRUG\_NAME\_POE | VARCHAR(100)
DRUG\_NAME\_GENERIC | VARCHAR(100)
FORMULARY\_DRUG\_CD | VARCHAR(120)
GSN | VARCHAR(200)
NDC | VARCHAR(120)
PROD\_STRENGTH | VARCHAR(120)
DOSE\_VAL\_RX | VARCHAR(120)
DOSE\_UNIT\_RX | VARCHAR(120)
FORM\_VAL\_DISP | VARCHAR(120)
FORM\_UNIT\_DISP | VARCHAR(120)
ROUTE | VARCHAR(120)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `STARTTIME`, `ENDTIME`

## `DRUG_TYPE`

## `DRUG`, `DRUG_NAME_POE`, `DRUG_NAME_GENERIC`

## `FORMULARY_DRUG_CD`, `GSN`, `NDC`

## `PROD_STRENGTH`

## `DOSE_VAL_RX`, `DOSE_UNIT_RX`

## `FORM_VAL_DISP`, `FORM_UNIT_DISP`

## `ROUTE`



# Important considerations

* The table does *not* specify if an order was later cancelled as of MIMIC III v1.0.