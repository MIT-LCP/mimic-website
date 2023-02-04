---
title: "poe_detail"
linktitle: "poe_detail"
weight: 1
date: 2020-08-10
description: >
  Supplementary information for orders made by providers in the hospital.
---

## *poe_detail*

The *poe_detail* table provides further information on POE orders. The table uses an Entity-Attribute-Value (EAV) model: the entity is `poe_id`, the attribute is `field_name`, and the value is `field_value`.
EAV tables allow for flexible description of entities when the attributes are heterogenous.

## Links to

* *poe_detail* on `poe_id`

<!--

# Important considerations

-->

## Table columns

Name | Postgres data type
---- | ----
`poe_id` | VARCHAR(25) NOT NULL
`poe_seq` | INTEGER NOT NULL
`subject_id` | INTEGER NOT NULL
`field_name` | VARCHAR(255) NOT NULL
`field_value` | TEXT

### `poe_id`

A unique identifier for the given order. `poe_id` is composed of `subject_id` and a monotonically increasing integer, `poe_seq`, in the following format: `subject_id`-`poe_seq`.

### `poe_seq`

A monotonically increasing integer which chronologically sorts the POE orders. That is, POE orders can be ordered sequentially by `poe_seq`.

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

### `field_name`

Each row provides detail regarding a particular aspect of a POE order. `field_name` is the name given to that aspect.
As of MIMIC-IV v2.2, the following table lists the possible values and the most common entry for it in `field_value`.

`field_name` | number of rows | most frequent `field_value` observation
--- | --- | ---
Admit to | 881522 | Medicine
Indication | 27190 | Antibiotics
Code status | 197932 | Resuscitate (Full code)
Transfer to | 161707 | Medicine
Admit category | 1093726 | Admit to inpatient
Consult Status | 36591 | Accepted
Discharge When | 431642 | Discharge Now
Level of Urgency | 45617 | Routine (within 24 hours)
Discharge Planning | 475428 | Finalized
Consult Status Time | 36591 | 2149-12-03 09:00:01
Tubes & Drains type | 491472 | Indwelling urinary catheter (IUC) - Foley

### `field_value`

`field_value` is the value associated with the given POE order and `field_name`. For example, for the `field_name` of 'Admit to', the `field_value` column contains the type of unit the patient was admitted to (Psychiatry, GYN, and so on).
