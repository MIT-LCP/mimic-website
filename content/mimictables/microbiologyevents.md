+++
date = "2015-09-01T19:34:46-04:00"
title = "MICROBIOLOGYEVENTS"
linktitle = "MICROBIOLOGYEVENTS"
weight = 27
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC tables"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains microbiology information, including tests performed and sensitivities.

**Number of rows:** 328,446

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ITEMS on `SPEC_ITEMID`
* D\_ITEMS on `ORG_ITEMID`
* D\_ITEMS on `AB_ITEMID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
CHARTDATE | TIMESTAMP(0)
CHARTTIME | TIMESTAMP(0)
SPEC\_ITEMID | INT
SPEC\_TYPE\_CD | VARCHAR(10)
SPEC\_TYPE\_DESC | VARCHAR(100)
ORG\_ITEMID | INT
ORG\_CD | INT
ORG\_NAME | VARCHAR(100)
ISOLATE\_NUM | SMALLINT
AB\_ITEMID | INT
AB\_CD | INT
AB\_NAME | VARCHAR(30)
DILUTION\_TEXT | VARCHAR(10)
DILUTION\_COMPARISON | VARCHAR(20)
DILUTION\_VALUE | DOUBLE PRECISION
INTERPRETATION | VARCHAR(5)
	
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