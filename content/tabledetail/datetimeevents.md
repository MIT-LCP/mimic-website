+++
date = "2015-09-01T19:34:46-04:00"
title = "Datetimeevents"
linktitle = "Datetimeevents"
weight = 11
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

Table source: CareVue and Metavision ICU databases.
Table purpose: Contains all date formatted data.
Number of rows: 4,486,049
Links to: 
* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Table columns

	SUBJECT_ID INT, 
	HADM_ID INT, 
	ICUSTAY_ID INT, 
	ITEMID INT, 
	CHARTTIME TIMESTAMP(0), 
	STORETIME TIMESTAMP(0), 
	CGID INT, 
	VALUE TIMESTAMP(0), 
	UOM VARCHAR(50), 
	WARNING SMALLINT, 
	ERROR SMALLINT, 
	RESULTSTATUS VARCHAR(50), 
	STOPPED VARCHAR(50)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `ITEMID`

## `CHARTTIME`, `STORETIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured. `STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

## `VALUE`

## `UOM`

## `WARNING`, `ERROR`

## `RESULTSTATUS`, `STOPPED`


# Important considerations