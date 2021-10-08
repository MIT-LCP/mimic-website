---
title: "vitalsign_hl7 table"
date: 2020-08-10
weight: 1
description: >
  vitalsign_hl7 table
---

# The *vitalsign_hl7* table

**This table is not yet populated.**

Patients admitted to the emergency department may be monitored by telemetry.
Minute-by-minute vital signs for telemetry are communicated to a central server in the hospital, and these vital signs are recorded here.
However, vital signs are only communicated with patient identifiers manually input into the bedside monitors, a process which is not routine practice.
As a result, many patients who are monitored by telemetry do not have their vital signs recorded in this table.

**Table source:** Emergency department information system.

**Table purpose:** Continuous vital signs for monitored patients.

**Number of rows:** 0.

**Links to:**

* *edstays* on `stay_id`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`stay_id`    | INTEGER NOT NULL
`charttime`  | TIMESTAMP(0) NOT NULL
`hr`         | INTEGER
`resp`       | INTEGER
`spo2`       | INTEGER
`pulse`      | INTEGER
`nbp_d`      | INTEGER
`nbp_m`      | INTEGER
`nbp_s`      | INTEGER

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `charttime`

The date and time that the set of vital signs were recorded.

## `hr`

The patient's heart rate.

## `resp`

The patient's respiratory rate.

## `spo2`

The patient's peripheral oxygen saturation.

## `pulse`

The patient's heart rate derived from a photoplethysmogram.

## `nbp_d`, `nbp_m`, `nbp_s`

The patient's diastolic (d), mean (m), and systolic (s) blood pressure. The `n` indicates that the measurement was made non-invasively (i.e. with a blood pressure cuff).