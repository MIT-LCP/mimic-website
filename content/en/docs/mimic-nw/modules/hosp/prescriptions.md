---
title: "prescriptions"
linktitle: "prescriptions"
weight: 7
date: 2023-09-18
description: >
  Prescribed medications.
---

The *prescriptions* table provides information about prescribed medications. Information includes the name of the drug, coded identifiers including the Generic Sequence Number (GSN) and National Drug Code (NDC), the product strength, the formulary dose, and the route of administration.

To facilitate further federation processes, the drug mappings to standard terminologies (RxNorm) will be released.

We provide a list of some common COVID-19 drugs in the database, as defined by RxNorm terminology, below:

- SARS-COV-2 (COVID-19) vaccine, vector - Ad26 100000000000 UNT/ML Injectable Suspension	
- remdesivir 100 MG Injection [Veklury]	
- 20 ML remdesivir 5 MG/ML Injection [Veklury]	
- SARS-CoV-2 (COVID-19) vaccine, mRNA-BNT162b2 0.1 MG/ML Injectable Suspension	
- SARS-CoV-2 (COVID-19) vaccine, mRNA-1273 0.2 MG/ML Injectable Suspension	


## Links to

* *emar* on `pharmacy_id`

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER NOT NULL
`pharmacy_id` | INTEGER NOT NULL
`starttime` | TIMESTAMP(3)
`stoptime` | TIMESTAMP(3)
`drug_type` | VARCHAR(20) NOT NULL
`drug` | VARCHAR(255) NOT NULL
`gsn` | VARCHAR(255)
`ndc` | VARCHAR(25)
`prod_strength` | VARCHAR(255)
`form_rx` | VARCHAR(25)
`dose_val_rx` | VARCHAR(100)
`dose_unit_rx` | VARCHAR(50)
`form_val_disp` | VARCHAR(50)
`form_unit_disp` | VARCHAR(50)
`doses_per_24_hrs` | REAL
`route` | VARCHAR(50)

<!-- `poe_id` | VARCHAR(25) -->
<!-- `poe_seq` | INTEGER --> 
<!-- `formulary_drug_cd` | VARCHAR(50) -->

### `subject_id`

`subject_id` is unique identifier for each patient. `subject_id` is unique to each row and can be used to identify data associated with a specific patient. It is a cryptographic random number and each patient has a `subject_id` which is consistent across tables.

### `hadm_id`

Each row of this table contains a unique `hadm_id`, which represents a single patient's admission to the hospital. It is possible for this table to have duplicate `subject_id`, indicating that a single patient had multiple admissions to the hospital. The *admissions* table can be linked to the *patients* table using `subject_id`.

### `pharmacy_id`

An identifier which links administrations in *emar* to prescription information in the *prescription* table.

### `starttime`, `stoptime`

The prescribed start and stop time for the medication. `stop_time` could refer to an order to stop a prescription, but in this case, it means the end date for the prescription. For example, in a prescription for one dose per day for 14 days, the `stop_time` would be 14 days after the `start_time`.

### `drug_type`

The component of the prescription which the drug occupies. Can be one of 'MAIN', 'BASE', or 'ADDITIVE'.

### `drug`

A free-text description of the medication administered. Often includes the dose and form.

### `gsn`

The Generic Sequence Number (GSN), a coded identifier used for medications.

### `ndc`

The National Drug Code (NDC), a coded identifier which uniquely identifiers medications. 

### `prod_strength`

A free-text description of the composition of the prescribed medication (e.g. '12 mg / 0.8 mL Oral Syringe', '12.5mg Tablet', etc).

### `form_rx`

The container in which the formulary dose is delivered (e.g. 'TABLET', 'VIAL','Solution', 'Syringe', 'Piggyback', 'Capsule', 'Suspension', etc).

### `dose_val_rx`

The prescribed dose for the patient intended to be administered over the given time period.

### `dose_unit_rx`

The unit of measurement for the dose.

### `form_val_disp`

The amount of the medication which is contained in a single formulary dose. 

### `form_unit_disp`

The unit of measurement used for the formulary dosage. Examples include 'mg', 'Units', 'mL', 'mEq', 'tablet', 'mcg/min', 'mcg/kg/hr', etc.


### `doses_per_24_hrs`

The number of doses per 24 hours for which the medication is to be given. A daily dose would result in `doses_per_24_hrs`: 1, bidaily (BID) or twice a day would be 2, and so on. Within NMHC, if the medication order couldn’t be converted to `doses_per_24_hrs` (such as 'Once', 'PRN', 'Continuous', 'Weekly', or 'Q 90 days') the value would be missing.

### `route`

The route of administration for the medication, such as 'Oral', 'Intravenous', 'Injection', 'Subcutaneous', 'Inhalation', 'Topical', etc. May be missing.
