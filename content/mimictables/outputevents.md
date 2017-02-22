+++
date = "2015-09-01T19:34:46-04:00"
title = "OUTPUTEVENTS"
linktitle = "OUTPUTEVENTS"
weight = 29
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"
+++

# The outputevents table

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Output data for patients.

**Number of rows:** 4,349,218

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
ICUSTAY\_ID | INT
CHARTTIME | TIMESTAMP(0)
ITEMID | INT
VALUE | DOUBLE PRECISION
VALUEUOM | VARCHAR(30)
STORETIME | TIMESTAMP(0)
CGID | BIGINT
STOPPED | VARCHAR(30)
NEWBOTTLE | INT
ISERROR | SMALLINT

# Detailed Description

## SUBJECT_ID, HADM_ID, ICUSTAY_ID

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## CHARTTIME

`CHARTTIME` is the time of an output event.

## ITEMID

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

Metavision `ITEMID` values are all above 220000. A subset of commonly used medications in CareVue data have `ITEMID` values are between 30000-39999. The remaining input/output `ITEMID` values are between 40000-49999.

## VALUE, VALUEUOM

`VALUE` and `VALUEUOM` list the amount of a substance at the `CHARTTIME` (when the exact start time is unknown, but usually up to an hour before).

## STORETIME

`STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## CGID

`CGID` is the identifier for the caregiver who validated the given measurement.

## STOPPED, NEWBOTTLE, ISERROR

`STOPPED` indicates if the order was disconnected at the given `CHARTTIME`. `NEWBOTTLE` indicates that a new bag of solution was hung at the given `CHARTTIME`. `ISERROR` is a Metavision checkbox where a care giver can specify that an observation is an error. No other details are provided.
