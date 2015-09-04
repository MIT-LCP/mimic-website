+++
date = "2015-09-01T19:34:46-04:00"
title = "Procedures_icd"
linktitle = "Procedures_icd"
weight = 21
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++


# Overview

**Table source:** Hospital database.

**Table purpose:** Contains ICD procedures for patients, most notably ICD-9 procedures.

**Number of rows:** 240,095

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ICD\_PROCEDURES on `ICD9_CODE`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
PROC\_SEQ\_NUM | INT
ICD9\_CODE | VARCHAR(20)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `PROC_SEQ_NUM`

## `ICD9_CODE`


# Important considerations