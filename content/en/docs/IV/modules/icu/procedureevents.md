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

`STORETIME` specifies the 'Time when the event was recorded in the system'.

## `ITEMID`

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to a type of measurement (e.g. heart rate).

## `VALUE`

This is the value that corresponds to the concept referred to by itemid. For example, if querying for itemid: 225794 (“Non-invasive Ventilation”), then the value column indicates the duration of the procedure.

## `VALUEUOM`

The unit of measurement for the value. Most frequently "None" (no value recorded); otherwise one of "day", "hour", "min". A query for itemiid 225794 ("Non-invasive Ventilation") with a `value` of 461 and `valueuom` of `min` would correspond to non-invasive ventilation provided for 461 minutes (which should match the difference between the `startTime` and `endTime` fields for the record). A procedure with `valueuom` equal to "None" corresponds to a procedure whose duration is not recorded (e.g. imaging procedures) and will show a difference of one second between `startTime` and `endTime` values.

## `LOCATION` , `LOCATION CATEGORY`

`LOCATION` and `LOCATION CATEGORY` provide information about where the procedure is taking place. For example, the `location` might be 'Left Upper Arm' and the `locationcategory` might be 'Invasive Venous'.

## `ORDERID`, `LINKORDERID`

`ORDERID` links multiple items contained in the same solution together. For example, when a solution of noradrenaline and normal saline is administered both noradrenaline and normal saline occur on distinct rows but will have the same `ORDERID`.

`LINKORDERID` links the same order across multiple rows. For example, if the rate of delivery for the solution with noradrenaline and normal saline is changed, two new rows which share the same new `ORDERID` will be generated, but the `LINKORDERID` will be the same.

## `ORDERCATEGORYNAME`, `SECONDARYORDERCATEGORYNAME`, `ORDERCOMPONENTTYPEDESCRIPTION`, `ORDERCATEGORYDESCRIPTION`

These columns provide higher level information about the medication/solution order. Categories represent the type of administration, while the `ORDERCOMPONENTTYPEDESCRIPTION` describes the role of the substance in the solution (i.e. main order parameter, additive, or mixed solution).

## `PATIENTWEIGHT`

The patient weight in kilograms.

## `TOTALAMOUNT`, `TOTALAMOUNTUOM`

Intravenous administrations are usually given by hanging a bag of fluid at the bedside for continuous infusion over a certain period of time. These columns list the total amount of the fluid in the bag containing the solution.

## `ISOPENBAG`

Whether the order was from an open bag.

## `CONTINUEINNEXTDEPT`

If the order ended on patient transfer, this field indicates if it continued into the next department (e.g. a floor).

## `CANCELREASON`

If the order was canceled, this column provides some explanation.

## `STATUSDESCRIPTION`

`STATUSDESCRIPTION` states the ultimate status of the item, or more specifically, row. It is used to indicate why the delivery of the compound has ended. There are only six possible statuses:

* `Changed` - The current delivery has ended as some aspect of it has changed (most frequently, the rate has been changed).
* `Paused` - The current delivery has been paused.
* `FinishedRunning` - The delivery of the item has finished (most frequently, the bag containing the compound is empty).
* `Stopped` - The delivery of the item been terminated by the caregiver.
* `Rewritten` - Incorrect information was input, and so the information in this row was rewritten (these rows are primarily useful for auditing purposes. The rates/amounts described were *not* delivered and so should not be used if determining what compounds a patient has received).
* `Flushed` - A line was flushed.

<!-- 
## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

-->
