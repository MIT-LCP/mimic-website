---
title: "datetimeevents"
linktitle: "datetimeevents"
weight: 10
date: 2020-08-10
description: >
  Documented information which is in a date format (e.g. date of last dialysis).
---


# The datetimeevents table

**Table source:** MetaVision ICU database.

**Table purpose:** Contains all date formatted data.

**Number of rows:** 7,112,999

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

<!-- # Important considerations -->

# Table columns


Name | Postgres Data type
---- | --------
subject\_id | INTEGER
hadm\_id | INTEGER
stay\_id | INTEGER
caregiver_id | INTEGER
charttime | TIMESTAMP(3)
storetime | TIMESTAMP(3)
itemid | INTEGER
value | TIMESTAMP(3)
valueuom | VARCHAR(20)
warning | SMALLINT
	
# Detailed Description

*datetimeevents* contains all date measurements about a patient in the ICU. For example, the date of last dialysis would be in the *datetimeevents* table, but the systolic blood pressure would not be in this table. As all dates in MIMIC are anonymized to protect patient confidentiality, all dates in this table have been shifted. Note that the chronology for an individual patient has been unaffected however, and quantities such as the difference between two dates remain true to reality.

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ward stay.

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

## `charttime`, `storetime`

`charttime` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured. `storetime` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

## `value`

The documented date - this is the value that corresponds to the concept referred to by `itemid`. For example, if querying for `itemid`: 225755 ("18 Gauge Insertion Date"), then the `value` column indicates the date the line was inserted.

## `valueuom`

The unit of measurement for the value - almost always the text string "Date".

## `warning`

`warning` specifies if a warning for this observation was manually documented by the care provider.