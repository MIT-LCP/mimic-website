+++
date = "2015-09-01T07:32:25-04:00"
draft = true
title = "microbiologyevents"

+++

# Overview

Table source: Hospital database.
Table purpose: Contains microbiology information, including tests performed and sensitivities.
Number of rows: 
Links to: 
* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ITEMS on `SPEC_ITEMID`
* D\_ITEMS on `ORG_ITEMID`
* D\_ITEMS on `AB_ITEMID`

# Table columns

	SUBJECT_ID INT, 
	HADM_ID INT, 
	CHARTDATE TIMESTAMP(0), 
	CHARTTIME TIMESTAMP(0), 
	SPEC_ITEMID INT, 
	SPEC_TYPE_CD VARCHAR(10), 
	SPEC_TYPE_DESC VARCHAR(100), 
	ORG_ITEMID INT, 
	ORG_CD INT, 
	ORG_NAME VARCHAR(100), 
	ISOLATE_NUM SMALLINT, 
	AB_ITEMID INT, 
	AB_CD INT, 
	AB_NAME VARCHAR(30), 
	DILUTION_TEXT VARCHAR(10), 
	DILUTION_COMPARISON VARCHAR(20), 
	DILUTION_VALUE DOUBLE PRECISION, 
	INTERPRETATION VARCHAR(5)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `CHARTDATE`, `CHARTTIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured.
`CHARTDATE` is the same as `CHARTTIME`, except there is no time available. Note that not all observations have a `CHARTTIME`, but all observations have a `CHARTDATE`.
In the cases where both `CHARTTIME` and `CHARTDATE` exists, `CHARTDATE` is equal to a truncated version of `CHARTTIME` (i.e. `CHARTTIME` without the timing information).
`CHARTDATE` was included as time information is not always available for microbiology measurements: in order to be clear about when this occurs, `CHARTTIME` is null, and `CHARTDATE` contains the date of the measurement.

## `SPEC_ITEMID`, `SPEC_TYPE_CD`, `SPEC_TYPE_DESC`

## `ORG_ITEMID`, `ORG_CD`, `ORG_NAME`

## `ISOLATE_NUM`

## `AB_ITEMID`, `AB_CD`, `AB_NAME`

## `DILUTION_TEXT`, `DILUTION_COMPARISON`, `DILUTION_VALUE`

## `INTERPRETATION`


# Important considerations