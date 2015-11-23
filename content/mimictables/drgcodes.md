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

Name | Postgres data type
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

`DRG_TYPE` provides the type of DRG code in the entry. There have been multiple versions of DRG coding systems, all of which have different meanings for the codes (and often the range of the codes overlap, and so if the wrong version is assumed the code will be interpreted incorrectly). There are two types of DRG codes in the MIMIC-III database: 'HCFA' and 'MS-DRG'.

## `DRG_CODE`

`DRG_CODE` contains a code which represents the diagnosis billed for by the hospital.

## `DESCRIPTION`

`DESCRIPTION` provides an human understandable summary of the meaning of the given DRG code.

## `DRG_SEVERITY`, `DRG_MORTALITY`

`DRG_SEVERITY` and `DRG_MORTALITY` provide additional granularity to DRG codes in the HCFA system. Severity and mortality allow for higher billing costs when a diagnosis is more severe, and vice versa.

# Important considerations

* Since there are multiple versions of DRG codes, queries will need to incorporate both the type of DRG and the code when filtering for a certain diagnosis.
* All patients have an MS-DRG, but not all patients have an HCFA DRG code. Note that HCFA is believed to be redundant to the MS-DRG codes.
