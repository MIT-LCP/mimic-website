+++
date = "2015-09-01T19:34:46-04:00"
title = "ICUSTAYS"
linktitle = "ICUSTAYS"
weight = 24
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"
+++


# Overview

**Table source:** Hospital database.

**Table purpose:** Defines each ICUSTAY\_ID in the database, i.e. defines a single ICU stay.

**Number of rows:** 61,532

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
ICUSTAY\_ID | INT
DBSOURCE | VARCHAR(20)
FIRST\_CAREUNIT | VARCHAR(20)
LAST\_CAREUNIT | VARCHAR(20)
FIRST\_WARDID | SMALLINT
LAST\_WARDID | SMALLINT
INTIME | TIMESTAMP(0)
OUTTIME | TIMESTAMP(0)
LOS | DOUBLE | PRECISION
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `DBSOURCE`

`DBSOURCE` contains the original ICU database the data was sourced from. Patients admitted between 2001 - 2008 had their data managed by the CareVue information system, represented in this column as 'carevue'. Patients admitted between 2008 - 2012 had their data managed by the Metavision system, represented in this column as 'metavision'. Knowing the database source is important as the data archiving for these two databases differs in some cases.

## `FIRST_CAREUNIT`, `LAST_CAREUNIT`

`FIRST_CAREUNIT` and `LAST_CAREUNIT` contain, respectively, the first and last ICU type in which the patient was cared for. As an `ICUSTAY_ID` groups all ICU admissions within 24 hours of each other, it is possible for a patient to be transferred from one type of ICU to another and have the same ICU ID.

## `FIRST_WARDID`, `LAST_WARDID`

`FIRST_WARDID` and `LAST_WARDID` contain the first and last ICU unit in which the patient stayed. Note the grouping of physical locations in the hospital database is referred to as ward. Though in practice ICUs are not referred to as wards, the hospital database technically tracks ICUs as "wards with an ICU cost center". As a result, each ICU is associated with a `WARDID`.

## `INTIME`, `OUTTIME`

`INTIME` provides the date and time the patient was transferred into the ICU. `OUTTIME` provides the date and time the patient was transferred out of the ICU.

## `LOS`

`LOS` is the length of stay for the patient for the given ICU stay, which may include one or more ICU units.

# Important considerations

* `ICUSTAY_ID` is a *generated* identifier, that is it is *not* based off any raw data identifier. The hospital and ICU databases are not intrinsically linked, and so do not have any concept of an ICU encounter identifier.
* The ICUSTAYS table is derived from the TRANSFERS table. Specifically, it groups the TRANSFERS table based on ICUSTAY\_ID, and excludes rows where no ICUSTAY\_ID is present.
