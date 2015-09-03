+++
date = "2015-09-01T19:34:46-04:00"
title = "ICUstayevents"
linktitle = "ICUstayevents"
weight = 14
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"
+++


# Overview

**Table source:** Hospital database.

**Table purpose:** Defines each ICUSTAY\_ID in the database, i.e. defines a single ICU stay.

**Number of rows:** 61,532

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

# Table columns

	SUBJECT_ID INT, 
	HADM_ID INT, 
	ICUSTAY_ID INT, 
	DBSOURCE VARCHAR(20), 
	FIRST_CAREUNIT VARCHAR(20), 
	LAST_CAREUNIT VARCHAR(20),
	FIRST_WARDID SMALLINT,
	LAST_WARDID SMALLINT,
	INTIME TIMESTAMP(0), 
	OUTTIME TIMESTAMP(0), 
	LOS DOUBLE PRECISION
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `DBSOURCE`

## `FIRST_CAREUNIT`, `LAST_CAREUNIT`

## `FIRST_WARDID`, `LAST_WARDID`

## `INTIME`, `OUTTIME`

## `LOS`


# Important considerations