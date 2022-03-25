---
title: "ICU stays"
linktitle: "icustays"
weight: 10
date: 2020-08-10
description: >
  Tracking information for ICU stays including adminission and discharge times.
---


# The icustays table

**Table source:** Hospital database.

**Table purpose:** Defines each ICU stay in the database using STAY\_ID.

**Number of rows:** 76,540

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`

# Important considerations

* `stay_id` is a *generated* identifier that is *not* based on any raw data identifier. The hospital and ICU databases are not intrinsically linked and so do not have any concept of an ICU encounter identifier.
* The ICUSTAYS table is derived from the TRANSFERS table. 
  * Rows from the TRANSFERS table are excluded where the ward is not an ICU.
  * Rows from the TRANSFERS table are excluded where no heart rate measurements were recorded in the ICU system. Since some records in the TRANSFERS table are for administrative records only.
  * Consecutive ICU unit stays in the TRANSFERS table are counted as one ICU stay. 


# Table columns

Name | Postgres data type
---- | ----
subject\_id | INT
hadm\_id | INT
stay\_id | INT
first\_careunit | VARCHAR(20)
last\_careunit | VARCHAR(20)
intime | TIMESTAMP(0)
outtime | TIMESTAMP(0)
los | DOUBLE PRECISION

# Detailed Description

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ward stay.

## `FIRST_CAREUNIT`, `LAST_CAREUNIT`

`FIRST_CAREUNIT` and `LAST_CAREUNIT` contain, respectively, the first and last ICU type in which the patient was cared for. As an `stay_id` groups all ICU admissions within 24 hours of each other, it is possible for a patient to be transferred from one type of ICU to another and have the same `stay_id`.

Care units are derived from the TRANSFERS table, and definition for the abbreviations can be found in the documentation for TRANSFERS.

## `INTIME`, `OUTTIME`

`INTIME` provides the date and time the patient was transferred into the ICU. `OUTTIME` provides the date and time the patient was transferred out of the ICU.

## `LOS`

`LOS` is the length of stay for the patient for the given ICU stay, which may include one or more ICU units. The length of stay is measured in fractional days.
