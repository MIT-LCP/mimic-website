---
title: "edstays table"
date: 2020-08-10
weight: 1
description: >
  edstays table
---

# The *edstays* table

The *edstays* table is the primary tracking table for emergency department visits.
It provides the time the patient entered the emergency department and the time they left the emergency department.

**Table source:** Emergency department information system.

**Table purpose:** Track patient admissions to the emergency department.

**Number of rows:** 448,972

**Links to:**

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id`    | INTEGER NOT NULL
`stay_id`    | INTEGER NOT NULL
`intime`     | TIMESTAMP(0) NOT NULL
`outtime`    | TIMESTAMP(0) NOT NULL

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `hadm_id`

If the patient was admitted to the hospital after their ED stay, `hadm_id` will contain the hospital identifier (ranges from 2000000 - 2999999). The `hadm_id` may be used to link the ED stay with the hospitalization in MIMIC-IV.

If `hadm_id` is `NULL`, the patient was not admitted to the hospital after their ED stay.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `intime`, `outtime`

The admission datetime (`intime`) and discharge datetime (`outtime`) of the given emergency department stay.
