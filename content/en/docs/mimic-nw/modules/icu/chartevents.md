---
title: "chartevents"
linktitle: "chartevents"
weight: 3
date: 2023-09-18
description: >
  Charted items during the ICU stay include numeric vital signs within respiratory, routine, general, and hemodynamic categories
---

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`


# Table columns

Name | Postgres Data type
---- | --------
subject\_id | INTEGER
hadm\_id | INTEGER
stay\_id | INTEGER
caregiver_id | INTEGER
charttime | TIMESTAMP(0)
storetime | TIMESTAMP(0)
itemid | INTEGER
value | VARCHAR(200)
valuenum | DOUBLE PRECISION
valueuom | VARCHAR(20)
warning | SMALLINT

### `subject_id`, `hadm_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay.

### `stay_id`

`stay_id` is an integer identifier which uniquely identifies each ICU admission within a hospital admission. Each hospital admission `hadm_id` must have at least one ICU admission `stay_id` but may include more than one. A `stay_id` groups all ICU admissions within 24 hours of each other.

### `caregiver_id`

`caregiver_id` uniquely identifies a single caregiver who measured the vital sign. 

### `charttime`

Date and time when the vital sign was measured, deidentified.

### `storetime`

`charttime` records the time at which an observation was made, and is usually the closest proxy to the time the data was actually measured. `storetime` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

### `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` (e.g. 220045) corresponds to an instantiation of the same measurement (e.g. Heart Rate) for Routine Vital Signs `category`, and 'bpm' `unit_name`.

### `value`, `valuenum`

`value` contains the numeric value in string format measured for the vital sign concept identified by the `itemid`. 

`valuenum` contains the same data in a numeric format. 

### `valueuom`

`valueuom` is the unit of measurement for the `value`, if appropriate. Either missing or “%”.

### `warning`

`warning` specifies if a warning for this observation was manually documented by the care provider. A value which is considered excessive for this measurement. Either an integer or missing.

