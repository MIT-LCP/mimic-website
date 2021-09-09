---
title: "outputevents"
linktitle: "outputevents"
weight: 10
date: 2020-08-10
description: >
  Information regarding patient outputs including urine, drainage, and so on.
---


# The *outputevents* table

**Table source:** MetaVision ICU database.

**Table purpose:** Output data for patients.

**Number of rows:** 3,703,137

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

<!-- # Important considerations -->

# Table columns

Name | Data type
---- | --------
subject\_id | Integer
hadm\_id | Integer
stay\_id | Integer
charttime | Date with times
storetime | Date with times
itemid | Integer
value | Floating point number
valueuom | Text

# Detailed Description

## subject_id, hadm_id, stay_id

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

<!-- 
## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

-->

## CHARTTIME

`CHARTTIME` is the time of an output event.

## STORETIME

`STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## ITEMID

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

## VALUE, VALUEUOM

`VALUE` and `VALUEUOM` list the amount of a substance at the `CHARTTIME` (when the exact start time is unknown, but usually up to an hour before).