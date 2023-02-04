---
title: "procedureevents"
linktitle: "procedureevents"
weight: 10
date: 2020-08-10
description: >
  Procedures documented during the ICU stay (e.g. ventilation), though not necessarily conducted within the ICU (e.g. x-ray imaging).
---


# The procedureevents table

**Table source:** MetaVision ICU database.

**Table purpose:** Contains procedures for patients

**Number of rows:** 696,092

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

# Important considerations

This table is **not** a required documentation field during routine care. As a result, existence of procedures here indicates their presence, but absence does not indicate the procedure was not conducted. The consistency of documentation varies by the type of procedure. For example, invasive ventilation tends to be documented, whereas non-invasive documentation is less consistently documented.

# Table columns


Name | Data type
---- | --------
subject\_id | INTEGER
hadm\_id | INTEGER
stay\_id | INTEGER
caregiver_id | INTEGER
starttime | TIMESTAMP
endtime | TIMESTAMP
storetime | TIMESTAMP
itemid | INTEGER
value | DOUBLE PRECISION
valueuom | VARCHAR(20)
location |  VARCHAR(100)
locationcategory |  VARCHAR(50)
orderid |  INTEGER
linkorderid |  INTEGER
ordercategoryname |  VARCHAR(50)
ordercategorydescription |  VARCHAR(30)
patientweight | DOUBLE PRECISION
isopenbag |  SMALLINT
continueinnextdept |  SMALLINT
statusdescription |  VARCHAR(20)
originalamount | DOUBLE PRECISION
originalrate | DOUBLE PRECISION

# Detailed Description

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

## `starttime`, `endtime`

`starttime` and `endtime` record the start and end time of an event.

## `storetime`

`storetime` specifies the time when the event was recorded in the system.

## `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` (e.g. 212) corresponds to a type of measurement (e.g. heart rate). The *d_items* table may be joined on this field. For any itemid appearing in the *procedureevents* table, *d_items* `linksto` column will have the value 'procedureevents'.

## `value`

In the `procedureevents` table, this identifies the duration of the procedure (if applicable). For example, if querying for itemid 225794 (“Non-invasive Ventilation”), then the value column indicates the duration of ventilation therapy.

## `valueuom`

The unit of measurement for the value. Most frequently "None" (no value recorded); otherwise one of "day", "hour", or "min". A query for itemiid 225794 ("Non-invasive Ventilation") returning a `value` of 461 and `valueuom` of 'min' would correspond to non-invasive ventilation provided for 461 minutes; this value is expected to match the difference between the `starttime` and `endtime` fields for the record. A procedure with `valueuom` equal to "None" corresponds to a procedure which is instantaneous (e.g. intubation, patient transfer) or whose duration is not relevant (e.g. imaging procedures). For these records, there will be a difference of one second between `starttime` and `endtime` values.

## `location` , `locationcategory`

`location` and `locationcategory` provide information about where on the patient's body the procedure is taking place. For example, the `location` might be 'Left Upper Arm' and the `locationcategory` might be 'Invasive Venous'.

## `orderid`, `linkorderid`

These columns link procedures to specific physician orders. Unlike in the `mimic_icu.inputevents` table, most procedures in `procedureevents` are ordered independently.

There are a limited number of records for which the same procedure was performed again at a later date under the same original order. When a procedure was repeated under the same original order, the `linkorderid` field of the record for the later procedure will be set to the `orderid` field of the earlier record. In all other cases, `orderid` = `linkorderid`.

## `ordercategoryname`, `ordercategorydescription`

These columns provide higher level information about the medication/solution order. Categories represent the type of administration.

## `patientweight`

The patient weight in kilograms.

## `isopenbag`

Whether the order was from an open bag.

## `continueinnextdept`

If the order ended on patient transfer, this field indicates if it continued into the next department (e.g. a floor).

## `statusdescription`

`statusdescription` states the ultimate status of the procedure referred to in the row. The statuses appearing on the `procedureevents` table are:

* `Paused` - The current delivery has been paused.
* `FinishedRunning` - The delivery of the item has finished (most frequently, the bag containing the compound is empty).
* `Stopped` - The delivery of the item been terminated by the caregiver.

Nearly all procedures recorded in *procedureevents* have a status of `FinishedRunning`.

## `originalamount`, `originalrate`

These fields are present in the table and never null, but have no clear meaning.
In particular, "originalrate" is either 0 or 1 for all records.
