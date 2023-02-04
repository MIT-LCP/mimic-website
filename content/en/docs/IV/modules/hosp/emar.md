---
title: "emar"
linktitle: "emar"
weight: 1
date: 2020-08-10
description: >
  The Electronic Medicine Administration Record (eMAR); barcode scanning of medications at the time of administration.
---

## *emar*

The EMAR table is used to record administrations of a given medicine to an individual patient.
Records in this table are populated by bedside nursing staff scanning barcodes associated with the medicine and the patient.

## Links to

* *emar_detail* on `emar_id`
* *pharmacy* on `pharmacy_id`
* *prescriptions* on `pharmacy_id`
* *poe* on `poe_id`


## Important considerations

* The eMAR system was implemented during 2011-2013. As a result, eMAR data is not available for all patients.

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER
`emar_id` | VARCHAR(25) NOT NULL
`emar_seq` | INTEGER NOT NULL
`poe_id` | VARCHAR(25) NOT NULL
`pharmacy_id` | INTEGER
`enter_provider_id` | VARCHAR(10)
`charttime` | TIMESTAMP NOT NULL
`medication` | TEXT
`event_txt` | VARCHAR(100)
`scheduletime` | TIMESTAMP
`storetime` | TIMESTAMP NOT NULL

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

### `hadm_id`

{{% include "/static/include/hadm_id.md" %}}

### `emar_id`, `emar_seq`

Identifiers for the eMAR table. `emar_id` is a unique identifier for each order made in eMAR. `emar_seq` is a consecutive integer which numbers eMAR orders chronologically. `emar_id` is composed of `subject_id` and `emar_seq` in the following pattern: '`subject_id`-`emar_seq`'.

### `poe_id`

An identifier which links administrations in *emar* to orders in *poe* and *prescriptions*.

### `pharmacy_id`

An identifier which links administrations in *emar* to pharmacy information in the *pharmacy* table.

### `enter_provider_id`

`enter_provider_id` provides an anonymous identifier for the provider who entered the information into the eMAR system.
{{% include "/static/include/provider_id.md" %}}

### `charttime`

The time at which the medication was administered.

### `medication`

The name of the medication which was administered.

### `event_txt`

Information about the administration. Most frequently `event_txt` is 'Administered', but other possible values are 'Applied', 'Confirmed', 'Delayed', 'Not Given', and so on.

### `scheduletime`

If present, the time at which the administration was scheduled.

### `storetime`

The time at which the administration was documented in the eMAR table.
