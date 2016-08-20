+++
date = "2015-09-01T19:34:46-04:00"
title = "TRANSFERS"
linktitle = "TRANSFERS"
weight = 35
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Physical locations for patients throughout their hospital stay.

**Number of rows:** 261,897

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`

# Important considerations

* The ICUSTAYS table is derived from this table.
* Care units are defined based off the `WARDID` being associated with an ICU cost center.
* ICUs in the Beth Israel have moved throughout the years, and consequently the same `WARDID` may be considered as an ICU for patient A but not an ICU for patient B.

# Table columns

Name | Postgres data type 
---- | ---- 
ROW\_ID | INT
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

`DBSOURCE` contains the original ICU database the data was sourced from. Patients admitted between 2001 - 2008 had their data managed by the CareVue information system, represented in this column as 'carevue'. Patients admitted between 2008 - 2012 had their data managed by the Metavision system, represented in this column as 'metavision'. Knowing the database source is important as the data archiving for these two databases differs in some cases.

## `EVENTTYPE`

`EVENTTYPE` describes what transfer event occurred: 'admit' for an admission, 'transfer' for an inter-hospital transfer and 'discharge' for a discharge from the hospital.


## `PREV_CAREUNIT`, `CURR_CAREUNIT`

`PREV_CAREUNIT` contains the care unit in which the patient previously resided. `CURR_CAREUNIT` contains the care unit in which the patient currently resides. The care unit is defined based upon the ward: if the ward is an ICU cost center, then the care unit defines the type of ICU. If the ward is *not* an ICU then in most cases the care unit is null. There are one or two exceptions to this rule. For example, ```NWARD``` is a ward for newborns.

The `INTIME` and `OUTTIME` of the transfer event correspond to the `CURR_CAREUNIT`. The `PREV_CAREUNIT` for each row is provided for convenience, and is identical to the `CURR_CAREUNIT` of the previous row (assuming the event is not an admission).

## `PREV_WARDID`, `CURR_WARDID`

`PREV_WARDID` and `CURR_WARDID` contain the previous and current ward in which the patient stayed. Note that the grouping of physical locations in the hospital database is referred to as a ward. Though in practice ICUs are not referred to as wards, the hospital database technically tracks ICUs as "wards with an ICU cost center". As a result, each ICU is associated with a `WARDID`, but not every `WARDID` is an ICU.

## `INTIME`, `OUTTIME`

`INTIME` provides the date and time the patient was transferred into the current care unit from the previous care unit. `OUTTIME` provides the date and time the patient was transferred out of the current care unit.

## `LOS`

`LOS` is the length of stay for the patient for the given ward stay, which may be within or outside of the ICU.

