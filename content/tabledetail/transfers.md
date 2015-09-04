+++
date = "2015-09-01T19:34:46-04:00"
title = "Transfers"
linktitle = "Transfers"
weight = 23
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Physical locations for patients throughout their hospital stay.

**Number of rows:** 261,897

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
ICUSTAY\_ID | INT
DBSOURCE | VARCHAR(20)
EVENTTYPE | VARCHAR(20)
PREV\_CAREUNIT | VARCHAR(20)
CURR\_CAREUNIT | VARCHAR(20)
PREV\_WARDID | SMALLINT
CURR\_WARDID | SMALLINT
INTIME | TIMESTAMP(0)
OUTTIME | TIMESTAMP(0)
LOS | INT

	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `DBSOURCE`

## `EVENTTYPE`

## `PREV_CAREUNIT`, `CURR_CAREUNIT`

## `PREV_WARDID`, `CURR_WARDID`

## `INTIME`, `OUTTIME`

## `LOS`


# Important considerations