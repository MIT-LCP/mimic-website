---
title: "What's new in MIMIC-IV?"
linktitle: "What's new?"
date: 2020-08-10
weight: 20
description: >
  Changes from MIMIC-III to MIMIC-IV.
---

Many users will be familiar with [MIMIC-III](/docs/iii), the predecessor of MIMIC-IV.
A number of improvements have been made, including simplifying the structure, adding new data elements, and improving the usability of previous data elements.

## Structure

The structure of MIMIC-IV is necessarily different than MIMIC-III.
In MIMIC-III, the set of tables were given as one large set, with no obvious differentiation between them.
In MIMIC-IV, we explicitly state the source database of each table.
Not only does this clarify the data provenance, but it answers many questions regarding data coverage.
For example, as the CHARTEVENTS table is sourced from the ICU clinical information system, it will only provide data for patients while they are in an ICU.
Conversely, the LABEVENTS table is sourced from the hospital database, and consequently contains information for a patient's entire hospital stay.

Table-wise changes are summarized below.

MIMIC-III table | MIMIC-IV module | Removed columns | Additional columns | Notes
--- | --- | --- | --- | ---
patients            | core | row_id, dob, dod_ssn, dod_hosp, expire_flag | anchor_age, anchor_year, anchor_year_group | DOD no longer available outside of the hospital.
admissions          | core | row_id, religion, has_chartevents_data | | Values changed for many columns (e.g. language, ethnicity).
transfers           | core | row_id, icustay_id, dbsource, prev_careunit, curr_careunit, prev_wardid, curr_wardid, los | transfer_id, careunit | Schema is simplified in MIMIC-IV.
d_hcpcs             | hosp | N/A, was d_cpt | | New table.
d_icd_diagnoses     | hosp | row_id, icd9_code, short_title | icd_code, icd_version | Now contains ICD-9 and ICD-10 codes.
d_icd_procedures    | hosp | row_id, icd9_code, short_title | icd_code, icd_version | Now contains ICD-9 and ICD-10 codes.
d_labitems          | hosp | row_id | | Many additional itemid added.
diagnoses_icd       | hosp | row_id, icd9_code | icd_code, icd_version | Now contains ICD-9 and ICD-10 codes.
drgcodes            | hosp | row_id | | 
emar                | hosp | N/A, new table. | |
emar_detail         | hosp | N/A, new table. | |
hcpcsevents         | hosp | N/A, was cptevents. | |
labevents           | hosp | row_id | labevent_id, specimen_id, storetime, ref_range_lower, ref_range_upper, priority, comments
microbiologyevents  | hosp | row_id | microevent_id, micro_specimen_id, test_seq, storedate, storetime, test_itemid, test_name, quantity, comments
pharmacy            | hosp | N/A, new table. | |
poe                 | hosp | N/A, new table. | |
poe_detail          | hosp | N/A, new table. | |
prescriptions       | hosp | row_id, startdate, enddate, drug_name_poe, drug_name_generic, formulary_drug_cd | starttime, stoptime, form_rx, doses_per_24_hrs |
procedures_icd      | hosp | row_id, icd9_code | icd_code, icd_version | Now contains ICD-9 and ICD-10 codes.
services            | hosp | row_id | |
d_items             | icu  | row_id, dbsource, conceptid | lownormalvalue, highnormalvalue
chartevents         | icu  | row_id, icustay_id, cgid, error, resultstatus, stopped | stay_id
datetimeevents      | icu  | row_id, icustay_id, cgid, error, resultstatus, stopped | stay_id
icustays            | icu  | row_id, icustay_id | stay_id
inputevents         | icu  | row_id, icustay_id, cgid, error | stay_id | Was inputevents_mv in MIMIC-III.
outputevents        | icu  | row_id, icustay_id, cgid, error | stay_id |
procedureevents     | icu  | row_id, icustay_id, cgid, comments_editedby, comments_canceledby | stay_id, patientweight, totalamount, totalamountuom, originalamount, originalrate |

## Contemporary

