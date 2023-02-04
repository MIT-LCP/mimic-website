---
title: "caregiver table"
linktitle: "caregiver"
date: 2023-02-03
weight: 1
description: >
  The caregiver table lists deidentified provider identifiers used in the ICU module.
---

## *caregiver*

A description table for the ICU caregivers in the ICU module referenced by *caregiver_id*.
As of MIMIC-IV v2.2, this table simply lists all unique `caregiver_id` in the database.

Note that, in order to distinguish identifiers used in the hospital wide EHR from those used in the ICU information system, we have adopted the nomenclature of "caregivers" for the ICU (`caregiver_id` and *caregivers*). For the hospital data in the hosp module, we use the terminology of "providers" (`provider_id` and *providers*). However, conceptually, both these sets of identifiers and tables refer to practicing providers at the hospital.

## Table columns

Name | Postgres data type
---- | ----
caregiver_id | VARCHAR(10) NOT NULL

### `caregiver_id`

`caregiver_id` lists all possible identifiers for caregivers used in the ICU module.
{{% include "/static/include/caregiver_id.md" %}}
