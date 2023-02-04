---
title: "emar_detail"
linktitle: "emar_detail"
weight: 1
date: 2020-08-10
description: >
  Supplementary information for electronic administrations recorded in *emar*.
---

## *emar_detail*

The *emar_detail* table contains information for each medicine administration made in the EMAR table.
Information includes the associated pharmacy order, the dose due, the dose given, and many other parameters associated with the medical administration.

## Links to

* *emar* on `emar_id`
* *pharmacy* on `pharmacy_id`

## Important considerations

* The eMAR system was implemented during 2011-2013. As a result, eMAR data is not available for all patients.

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`emar_id` | VARCHAR(25) NOT NULL
`emar_seq` | INTEGER NOT NULL
`parent_field_ordinal` | VARCHAR(10)
`administration_type` | VARCHAR(50)
`pharmacy_id` | INTEGER
`barcode_type` | VARCHAR(4)
`reason_for_no_barcode` | TEXT
`complete_dose_not_given` | VARCHAR(5)
`dose_due` | VARCHAR(100)
`dose_due_unit` | VARCHAR(50)
`dose_given` | VARCHAR(255)
`dose_given_unit` | VARCHAR(50)
`will_remainder_of_dose_be_given` | VARCHAR(5)
`product_amount_given` | VARCHAR(30)
`product_unit` | VARCHAR(30)
`product_code` | VARCHAR(30)
`product_description` | VARCHAR(255)
`product_description_other` | VARCHAR(255)
`prior_infusion_rate` | VARCHAR(40)
`infusion_rate` | VARCHAR(40)
`infusion_rate_adjustment` | VARCHAR(50)
`infusion_rate_adjustment_amount` | VARCHAR(30)
`infusion_rate_unit` | VARCHAR(30)
`route` | VARCHAR(10)
`infusion_complete` | VARCHAR(1)
`completion_interval` | VARCHAR(50)
`new_iv_bag_hung` | VARCHAR(1)
`continued_infusion_in_other_location` | VARCHAR(1)
`restart_interval` | TEXT
`side` | VARCHAR(10)
`site` | VARCHAR(255)
`non_formulary_visual_verification` | VARCHAR(1)

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

### `emar_id`, `emar_seq`

Identifiers for the eMAR table. `emar_id` is a unique identifier for each order made in eMAR. `emar_seq` is a consecutive integer which numbers eMAR orders chronologically. `emar_id` is composed of `subject_id` and `emar_seq` in the following pattern: '`subject_id`-`emar_seq`'.

### `parent_field_ordinal`

`parent_field_ordinal` delineates multiple administrations for the same eMar event, e.g. multiple formulary doses for the full dose. As eMAR requires the administrating provider to scan a barcode for *each* formulary provided to the patient, it is often the case that multiple rows in *emar_detail* correspond to a single row in *emar* (e.g. multiple pills are administered which add up to the desired dose). The structure for *emar_detail* rows is as follows:

* There is one row per eMAR order with a NULL `parent_field_ordinal`: this row usually contains the desired dose for the administration.
* Afterward, if there are N formulary doses, `parent_field_ordinal` will take values '1.1', '1.2', ..., '1.N'.

The most common case occurs when there is only one formulary dose per medication. In this case the `emar_id` will have two rows in the *emar_detail* table: one with a NULL value for `parent_field_ordinal` (usually providing the dose due), and one row with a value of '1.1' for `parent_field_ordinal` (usually providing the actual dose administered).

### `administration_type`

The type of administration, including 'IV Bolus', 'IV Infusion', 'Medication Infusion', 'Transdermal Patch', and so on.

### `pharmacy_id`

An identifier which allows linking the eMAR order to pharmacy information provided in the *pharmacy* table. Note: rarely the same `emar_id` may have multiple distinct `pharmacy_id` across rows in the *emar_detail* table.

### Remaining columns

The remaining columns provide information about the delivery of the formulary dose of the administered medication.
