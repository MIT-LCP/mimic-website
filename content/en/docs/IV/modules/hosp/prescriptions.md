---
title: "prescriptions"
linktitle: "prescriptions"
weight: 1
date: 2020-08-10
description: >
  Prescribed medications.
---

## *prescriptions*

The *prescriptions* table provides information about prescribed medications. Information includes the name of the drug, coded identifiers including the Generic Sequence Number (GSN) and National Drug Code (NDC), the product strength, the formulary dose, and the route of administration.

## Links to

* *pharmacy* on `pharmacy_id`
* *emar* on `pharmacy_id`

<!--

# Important considerations

-->

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER NOT NULL
`pharmacy_id` | INTEGER
`poe_id` | VARCHAR(25)
`poe_seq` | INTEGER
`starttime` | TIMESTAMP
`stoptime` | TIMESTAMP
`drug_type` | VARCHAR(20) NOT NULL
`drug` | VARCHAR(255) NOT NULL
`formulary_drug_cd` | VARCHAR(50)
`gsn` | VARCHAR(10)
`ndc` | VARCHAR(20)
`prod_strength` | VARCHAR(255)
`form_rx` | VARCHAR(25)
`dose_val_rx` | VARCHAR(100)
`dose_unit_rx` | VARCHAR(50)
`form_val_disp` | VARCHAR(50)
`form_unit_disp` | VARCHAR(50)
`doses_per_24_hrs` | REAL
`route` | VARCHAR(50)

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

### `hadm_id`

{{% include "/static/include/hadm_id.md" %}}

### `pharmacy_id`

An identifier which links administrations in *emar* to pharmacy information in the *pharmacy* table.

### `starttime`, `stoptime`

The prescribed start and stop time for the medication.

### `drug_type`

The component of the prescription which the drug occupies. Can be one of 'MAIN', 'BASE', or 'ADDITIVE'.

### `drug`

A free-text description of the medication administered.

### `formulary_drug_cd`

A hospital specific ontology used to order drugs from the formulary.

### `gsn`

The Generic Sequence Number (GSN), a coded identifier used for medications.

### `ndc`

The National Drug Code (NDC), a coded identifier which uniquely identifiers medications.

### `prod_strength`

A free-text description of the composition of the prescribed medication (e.g. '12 mg / 0.8 mL Oral Syringe', '12.5mg Tablet', etc).

### `form_rx`

The container in which the formulary dose is delivered (e.g. 'TABLET', 'VIAL', etc).

### `dose_val_rx`

The prescribed dose for the patient intended to be administered over the given time period.

### `dose_unit_rx`

The unit of measurement for the dose.

### `form_val_disp`

The amount of the medication which is contained in a single formulary dose.

### `form_unit_disp`

The unit of measurement used for the formulary dosage.

### `doses_per_24_hrs`

The number of doses per 24 hours for which the medication is to be given. A daily dose would result in `doses_per_24_hrs`: 1, bidaily (BID) would be 2, and so on.

### `route`

The route of administration for the medication.