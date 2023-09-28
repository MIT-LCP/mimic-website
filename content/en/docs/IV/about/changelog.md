---
title: "MIMIC-IV Change log"
linktitle: "Change log"
date: 2020-08-10
weight: 40
description: >
  Changes between releases of MIMIC-IV.
---

The latest version of MIMIC-IV is v2.2.

This page lists changes implemented in sequential updates to the MIMIC-IV database. Issues are tracked using a unique issue number, usually of the form #100, #101, etc. Note that some of these issues are only accessible in a private 'building' repository.

### MIMIC-IV v2.2

MIMIC-IV v2.2 was released on January 6, 2023. It added provider identifiers, imputed `hadm_id` for a number of rows in _emar_, and changed the subset of `subject_id` which are held out. Final row counts are available in the validation scripts published with the [MIMIC Code Repository](https://github.com/MIT-LCP/mimic-code/). For clarity, after removal of the test set, the row counts are as follows:

*   _patients_: 299,712 (was 315,460 in v2.0)
*   _admissions_: 431,231 (was 454,324 in v2.0)
*   _icustays_: 73,181 (was 76,943 in v2.0)

#### icu module

*   _caregiver_
    *   New table in v2.2. Contains one column: `caregiver_id`, a deidentified integer which uniquely represents a single caregiver or provider. These identifiers are sourced from the MetaVision ICU system. When present in a table, it indicates the user who documented the data into MetaVision. For example, the `caregiver_id` associated with a row indicating mechanical ventilation in the procedureevents table represents the user who documented the event, and not the provider who performed the procedure.
*   _chartevents_, _datetimeevents_, _ingredientevents_, _inputevents_, _outputevents_, _procedureevents_
    * Added the `caregiver_id` column. This column is a deidentified integer representing the care provider who documented the data for the given row.

#### hosp module

*   _provider_
    *   New table in v2.2. Contains one column: `provider_id`, a deidentified string which uniquely represents a single caregiver or provider. These identifiers are sourced from the hospital wide EHR system, and used in a variety of contexts across tables in the module.
*   _admissions_
    *   New column: `admit_provider_id`, a deidentified string representing the provider who admitted the patient.
*   _emar_
    *   New column: `enter_provider_id`, a deidentified string representing the provider who entered the medication administration information into the database.
    *   Fixed a bug where a subset of _emar_ rows (713,117, ~2.5%) did not have an `hadm_id` even though they were associated with a given hospitalization. These rows occur outside of the administratively documented admission and discharge times for a hospitalization, but are still considered as administered during that hospitalization in the raw data.
*   _labevents_, _microbiologyevents_, _poe_, _prescriptions_
    *   New column: `order_provider_id`, a deidentified string representing the provider who ordered the corresponding event (e.g. the lab test in the case of _labevents_, or the medication in the case of _prescriptions_).

### MIMIC-IV v2.1

MIMIC-IV v2.1 was released on November 14, 2022. It removed a subset of subject_id which will be retained internally as a test set. Future data releases will exclude these patients.

#### Major changes

* A subset of patients were removed from the dataset. 15,748 subject_id were removed from the patients table. 23,093 hadm_id were removed from the admissions table. 3,762 stay_id were removed from the icustays table.

### MIMIC-IV v2.0

MIMIC-IV v2.0 was released on June 12, 2022. It focused on expanding the data elements available for patients within MIMIC-IV v1.0. Additional data available includes out-of-hospital date of death, information from the online medical record system (which includes height and weight), and more detail for continuous infusions in the ICU.

#### Major changes

*   The core module has been removed to simplify the schema. The _admissions_, _patients_, and _transfers_ tables are now in the hosp module.
*   Neonates have been removed from the dataset. Neonatal data will be released in a separate project with data from the neonatal intensive care unit.

#### icu module

*   _icustays_
    *   Around 700 stays (~1%) have changed due to the changes in the _patients_ table.
*   _chartevents, d\_items_
    *   The problem list from MetaVision has been added. All problems are documented with the same `itemid` now present in _d\_items_: 220001. There are just over 1,000 unique problems. Most documented problems are related to the care plan for the patient and documented during nurse shift changes (either 7am or 7pm). Less frequently, the ongoing issues are documented here.
*   _ingredientevents_
    *   This is a new table associated with _inputevents_. Each intravenous administration tracked in _inputevents_ is associated with a set of ingredients. These ingredients include water content, caloric information, and so on. The goal of the _inputevents_ table is to support nutrition research and to provide a mechanism for estimating fluid input via summing all instances of the water ingredient. These ingredients have been separated from the _inputevents_ table to simplify analysis and reduce the size of _inputevents_.
*   _inputevents_
    *   Removed a single column which contained only null values: `cancelreason`.
*   _procedureevents_
    *   Removed columns which contained only null values: `totalamount`, `totalamountuom`, `cancelreason`, `comments_editedby`, `comments_canceledby`, `comments_date`, `secondaryordercategoryname`.

#### hosp module

*   _admissions_
    *   Fixed an issue where hospitalizations were missing _edregtime_ and _edouttime_ when the patient was admitted via the ED (reported in [#1247](https://github.com/MIT-LCP/mimic-code/issues/1247), thanks [@MEladawi](https://github.com/MEladawi)).
*   _patients_
    *   `dod` is now populated with out-of-hospital mortality from state death records. For patients admitted to the ICU, this change has increased capture of date of death from 8,223 records to 23,844 (i.e. we now have out-of-hospital mortality for an additional 15,621 ICU patients).
    *   The mechanism for determining patients included in MIMIC was changed. For the most part this has resulted in an improvement, particularly regarding the logic for merging patients who had distinct medical record numbers. As a result of this change, most tables have had a change in the data content. Approximately 1% of stays were affected.
*   _transfers_
    *   Fixed a bug where the `outtime` for ED stays with no associated `hadm_id` (i.e. an ED stay where the individual was not admitted to the hospital) was incorrect. This resulted in all _transfers_ rows with a NULL `hadm_id` having an apparent stay of minutes or less. The `outtime` column has now been corrected.
*   _labevents, d\_labitems_
    *   The `itemid` for _d\_labitems_ has been changed for 43 items. These are extremely infrequently documented and each `itemid` has fewer than 100 observations in _labevents_. The exact `itemid` are provided in the changelog file CHANGELOG.txt.
    *   Errors were found in the current values of `loinc_code` (reported in [#938](https://github.com/MIT-LCP/mimic-code/issues/938), thanks [@Mauvila](https://github.com/Mauvila)). In order to enable collaborative improvement, the `loinc_code` column has been removed, and will now be collaboratively developed in the [MIMIC Code Repository](https://github.com/MIT-LCP/mimic-code/). Initial values will be sourced from the hospital system.
    *   A number of labs which previously had the value in the comments field now have the value in the value field (reported in [#941](https://github.com/MIT-LCP/mimic-code/issues/941), thanks [@Mauvila](https://github.com/Mauvila)). This change makes the _labevents_ table more consistent with MIMIC-III, which had these values in the value field.
*   _microbiologyevents_
    *   New organisms, tests, specimens, and antibiotics have been added.
*   _omr_
    *   A new table has been added: _omr._ The source of this data is the Online Medical Record, and it contains miscellaneous information useful for understanding an individual's health. As of v2.0, the _omr_ table has the following information: blood pressure, height, weight, body mass index, and Estimated Glomerular Filtration Rate (eGFR). These values are available from both inpatient and outpatient visits, and in many cases a "baseline" value from before a patient's hospitalization is available.
*   _prescriptions_
    *   The `formulary_drug_cd` table has been added back (was previously in MIMIC-III). This column has the same set of values as the `product_code` column of emar\_detail.

### MIMIC-IV v1.0

MIMIC-IV v1.0 was released March 16th, 2021.

#### core

* *admissions*
    * A number (~1000, <1%) of erroneous `hadm_id` have been removed.
* *patients*
    * 942 `subject_id` have been removed as they were only associated with the above erroneous `hadm_id`.
    * `dod` is now populated using the patient's `deathtime` from their latest hospitalization (reported in [#71](https://github.com/MIT-LCP/mimic-iv/issues/71), thanks [@jinjinzhou](https://github.com/jinjinzhou)).
    * At the moment, out-of-hospital mortality is **not** captured by `dod`
* *transfers*
    * Removed erroneous transfers included in the previous version.
    * `transfer_id` has been regenerated. `transfer_id` in MIMIC-IV v1.0 are **not compatible** with `transfer_id` from v0.4. We do not intend to change `transfer_id` when updating MIMIC-IV, but had to update it due to an error in its generation.
    * All `hadm_id` in transfers are also present in *admissions* and vice-versa (reported in [#84](https://github.com/MIT-LCP/mimic-iv/issues/84), thanks [@kokoko12305](https://github.com/kokoko12305)).

#### icu

* *icustays*
    * ICU stays were inappropriately assigned in the previous version due to an error in the preprocessing code. Previously, non-ICU ward transfers were included in the ICU stays, and certain ward stays were not treated as ICU stays (reported in [#67](https://github.com/MIT-LCP/mimic-iv/issues/67), thanks [@JHLiu7](https://github.com/JHLiu7) and [@stefanhgm](https://github.com/stefanhgm)). The assignment of `stay_id` has been regenerated.
    * The mapping between hospital transfers and ICU stays has been updated.
    * `stay_id` in MIMIC-IV v1.0 are **not compatible** with `stay_id` from v0.4. We do not intend to change `stay_id` when updating MIMIC-IV, but had to update it due to an error in its generation.
* The change in *icustays* has re-assigned values to new `stay_id`, as a result all tables have had their content changed (due to a change in `stay_id`), but the structure is unchanged.

#### hosp

* *hcpcsevents*
    * Data has been added for a number of previously excluded hospitalizations.
    * The table now has a `chartdate` column, containing the date associated with the code. Every row is associated with a date.
* *drgcodes*
    * Data has been added for a number of previously excluded hospitalizations.
    * Duplicate DRG codes have been removed from the table.
    * Descriptions have been updated using the latest dictionaries made available from [the Massachusetts government website](https://www.mass.gov/service-details/special-notices-for-acute-hospitals) and [HCUP](https://www.hcup-us.ahrq.gov/db/state/siddbdocumentation.jsp).
* *diagnoses_icd*, *d_icd_diagnoses*
    * Data has been added for a number of previously excluded hospitalizations (reported in [#27](https://github.com/MIT-LCP/mimic-iv/issues/27), thanks [@yugangjia](https://github.com/yugangjia)).
    * The icd_code column is now trimmed and stored as a VARCHAR, i.e. codes no longer contain trailing whitespaces (`850 ` -> `850`).
    * Missing ICD codes have been added to the dictionary. All ICD codes in the diagnoses_icd table have an associated reference in *d_icd_diagnoses*.
* *labevents*
    * The `comments` field has been updated, fixing a bug where comments longer than 4096 characters were truncated. Due to the deidentification, it's unlikely users will see much difference, as these comments will appear as `___`.
* *procedures_icd*
    * Data has been added to *procedures_icd* for a number of previously excluded hospitalizations.
    * The table now has a chartdate column, containing the date associated with each billed procedure.
    * The icd_code column is now trimmed and stored as a VARCHAR, i.e. codes no longer contain trailing whitespaces (`850 ` -> `850`).
    * Missing ICD codes have been added to the dictionary. All ICD codes in the *procedures_icd* table have an associated reference in *d_icd_procedures*.

### MIMIC-IV v0.4

MIMIC-IV v0.4 was released August 13th, 2020.

- *d_micro*
    - This table has been removed
- *microbiologyevents*
    - Added the `spec_type_desc`, `test_name`, `org_name`, and `ab_name` columns
        - These columns contain the textual name of the organism/antibiotic/test/specimen
    - Added the `comments` column
        - this column contains information about the test, and in some cases (e.g. viral load tests), contains the result
    - `micro_specimen_id` has been regenerated; the values will not match previous versions.

### MIMIC-IV v0.3

MIMIC-IV v0.3 was released July 13th, 2020. 

- Fixed an alignment issue in shifted dates/times

### MIMIC-IV v0.2

MIMIC-IV v0.2 was released June 23rd, 2020.

- Updated demographics in the patient table
  - `anchor_year` -> `anchor_year_group`
  - `anchor_year_shifted` -> `anchor_year`
  - See the [patients table](/docs/iv/modules/core/patients) for detail on these columns
- *transfers*
  - Deleted the `los` column
- *emar*
  - `mar_id` -> `emar_id`
    - `emar_id` is now a composite of `subject_id` and `emar_seq`, and has form "subject_id-emar_seq"
  - `emar_seq` column - a monotonically increasing integer starting with the first eMAR administration
  - Added `poe_id` and `pharmacy_id` columns for linking to those tables
- *emar_detail*
  - `mar_id` -> `emar_id` (changed as above)
  - Deleted the `mar_detail_id` column
- *hcpcsevents*
  - `ticket_id_seq` -> `seq_num`
- *labevents*
  - Many previously NULL values are now populated - these were removed originally due to deidentification
  - Added the `comments` column. This contains deidentified free-text comments with labs. PHI is replaced with three underscores (`___`). If an entire comment is `___`, then the entire comment was scrubbed.
  - `spec_id` -> `specimen_id`
- *microbiologyevents*
  - `stay_id` column removed
  - `spec_id` -> `micro_specimen_id`
- Added the [*poe*](/docs/iv/modules/hosp/poe) and [*poe_detail*](/docs/iv/modules/hosp/poe_detail) tables
  - Documentation of provider orders for various treatments and other aspects of patient management
- Added the [*prescriptions*](/docs/iv/modules/hosp/prescriptions) table
  - Documentation of medicine prescriptions via the provider order interface
- Added the [*pharmacy*](/docs/iv/modules/hosp/pharmacy) table
  - Detailed information regarding prescriptions provided by the pharmacy including formulary dose, route, frequency, dose, and so on.
- *inputevents*
  - Fixed an error in the calculation of the *amount* column
- *icustays*
  - Re-derived `stay_id` - the new `stay_id` are distinct from the previous version.
- *diagnosis*
  - Added diagnosis table with similar schema as the *diagnosis_icd* table.
- *main*
  - Removed diagnosis columns from this table (inserted into *diagnosis* above)

### MIMIC-IV v0.1

MIMIC-IV v0.1 was released on 15 August 2019.