MIMIC-IV contains data from 2008 - 2019 (inclusive).
Biomarkers which have been more recently introduced will be available.

## CareVue is no more

As the update covers the years 2008 - 2019, the CareVue clinical information system is no longer relevant, as it was not used during that time period. The implications are:

* All `itemid` in d_items with a value less than 220000 are no longer relevant.
* The *inputevents_cv* table has been removed. The *inputevents_mv* table was renamed *inputevents*. The structure is otherwise unchanged.
* The *procedureevents_mv* table has been renamed *procedureevents*.

## `icustay_id` is now `stay_id`

Eventually, stays across different areas of the hospital will be indexed by a unique `stay_id`, such that a stay in the emergency department, ICU, and operating room will all be distinct and referred to by the same identifier. In preparation for this change, `icustay_id` has been renamed `stay_id`.

## Years are included

The date-shift strategy in MIMIC has changed.
Instead of releasing the day of the week and the season, we have released the approximate year of patient admission.
This allows studying patients over time as care practices change.

## Audit trails are removed

MIMIC-III contained a number of rows associated with auditing clinical documentation. These rows were marked as erroneous in various ways (`error` = 1, `statusdescription` = 'Rewritten'). These rows have been removed in MIMIC-IV.

<!-- 
### ED data

Completely new to MIMIC is the inclusion of data from the emergency department (MIMIC-ED).
This data covers over 200,000 patients and provides crucial information about the initial period of their hospital stay. The ED section describes the tables in MIMIC-ED. Approximately 65% of patients admitted to an ICU at the BIDMC are first seen in the emergency department.

-->

## Chest x-ray data

Imaging data is also an entirely new addition to MIMIC. The MIMIC-CXR database is [publicly available](https://physionet.org/content/mimic-cxr/). Notably, the `subject_id` identifier used in the MIMIC-CXR database is consistent with the `subject_id` used in MIMIC-IV. Therefore, all chest x-rays in MIMIC-CXR are linkable to patient stays in MIMIC-IV.

## Table-wise improvements over MIMIC-III

A number of enhancements have been made to tables which may be familiar to you from MIMIC-III.
Entirely new tables have also been added.

### Hospital data

#### *emar* and *emar_detail*

Two entirely new tables are made available, sourced from the relatively newly installed electronic Medicine Administration Record (eMAR) system.
Bedside staff will scan barcodes for each individual formulary unit of a medication when administering it. This allows for a granular, high resolution record of when a medication was given.

#### *labevents*

* Reference ranges are now available.
* A specimen identifier (`specimen_id`) allows users to group all measurements made for a single specimen (e.g. all blood gas measurements from the same sample of blood).
* A priority column indicates the priority level of the laboratory measure.

#### *microbiologyevents*

* Now contains the name of the test performed.

#### *prescriptions*

* Instead of `startdate` and `enddate`, *prescriptions* now has `starttime` and `stoptime`.
  * This means all prescriptions now have the date **and** time of start/stop
  * In an internal assessment, only 10 prescriptions were missing the start hour, and 1650 prescriptions were missing the stop hour (there are over 17 million rows in this table).
  * We cannot guarantee the start time is the first instance of patient administration (as these are *prescriptions*), but the added resolution should help in research studies.
* `drug_name_generic`, `drug_name_poe`, and `formulary_drug_cd` have been removed.
  * `drug_name_poe`, when not null, was always equal to `drug`.
  * `drug` is the displayed drug name in the EHR, and is more reliable than `drug_name_generic`.
  * `formulary_drug_cd` was an internal ontology that did not provide additional information over `drug`.
* New columns!
  * `pharmacy_id` - to link to the *pharmacy* table which has additional information about the prescription
  * `form_rx`.
  * `doses_per_24_hrs` provides the number of doses per 24 hours prescribed by this row.

<!-- 
### ICU data

#### INPUTEVENTS

* Ingredients are now stored in the data. Importantly, "water" is an ingredient in most inputs, and tabulating the amount of water a patient receives allows accurate estimation of the patient's fluid intake.

-->
