+++
date = "2015-09-01T07:32:25-04:00"
draft = true
title = "noteevents"

+++

# Overview

Table source: Hospital database.
Table purpose: Contains all notes for patients.
Number of rows: 
Links to: 
* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Table columns

	RECORD_ID INT, 
	SUBJECT_ID INT, 
	HADM_ID INT, 
	CHARTDATE TIMESTAMP(0), 
	CATEGORY VARCHAR(50), 
	DESCRIPTION VARCHAR(300), 
	CGID INT, 
	ISERROR CHAR(1), 
	TEXT TEXT
	
# Detailed Description

## `RECORD_ID`

`RECORD_ID` identifies a unique note in the database. This is almost always unique to the row. However, there are a handful of cases where the hospital admission times overlap, resulting in ambiguity regarding which admission the note is associated with. In these cases, the note is duplicated and associated with each `HADM_ID`.

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `CHARTDATE`

`CHARTDATE` records the date at which the note was charted.

## `CATEGORY`, `DESCRIPTION`

`CATEGORY` and `DESCRIPTION` define the type of note recorded. For example, a `CATEGORY` of 'Discharge' indicates that the note is a discharge note, and a `DESCRIPTION` of 'Summary' in conjunction with this indicates that the note is a discharge summary.

## `CGID`

`CGID` is the identifier for the caregiver who input the note.

## `ISERROR`

## `TEXT`

`TEXT` contains the note text.

# Important considerations

* `TEXT` is often large and contains many newline characters: it may be easier to read if viewed in a distinct program rather than the one performing the queries.