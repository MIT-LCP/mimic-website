---
title: "chartevents"
linktitle: "chartevents"
weight: 10
date: 2020-08-10
description: >
  Charted items occurring during the ICU stay. Contains the majority of information documented in the ICU.

---


# The chartevents table

**Table source:** MetaVision ICU database.

**Table purpose:** Contains all charted data for all patients.

**Number of rows:** 313,645,063

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

# Brief summary

*chartevents* contains all the charted data available for a patient. During their ICU stay, the primary repository of a patient's information is their electronic chart. The electronic chart displays patients' routine vital signs and any additional information relevant to their care: ventilator settings, laboratory values, code status, mental status, and so on. As a result, the bulk of information about a patient's stay is contained in *chartevents*. Furthermore, even though laboratory values are captured elsewhere (*labevents*), they are frequently repeated within *chartevents*. This occurs because it is desirable to display the laboratory values on the patient's electronic chart, and so the values are copied from the database storing laboratory values to the database storing the *chartevents*.

# Important considerations

* Some items are duplicated between the *labevents* and *chartevents* tables. In cases where there is disagreement between measurements, *labevents* should be taken as the ground truth.

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

## `subject_id`, `hadm_id`, `stay_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay and `stay_id` is unique to a patient ward stay. More information about these identifiers is [available here](/docs/iv/about/concepts/).

### `caregiver_id`

{{% include "/static/include/caregiver_id.md" %}}

## `charttime`, `storetime`

`charttime` records the time at which an observation was made, and is usually the closest proxy to the time the data was actually measured. `storetime` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## `itemid`

Identifier for a single measurement type in the database. Each row associated with one `itemid` (e.g. 220045) corresponds to an instantiation of the same measurement (e.g. heart rate).

## `value`, `valuenum`

`value` contains the value measured for the concept identified by the `itemid`. If this value is numeric, then `valuenum` contains the same data in a numeric format. If this data is not numeric, `valuenum` is null. In some cases (e.g. scores like Glasgow Coma Scale, Richmond Sedation Agitation Scale and Code Status), `valuenum` contains the score and `value` contains the score and text describing the meaning of the score.

## `valueuom`

`valueuom` is the unit of measurement for the `value`, if appropriate.

## `warning`

`warning` specifies if a warning for this observation was manually documented by the care provider.

