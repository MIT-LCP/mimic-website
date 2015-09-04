+++
date = "2015-09-01T19:34:46-04:00"
title = "DRGcodes"
linktitle = "DRGcodes"
weight = 13
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

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

## `DRG_CODE`

## `DESCRIPTION`

## `DRG_SEVERITY`, `DRG_MORTALITY`


# Important considerations