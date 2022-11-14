---
title: "diagnosis table"
date: 2020-08-10
weight: 1
description: >
  diagnosis table
---

# The *diagnosis* table

The *diagnosis* table provides billed diagnoses for patients. Diagnoses are determined after discharge from the emergency department.

**Table source:** Emergency department information system.

**Table purpose:** Track patient admissions to the emergency department.

**Number of rows:** 899,050

**Links to:**

* *edstays* on `stay_id`

# Table columns

Name | Postgres data type
---- | ----
`subject_id`    | INTEGER NOT NULL
`stay_id`       | INTEGER NOT NULL
`seq_num`       | INTEGER NOT NULL
`icd_code`      | VARCHAR(10) NOT NULL
`icd_version`   | INTEGER NOT NULL
`icd_title`     | TEXT NOT NULL

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `seq_num`

A pseudo-priority for the diagnosis. A `seq_num` of 1 usually indicates a "primary" diagnosis, but accurately assessing the priority for patients with multiple diagnoses is challenging.

## `icd_code`

A coded diagnosis using the International Classification of Diseases (ICD) ontology.

## `icd_version`

The version of the ICD system used; either 9 indicating ICD-9 or 10 indicating ICD-10. The ontologies for these two systems differ, and therefore the meaning of the `icd_code` will depend on the `icd_version`.

## `icd_title`

The textual description of the diagnosis.
