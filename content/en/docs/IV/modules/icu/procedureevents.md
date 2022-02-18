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

**Number of rows:** 592,932

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
starttime | TIMESTAMP NOT NULL
endtime | TIMESTAMP NOT NULL
storetime | TIMESTAMP NOT NULL
itemid | Integer
value | Float (53)
valueuom | VARCHAR (20)
location |  VARCHAR(100)
locationcategory |  VARCHAR(50)
orderid |  Integer
linkorderid |  Integer
ordercategoryname |  VARCHAR(50)
secondaryordercategoryname |  VARCHAR(50)
ordercategorydescription |  VARCHAR(30)
patientweight | FLOAT(53)
totalamount | FLOAT(53)
totalamountuom | VARCHAR(50)
isopenbag |  SMALLINT
continueinnextdept |  SMALLINT
cancelreason |  SMALLINT
statusdescription |  VARCHAR(20)
comments_date | TIMESTAMP
<!-- originalamount | Float (53)
originalrate | Float (53)
These fields are present in the table and never null, but have no clear meaning.
In particular, "originalrate" is either 0 or 1 for all records.
-->

# Detailed Description

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

## `STARTTIME`, `ENDTIME`

`STARTTIME` and `ENDTIME` record the start and end time of an event.

## `STORETIME`

`STORETIME` specifies the time when the event was recorded in the system.

## `ITEMID`

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to a type of measurement (e.g. heart rate). The `mimic_icu.d_items` table may be joined on this field. For any itemid appearing in the `procedureevents` table, `mimic_icu.d_items.linksto` will have the value 'procedureevents'.

## `VALUE`

In the `procedureevents` table, this identifies the duration of the procedure (if applicable). For example, if querying for itemid 225794 (“Non-invasive Ventilation”), then the value column indicates the duration of ventilation therapy.

## `VALUEUOM`

The unit of measurement for the value. Most frequently "None" (no value recorded); otherwise one of "day", "hour", or "min". A query for itemiid 225794 ("Non-invasive Ventilation") returning a `value` of 461 and `valueuom` of 'min' would correspond to non-invasive ventilation provided for 461 minutes; this value is expected to match the difference between the `startTime` and `endTime` fields for the record. A procedure with `valueuom` equal to "None" corresponds to a procedure which is instantaneous (e.g. intubation, patient transfer) or whose duration is not relevant (e.g. imaging procedures). For these records, there will be a difference of one second between `startTime` and `endTime` values.

## `LOCATION` , `LOCATION CATEGORY`

`LOCATION` and `LOCATION CATEGORY` provide information about where on the patient's body the procedure is taking place. For example, the `location` might be 'Left Upper Arm' and the `locationcategory` might be 'Invasive Venous'.

## `ORDERID`, `LINKORDERID`

These columns link procedures to specific physician orders. Unlike in the `mimic_icu.inputevents` table, most procedures in `procedureevents` are ordered independently.

There are a limited number of records for which the same procedure was performed again at a later date under the same original order. When a procedure was repeated under the same original order, the `LINKORDERID` field of the record for the later procedure will be set to the `ORDERID` field of the earlier record. In all other cases, `ORDERID` = `LINKORDERID`.

## `ORDERCATEGORYNAME`, `SECONDARYORDERCATEGORYNAME`, `ORDERCATEGORYDESCRIPTION`

These columns provide higher level information about the medication/solution order. Categories represent the type of administration.

## `PATIENTWEIGHT`

The patient weight in kilograms.

## `TOTALAMOUNT`, `TOTALAMOUNTUOM`

These columns refer to intravenous administrations and are not recorded on the `procedureevents` table; they will be `null` for all entries.

## `ISOPENBAG`

Whether the order was from an open bag.

## `CONTINUEINNEXTDEPT`

If the order ended on patient transfer, this field indicates if it continued into the next department (e.g. a floor).

## `CANCELREASON`

This column is 0 for all records.

## `STATUSDESCRIPTION`

`STATUSDESCRIPTION` states the ultimate status of the procedure referred to in the row. The statuses appearing on the `procedureevents` table are:

* `Paused` - The current delivery has been paused.
* `FinishedRunning` - The delivery of the item has finished (most frequently, the bag containing the compound is empty).
* `Stopped` - The delivery of the item been terminated by the caregiver.

Nearly all procedures recorded in `procedureevents` have a status of `FinishedRunning`.

<!-- 
## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

-->
