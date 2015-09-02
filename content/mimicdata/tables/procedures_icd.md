+++
date = "2015-09-01T07:32:25-04:00"
draft = true
title = "procedures_icd"

+++


# Overview

Table source: Hospital database.
Table purpose: Contains ICD procedures for patients, most notably ICD-9 procedures.
Number of rows: 
Links to: 
* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ICD\_PROCEDURES on `ICD9_CODE`

# Table columns

	SUBJECT_ID INT, 
	HADM_ID INT, 
	PROC_SEQ_NUM INT, 
	ICD9_CODE VARCHAR(20)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `PROC_SEQ_NUM`

## `ICD9_CODE`


# Important considerations