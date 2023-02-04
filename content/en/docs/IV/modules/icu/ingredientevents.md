---
date: "2022-06-12T00:00:00-04:00"
title: "Ingredientevents"
linktitle: "Ingredientevents"
weight: 10
date: 2020-08-10
description: >
  Ingredients of continuous or intermittent administrations including nutritional and water content.
---

# The *inputevents* table

**Table source:** MetaVision ICU database.

**Table purpose:** Ingredients contained within inputs data for patients.

**Number of rows:** 12,229,408

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

# Important considerations

* In the source data, there is no concept of a volume in the database: only a `rate`. All rows are recorded with a `starttime` and an `endtime`. The `amount` in this table is *derived* from the `rate` column, and provided for convenience. An exception is bolus administrations: these are listed as ending one minute after they started, i.e. `endtime`: `starttime` + 1 minute, and they do not have a `rate`.

# Table columns

Name | Postgres data type
---- | ----
subject\_id | INTEGER
hadm\_id | INTEGER
stay\_id | INTEGER
caregiver_id | INTEGER
starttime | TIMESTAMP(0)
endtime | TIMESTAMP(0)
storetime | TIMESTAMP(0)
itemid | INTEGER
amount | DOUBLE PRECISION
amountuom | VARCHAR(20)
rate | DOUBLE PRECISION
rateuom | VARCHAR(20)
orderid | INTEGER
linkorderid | INTEGER
statusdescription | VARCHAR(20)
originalamount | DOUBLE PRECISION
originalrate | DOUBLE PRECISION

# Detailed Description

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

## `starttime`, `endtime`

`starttime` and `endtime` record the start and end time of the event.

## `storetime`

`storetime` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` which corresponds to an instantiation of the same measurement (e.g. norepinephrine).

## `amount`, `amountuom`

`amount` and `amountuom` list the amount of a drug or substance administered to the patient either between the `starttime` and `endtime`.

## `rate`, `rateuom`

`rate` and `rateuom` list the rate at which the drug or substance was administered to the patient either between the `starttime` and `endtime`.

## `orderid`, `linkorderid`

`orderid` links multiple items contained in the same solution together. For example, when a solution of noradrenaline and normal saline is administered both noradrenaline and normal saline occur on distinct rows but will have the same `orderid`.

`linkorderid` links the same order across multiple instantiations: for example, if the rate of delivery for the solution with noradrenaline and normal saline is changed, two new rows which share the same new `orderid` will be generated, but the `linkorderid` will be the same.

## `statusdescription`

`statusdescription` states the ultimate status of the item, or more specifically, row. It is used to indicate why the delivery of the compound has ended. There are only six possible statuses:

* Changed - The current delivery has ended as some aspect of it has changed (most frequently, the rate has been changed)
* Paused - The current delivery has been paused
* FinishedRunning - The delivery of the item has finished (most frequently, the bag containing the compound is empty)
* Stopped - The delivery of the item been terminated by the caregiver
* Rewritten - Incorrect information was input, and so the information in this row was rewritten (these rows are primarily useful for auditing purposes - the rates/amounts described were *not* delivered and so should not be used if determining what compounds a patient has received)
* Flushed - A line was flushed.

## `originalamount`

Drugs are usually mixed within a solution and delivered continuously from the same bag. This column represents the amount of the compound contained in the bag at `starttime`.

## `originalrate`

This is the rate that was input by the care provider. Note that this may differ from `rate` because of various reasons: `originalrate` was the original planned rate, while the `rate` column will be the true rate delivered.