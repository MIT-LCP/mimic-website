+++
date = "2015-09-01T19:34:46-04:00"
title = "DRGCODES"
linktitle = "DRGCODES"
weight = 22
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains diagnosis related groups (DRG) codes for patients.

**Number of rows:** 125,557

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

# Table columns

Name | PostgreSQL data type
---- | ----
SUBJECT\_ID | INT
HADM\_ID | INT
DRG\_TYPE | VARCHAR(20)
DRG\_CODE | VARCHAR(20)
DESCRIPTION | VARCHAR(300)
DRG\_SEVERITY | SMALLINT
DRG\_MORTALITY | SMALLINT

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `DRG_TYPE`

`DRG_TYPE` provides the type of DRG code in the entry. There are two types of DRG codes in the database which have overlapping ranges but distinct definitions for the codes. The two types of DRG codes in the MIMIC-III database are 'HCFA' (Health Care Financing Administration) and 'APR' (All Payers Registry).

## `DRG_CODE`

`DRG_CODE` contains a code which represents the diagnosis billed for by the hospital.

## `DESCRIPTION`

`DESCRIPTION` provides a human understandable summary of the meaning of the given DRG code.
The description field frequently has acronyms which represent comorbidity levels (comorbid conditions or "CC"). The following table provides a definition for some of these acronyms:


Acronym | Description
---- | ----
w CC/MCC | with CC or Major CC
w MCC | with Major CC
w CC | with CC and without Major CC
w NonCC | with NonCC and without CC or Major CC
w/o MCC | with CC or Non CC and without Major CC
w/o CC/MCC | with nonCC and without CC or Major CC

Note that there are three levels of comorbidities: none, with comorbid conditions, and with major comorbid conditions. These acronyms are primarily used in HCFA/MS DRG codes.

## `DRG_SEVERITY`, `DRG_MORTALITY`

`DRG_SEVERITY` and `DRG_MORTALITY` provide additional granularity to DRG codes in the 'APR' DRG type. Severity and mortality allow for higher billing costs when a diagnosis is more severe, and vice versa.

# Important considerations

* HCFA-DRG codes have multiple descriptions as they have changed over time. Sometimes these descriptions are similar, but sometimes they are *completely different diagnoses*. Users will need to select rows using both the code *and* the description.
* Since there are multiple versions of DRG codes, queries will need to incorporate both the type of DRG and the code when filtering for a certain diagnosis.
* All patients have an HCFA-DRG code, but not all patients have an APR-DRG code. Note that APR-DRG is believed to be an alternative, more specific, code which could be used in conjunction with the HCFA codes.
