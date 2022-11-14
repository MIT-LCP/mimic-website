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

**Number of rows:** 425,087

**Links to:**

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
`subject_id`        | INTEGER NOT NULL
`hadm_id`           | INTEGER NOT NULL
`stay_id`           | INTEGER NOT NULL
`intime`            | TIMESTAMP(0) NOT NULL
`outtime`           | TIMESTAMP(0) NOT NULL
`gender`            | VARCHAR(1) NOT NULL
`race`              | VARCHAR(60)
`arrival_transport` | VARCHAR(50) NOT NULL
`disposition`       | VARCHAR(255)


## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `hadm_id`

If the patient was admitted to the hospital after their ED stay, `hadm_id` will contain the hospital identifier (ranges from 2000000 - 2999999). The `hadm_id` may be used to link the ED stay with the hospitalization in MIMIC-IV.

If `hadm_id` is `NULL`, the patient was not admitted to the hospital after their ED stay.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `intime`, `outtime`

The admission datetime (`intime`) and discharge datetime (`outtime`) of the given emergency department stay.

## `gender`

The patient's administrative gender as documented in the hospital system.

## `race`

The patient's self-reported race. Race is aggregated into higher level categories for very small groups.
As of MIMIC-IV-ED v2.1, there were 33 unique categories for race.

## `arrival_transport`

The method through which the individual arrived at the ED. A count of the possible entries is provided below.

arrival_transport | count
--- | ---
WALK IN           | 251849
AMBULANCE         | 155752
UNKNOWN           |  15352
OTHER             |   1266
HELICOPTER        |    868

## `disposition`

The method through which the individual left the ED. Of the non-null methods, the possibilities include:

disposition | count
--- | ---
HOME                         | 241632
ADMITTED                     | 158010
TRANSFER                     | 7025
LEFT WITHOUT BEING SEEN      | 6155
OTHER                        | 4297
LEFT AGAINST MEDICAL ADVICE  | 1881
ELOPED                       | 5710
EXPIRED                      | 377