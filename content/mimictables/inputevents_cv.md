+++
date = "2015-09-01T19:34:46-04:00"
title = "INPUTEVENTS_CV"
linktitle = "INPUTEVENTS_CV"
weight = 24
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"
+++

# Overview

**Table source:** CareVue ICU databases.

**Table purpose:** Input data for patients.

**Number of rows:** 17,528,894

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

A high level description of the data is available [here](/mimicdata/io).

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
AMOUNT | DOUBLE PRECISION
AMOUNTUOM | VARCHAR(30)
RATE | DOUBLE PRECISION
RATEUOM | VARCHAR(30)
STORETIME | TIMESTAMP(0)
CGID | BIGINT
ORDERID | BIGINT
LINKORDERID | BIGINT
STOPPED | VARCHAR(30)
NEWBOTTLE | INT
ORIGINALAMOUNT | DOUBLE PRECISION
ORIGINALAMOUNTUOM | VARCHAR(30)
ORIGINALROUTE | VARCHAR(30)
ORIGINALRATE | DOUBLE PRECISION
ORIGINALRATEUOM | VARCHAR(30)
ORIGINALSITE | VARCHAR(30)

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `STARTTIME`, `ENDTIME`

`STARTTIME` and `ENDTIME` record the start and end time of an input/output event.

* `STARTTIME` is only available for inputs, and is unavailable for a large portion of the data (see the [understanding IOEVENTS page](/mimicdata/ioevents))
* `ENDTIME` is the only time used for outputs

## ITEMID

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).
Metavision `ITEMID` values are all above 220000. A subset of commonly used medications in CareVue data have `ITEMID` values are between 30000-39999. The remaining input/output `ITEMID` values are between 40000-49999.

## AMOUNT, AMOUNTUOM

`AMOUNT` and `AMOUNTUOM` list the amount of a drug or substance administered to the patient either between the `STARTTIME` and `ENDTIME` (if both are available) or at the `ENDTIME` (when the exact start time is unknown, but usually up to an hour before).

## RATE, RATEUOM

`RATE` and `RATEUOM` list the rate at which the drug or substance was administered to the patient either between the `STARTTIME` and `ENDTIME` (if both are available), or it lists the rate at which the drug is *currently* administered at the `ENDTIME`.

## STORETIME

`STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## CGID

`CGID` is the identifier for the caregiver who validated the given measurement.

## ORDERID, LINKORDERID

`ORDERID` links multiple items contained in the same solution together. For example, when a solution of noradrenaline and normal saline is administered both noradrenaline and normal saline occur on distinct rows but will have the same `ORDERID`.

`LINKORDERID` links the same order across multiple instantiations: for example, if the rate of delivery for the solution with noradrenaline and normal saline is changed, two new rows which share the same new `ORDERID` will be generated, but the `LINKORDERID` will be the same.

## STOPPED, NEWBOTTLE

`STOPPED` indicates whether the infusion has been disconnected or continued. `NEWBOTTLE` indicates if a new preparation of the solution was hung at the bedside.

## ORIGINALAMOUNT, ORIGINALAMOUNTUOM, ORIGINALROUTE, ORIGINALRATE, ORIGINALRATEUOM , ORIGINALSITE

These columns provide information about the solution the medication was a part of when it was first entered into the information system.
