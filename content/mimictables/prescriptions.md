+++
date = "2015-09-01T19:34:46-04:00"
title = "PRESCRIPTIONS"
linktitle = "PRESCRIPTIONS"
weight = 31
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# The prescriptions table

**Table source:** Hospital provider order entry database.

**Table purpose:** Contains medication related order entries, i.e. prescriptions.

**Number of rows:** 4,156,450

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`

# Important considerations

* The table does *not* specify if an order was later cancelled as of MIMIC-III v1.0.

# Table columns

Name | Postgres data type 
---- | ----
ROW\_ID | INT
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

## `STARTDATE`, `ENDDATE`

`STARTDATE` and `ENDDATE` specify the date period for which the prescription was valid.

## `DRUG_TYPE`

`DRUG_TYPE` provides the type of drug prescribed.

## `DRUG`, `DRUG_NAME_POE`, `DRUG_NAME_GENERIC`

These columns are various representations of the drug prescribed to the patient. 

## `FORMULARY_DRUG_CD`, `GSN`, `NDC`

These columns provide a representation of the drug in various coding systems. `GSN` is the Generic Sequence Number. `NDC` is the [National Drug Code](https://en.wikipedia.org/wiki/National_Drug_Code)

## `PROD_STRENGTH`

## `DOSE_VAL_RX`, `DOSE_UNIT_RX`

## `FORM_VAL_DISP`, `FORM_UNIT_DISP`

## `ROUTE`

The route prescribed for the drug.

