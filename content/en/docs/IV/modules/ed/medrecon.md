---
title: "medrecon table"
date: 2020-08-10
weight: 1
description: >
  medrecon table
---

# The *medrecon* table

On admission to the emergency departments, staff will ask the patient what current medications they are taking. This process is called medicine reconciliation, and the *medrecon* table stores the findings of the care providers.

**Table source:** Emergency department information system.

**Table purpose:** Document medications a patient is currently taking.

**Number of rows:** 2,987,342

**Links to:**

* *edstays* on `stay_id`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
`subject_id`      | INTEGER NOT NULL
`stay_id`         | INTEGER NOT NULL
`charttime`       | TIMESTAMP(0)
`name`            | VARCHAR(255)
`gsn`             | VARCHAR(10)
`ndc`             | VARCHAR(12)
`etc_rn`          | SMALLINT NOT NULL
`etccode`         | VARCHAR(8)
`etcdescription`  | VARCHAR(255)

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `charttime`

The time at which the medicine reconciliation was charted.

## `name`

The name of the medication.

## `gsn`

The Generic Sequence Number (GSN), an ontology for the medication.

## `ndc`

The National Drug Code (ndc) for the medication.

## `etc_rn`, `etccode`, `etcdescription`

Medications are grouped using a hierarchical ontology known as the Enhanced Therapeutic Class (ETC). As more than one group may be associated with the medication, a sequential integer (`etc_rn`) was generated to differentiate the groups. There is no meaning to the order of `etc_rn`. `etccode` provides the code and `etcdescription` provides the description of the group.