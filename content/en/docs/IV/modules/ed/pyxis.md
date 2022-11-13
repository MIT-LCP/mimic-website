---
title: "pyxis table"
date: 2020-08-10
weight: 1
description: >
  pyxis table
---

# The *pyxis* table

The *pyxis* table provides information for medicine dispensations made via the Pyxis system.

Note that as the same medication may have multiple `gsn` values, each row does *not* necessarily indicate a unique dispensation. The `med_rn` column allows for subselecting to individual dispensations.

**Table source:** Emergency department information system.

**Table purpose:** Track medicine administrations.

**Number of rows:** 1,586,053

**Links to:**

* *edstays* on `stay_id`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`stay_id`   | INTEGER NOT NULL
`charttime` | TIMESTAMP(0)
`med_rn`    | SMALLINT NOT NULL
`name`      | VARCHAR(255)
`gsn_rn`    | SMALLINT NOT NULL
`gsn`       | VARCHAR(10)

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `charttime`

The time at which the medication was charted, which is the closest approximation to the time the medication was administered.

## `med_rn`

A row number for the medicine used to group single dispensations.

## `name`

The name of the medicine.

## `gsn`

The Generic Sequence Number (GSN), an ontology which provides a code for each medicine.

## `gsn_rn`

As a medicine may be a member of multiple groups in the GSN ontology, this row number differentiates them. The order of `gsn_rn` has no meaning.