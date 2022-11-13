---
title: "vitalsign table"
date: 2020-08-10
weight: 1
description: >
  vitalsign table
---

# The *vitalsign* table

Patients admitted to the emergency department have routine vital signs taken ever 1-4 hours. These vital signs are stored in the *vitalsign* table.

**Table source:** Emergency department information system.

**Table purpose:** Provides nurse documented vital signs.

**Number of rows:** 1,564,610

**Links to:**

* *edstays* on `stay_id`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
`subject_id`  | INTEGER NOT NULL
`stay_id`     | INTEGER NOT NULL
`charttime`   | TIMESTAMP(0)
`temperature` | NUMERIC(10, 4)
`heartrate`   | NUMERIC(10, 4)
`resprate`    | NUMERIC(10, 4)
`o2sat`       | NUMERIC(10, 4)
`sbp`         | INTEGER
`dbp`         | INTEGER
`rhythm`      | TEXT
`pain`        | TEXT

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `charttime`

The time at which the vital signs were charted.

## `temperature`

The patient's temperature in degrees Farenheit. Some temperatures may be incorrectly documented as Celsius.

## `heartrate`

The patient's heart rate in beats per minute.

## `resprate`

The patient's respiratory rate in breaths per minute.

## `o2sat`

The patient's oxygen saturation measured as a percentage.

## `sbp`, `dbp`

The patient's systolic (sbp) and diastolic (dbp) blood pressure measured in millimetres of mercury (mmHg).

<!-- o2flow -->

## `rhythm`

The patient's heart rhythm.

## `pain`

The patient's self-reported level of pain on a scale from 0-10. The pain is documented as free-text and may contain non-numeric entries.