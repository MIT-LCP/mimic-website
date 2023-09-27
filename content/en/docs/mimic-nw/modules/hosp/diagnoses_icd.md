---
title: "diagnoses_icd"
linktitle: "diagnoses_icd"
weight: 5
date: 2023-09-18
description: >
  Billed ICD-9/ICD-10 diagnoses for hospitalizations.
---

The *diagnoses_icd* contains a record of all diagnoses a patient was billed for during their hospital stay using the ICD-9 and ICD-10 ontologies.
Diagnoses are billed on hospital discharge, and are determined by trained persons who read signed clinical notes.

### Links to

* *d_icd_diagnoses* ON `icd_code` and `icd_version`

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER NOT NULL
`icd_code` | VARCHAR(7)
`icd_version` | INTEGER

## Detailed Description

### `subject_id`

`subject_id` is unique identifier for each patient. `subject_id` is unique to each row and can be used to identify data associated with a specific patient. It is a cryptographic random number and each patient has a `subject_id` which is consistent across tables.

### `hadm_id`

Each row of this table contains a unique `hadm_id`, which represents a single patient's admission to the hospital. It is possible for this table to have duplicate `subject_id`, indicating that a single patient had multiple admissions to the hospital. The ADMISSIONS table can be linked to the *patients* table using `subject_id`.

### `icd_code` 

`icd_code` is the International Coding Definitions (ICD) code.

### `icd_version`

There are two versions for this coding system: version 9 (ICD-9) and version 10 (ICD-10). These can be differentiated using the `icd_version` column.

