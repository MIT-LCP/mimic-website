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

**Number of rows:** 4,234,967

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

<!-- # Important considerations -->

# Table columns

Name | Data type
---- | --------
subject\_id | INTEGER
hadm\_id | INTEGER
stay\_id | INTEGER
caregiver_id | INTEGER
charttime | TIMESTAMP(3)
storetime | TIMESTAMP(3)
itemid | INTEGER
value | DOUBLE PRECISION
valueuom | VARCHAR(20)

# Detailed Description

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

## `charttime`

`charttime` is the time of an output event.

## `storetime`

`storetime` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

## `value`, `valueuom`

`value` and `valueuom` list the amount of a substance at the `charttime` (when the exact start time is unknown, but usually up to an hour before).