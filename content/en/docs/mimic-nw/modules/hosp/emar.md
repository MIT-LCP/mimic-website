---
title: "emar"
linktitle: "emar"
weight: 8
date: 2023-09-18
description: >
  The Electronic Medicine Administration Record (eMAR); barcode scanning of medications at the time of administration.
---

## *emar*

The EMAR table is used to record administrations of a given medicine to an individual patient.
Records in this table are populated by bedside nursing staff scanning barcodes associated with the medicine and the patient.

## Links to

* *prescriptions* on `pharmacy_id`

## Important considerations

* In the clinical process, a doctor prescribes the medication, a pharmacist fills the prescription, and a nurse administers it through the electronic Medication Administration Record (eMAR). Therefore, it is important to note that not all 'eMAR pharmacy_id’ entries should necessarily appear in the prescription table.
* It's possible for discrepancies to occur in the transition from left to right in this process, where a wrong prescription might be detected and corrected by the pharmacist before the medication is filled.
* Similarly, many prescriptions don’t have a corresponding eMAR entry, usually because the prescription is intended for outpatient use following discharge.
* It is typical for one prescription to have multiple eMAR entries; for example, a medication order “BID for 7 days” would be expected to have 14 eMAR entries.

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER
`emar_id` | VARCHAR(25) NOT NULL
`emar_seq` | INTEGER NOT NULL
`pharmacy_id` | INTEGER
`charttime` | TIMESTAMP NOT NULL
`medication` | TEXT
`event_txt` | VARCHAR(100)
`scheduletime` | TIMESTAMP
`storetime` | TIMESTAMP NOT NULL

### `subject_id`

`subject_id` is unique identifier for each patient. `subject_id` is unique to each row and can be used to identify data associated with a specific patient. It is a cryptographic random number and each patient has a `subject_id` which is consistent across tables.

### `hadm_id`

Each row of this table contains a unique `hadm_id`, which represents a single patient's admission to the hospital. It is possible for this table to have duplicate `subject_id`, indicating that a single patient had multiple admissions to the hospital. The ADMISSIONS table can be linked to the PATIENTS table using `subject_id`.

### `emar_id`, `emar_seq`

Identifiers for the eMAR table. `emar_id` is a unique identifier for each order made in eMAR. `emar_seq` is a consecutive integer which numbers eMAR orders chronologically. `emar_id` is composed of `subject_id` and `emar_seq` in the following pattern: '`subject_id`-`emar_seq`'.

### `charttime`

The date and time at which the medication was administered.

### `medication`

The name of the medication which was administered.

### `event_txt`

Information about the administration. Most frequently `event_txt` is 'Administered', but other possible values are 'Applied', 'Confirmed', 'Delayed', 'Not Given', and so on. The  binary flags to denote adminstered and non-administered prescriptions will be released.
 

### `scheduletime`

If present, the time at which the administration was scheduled.

### `storetime`

The time at which the administration was documented in the eMAR table.
