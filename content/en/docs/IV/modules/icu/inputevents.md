---
date: "2015-09-01T19:34:46-04:00"
title: "Inputevents"
linktitle: "inputevents"
weight: 10
date: 2020-08-10
description: >
  Information documented regarding continuous infusions or intermittent administrations.
---

# The *inputevents* table

**Table source:** MetaVision ICU database.

**Table purpose:** Input data for patients.

**Number of rows:** 8,978,893

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

# Brief example

The original source database recorded input data using two tables: RANGESIGNALS and ORDERENTRY. These tables do not appear in MIMIC as they have been merged to form the INPUTEVENTS table. RANGESIGNALS contains recorded data elements which last for a fixed period of time. Furthermore, the RANGESIGNALS table recorded information for each component of the drug separately. For example, for a norepinephrine administration there would be two components: a main order component (norepinephrine) and a solution component (NaCl). The `starttime` and `endtime` of RANGESIGNALS indicated when the drug started and finished. *Any* change in the drug rate would result in the current infusion ending, and a new `starttime` being created.

Let's examine an example of a patient being given norepinephrine.

Item | `starttime` | `endtime` | `rate` | `rateuom` | `orderid` | `linkorderid`
---- | ---- | ---- | ---- | ---- | ---- | ----
Norepinephrine | 18:20 | 18:25 | 1 | mcg/kg/min | 8003 | 8003
NaCl | 18:20 | 18:25 | 10 | ml/hr | 8003 | 8003
Norepinephrine | 18:25 | 20:00 | 2 | mcg/kg/min | 8020 | 8003
NaCl | 18:25 | 20:00 | 20 | ml/hr | 8020 | 8003

The `starttime` for the solution (NaCl) and the drug (norepinephrine) would be 18:20. The rate of the drug is 1 mcg/kg/min, and the rate of the solution is 10 mL/hr. The nurse decides to increase the drug rate at 18:25 to 2 mcg/kg/min. As a result, the `endtime` for the two rows corresponding to the solution (NaCl and norepinephrine) is set to 18:25. Two new rows are generated with a `starttime` of 18:25. These two new rows would continue until either (i) the drug rate was changed or (ii) the drug was delivery was discontinued. The `orderid` column is used to group drug delivery with rate of delivery. In this case, we have NaCl and norepinephrine in the same bag delivered at the same time - as a result their `orderid` is the same (8003). When the rate is changed, a new `orderid` is generated (8020). The column `linkorderid` can be used to link this drug across all administrations, even when the rate is changed. Note also that `linkorderid` is always equal to the first `orderid` which occurs for the solution, as demonstrated in the example above.

# Important considerations

* For Metavision data, there is no concept of a volume in the database: only a `rate`. All inputs are recorded with a `starttime` and an `endtime`. As a result, the volumes in the database for Metavision patients are *derived* from the rates. Furthermore, exact start and stop times for the drugs are easily deducible.
* A bolus will be listed as ending one minute after it started, i.e. `endtime`: `starttime` + 1 minute

# Table columns

Name | Postgres data type
---- | ----
subject\_id | INT
hadm\_id | INT
stay\_id | INT
caregiver_id | INTEGER
starttime | TIMESTAMP(0)
endtime | TIMESTAMP(0)
storetime | TIMESTAMP(0)
itemid | INT
amount | DOUBLE PRECISION
amountuom | VARCHAR(30)
rate | DOUBLE PRECISION
rateuom | VARCHAR(30)
orderid | BIGINT
linkorderid | BIGINT
ordercategoryname | VARCHAR(100)
secondaryordercategoryname | VARCHAR(100)
ordercomponenttypedescription | VARCHAR(200)
ordercategorydescription | VARCHAR(50)
patientweight | DOUBLE PRECISION
totalamount | DOUBLE PRECISION
totalamountuom | VARCHAR(50)
`isopenbag` | SMALLINT
statusdescription | VARCHAR(30)
originalamount | DOUBLE PRECISION
originalrate | DOUBLE PRECISION

# Detailed Description

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

## `starttime`, `endtime`

`starttime` and `endtime` record the start and end time of an input/output event.

## `storetime`

`storetime` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` which corresponds to an instantiation of the same measurement (e.g. norepinephrine).

## `amount`, `amountuom`

`amount` and `amountuom` list the amount of a drug or substance administered to the patient either between the `starttime` and `endtime`.

## rate, rateuom

`rate` and `rateuom` list the rate at which the drug or substance was administered to the patient either between the `starttime` and `endtime`.

## orderid, linkorderid

`orderid` links multiple items contained in the same solution together. For example, when a solution of noradrenaline and normal saline is administered both noradrenaline and normal saline occur on distinct rows but will have the same `orderid`.

`linkorderid` links the same order across multiple instantiations: for example, if the rate of delivery for the solution with noradrenaline and normal saline is changed, two new rows which share the same new `orderid` will be generated, but the `linkorderid` will be the same.

## `ordercategoryname`, `secondaryordercategoryname`, `ordercomponenttypedescription`, `ordercategorydescription`

These columns provide higher level information about the order the medication/solution is a part of. Categories represent the type of administration, while the `ordercomponenttypedescription` describes the role of the substance in the solution (i.e. main order parameter, additive, or mixed solution)

## `patientweight`

The patient weight in kilograms.

## `totalamount`, `totalamountuom`

Intravenous administrations are usually given by hanging a bag of fluid at the bedside for continuous infusion over a certain period of time. These columns list the total amount of the fluid in the bag containing the solution.

## `isopenbag`

Whether the order was from an open bag.

## `continueinnextdept`

If the order ended on patient transfer, this field indicates if it continued into the next department (e.g. a floor).

## `statusdescription`

`statusdescription` states the ultimate status of the item, or more specifically, row. It is used to indicate why the delivery of the compound has ended. There are only six possible statuses:

* Changed - The current delivery has ended as some aspect of it has changed (most frequently, the rate has been changed)
* Paused - The current delivery has been paused
* FinishedRunning - The delivery of the item has finished (most frequently, the bag containing the compound is empty)
* Stopped - The delivery of the item been terminated by the caregiver
* Flushed - A line was flushed.

## `originalamount`

Drugs are usually mixed within a solution and delivered continuously from the same bag. This column represents the amount of the drug contained in the bag at `starttime`. For the first infusion of a new bag, `originalamount`: `totalamount`. Later on, if the rate is changed, then the amount of the drug in the bag will be lower (as some has been administered to the patient). As a result, `originalamount` < `totalamount`, and `originalamount` will be the amount of drug leftover in the bag at that `starttime`.

## `originalrate`

This is the rate that was input by the care provider. Note that this may differ from `rate` because of various reasons: `originalrate` was the original planned rate, while the `rate` column will be the true rate delivered. For example, if a a bag is about to run out and the care giver decides to push the rest of the fluid, then `rate` > `originalrate`.
However, these two columns are usually the same, but have minor non-clinically significant differences due to rounding error.