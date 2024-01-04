---
title: "procedureevents"
linktitle: "procedureevents"
weight: 4
date: 2023-09-18
description: >
  Procedures documented during the ICU stay (e.g. ventilation), though not necessarily conducted within the ICU (e.g. x-ray imaging).
---

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

# Important considerations

* In the context of COVID-19, we have observed a higher frequency of certain procedures, such as invasive ventilation. 

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

### `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ICU stay.

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

### `starttime`

Date and time when the procedure started.

### `endtime`

Date and time when the procedure ended.

### `storetime`

`storetime` specifies the time when the event was recorded in the system.

### `itemid`

Identifier for a single event type in the *procedurevents* table. Each row associated with one `itemid` (e.g. 225792) corresponds to a type of measurement (e.g. Invasive Ventilation) and `category` (e.g. 2-Ventilation). The *d_items* table may be joined on this field. For any itemid appearing in the *procedureevents* table, *d_items* `linksto` column will have the value 'procedureevents'.


## `value`

In the *procedureevents* table, this identifies the duration of the procedure (if applicable). For example, if querying for `itemid` 225794 (Non-invasive Ventilation), then the value column indicates the duration of ventilation therapy. 

### `valueuom`

The unit of measurement for the value. Most frequently 'None' (no value recorded); otherwise one of 'day', 'hour', or 'min'. A query for itemiid 225794 (Non-invasive Ventilation) returning a `value` of 461 and `valueuom` of 'min' would correspond to non-invasive ventilation provided for 461 minutes; this value is expected to match the difference between the `starttime` and `endtime` fields for the record. A procedure with `valueuom` equal to 'None' corresponds to a procedure which is instantaneous (e.g. intubation, patient transfer) or whose duration is not relevant (e.g. imaging procedures). For these records, there will be a difference of one second between `starttime` and `endtime` values.

### `statusdescription`

`statusdescription` states the ultimate status of the procedure referred to in the row. The statuses appearing on the *procedureevents* table are:

* `Paused` - The current delivery has been paused.
* `FinishedRunning` - The delivery of the item has finished (most frequently, the bag containing the compound is empty).
* `Stopped` - The delivery of the item been terminated by the caregiver.

Nearly all procedures recorded in *procedureevents* have a status of `FinishedRunning`.

In  NMHC, this column is usually missing. If not missing, one of the following is included:

* `Final result` - The final result of the procedure is available.
* `In process` - The procedure is currently in progress.
* `Edited Result - FINAL` - The result has been edited and finalized.
* `Preliminary result` - A preliminary result is available.
* `Edited` - The entry has been edited.
