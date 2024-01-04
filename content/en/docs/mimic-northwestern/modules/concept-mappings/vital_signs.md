---
title: "vital signs"
linktitle: "vital signs"
weight: 3
date: 2023-09-18
description: >
  Numeric vital sign concept mappings within general, routine, respiratory, and hemodynamic categories.
---

Vital signs data in MIMIC-Northwestern is split between two tables in the ICU module, the d_items and chartevents. The d_items table is the definition table for all concepts recorded in the events tables in the ICU module, including the chartevents table, and the chartevents table contains all the charted data available for a patient during their ICU stay, including vital signs readings. 

Data from the d_items table is used for mapping vital signs values to Logical Observation Identifiers Names and Codes (LOINC), including the label and the unit of measurement. Vital signs with numeric parameter types that are stratified into four categories including 'General', 'Routine Vital Signs', 'Respiratory' and 'Hemodynamics' are included in the mappings. Similar to lab results, the online tool [SearchLOINC](https://loinc.org/search/) is used to map vital signs to Logical Observation Identifiers Names and Codes (LOINC) v2.72 and the [OHDSI Athena code dictionary](https://athena.ohdsi.org/) for Observational Medical Outcomes Partnership (OMOP) codes. 

Two concepts in MIMIC under the 'Routine Vital Signs' category are not mapped because no suitable LOINC code exists for these concepts. These concepts account for around 0.02% of total vital signs events in MIMIC. The rest of the concepts have an exact match.

Examples of MIMIC vital signs that were unmapped:

| Vital sign name | Mapping challenge | Comments |
|-----------------|---------------|----------|
| Bladder Pressure | No LOINC code available | Bladder pressure is a technique used to monitor intra-abdominal pressure. |
| Doppler BP | No LOINC code available | Doppler is sometimes used in the process of measuring systolic blood pressure if the pulse is faint. |

## Important considerations

* Northwestern mappings contain most of the clinically relevant concepts in MIMIC. Body mass index, 'BMI' is an additional item sourced from the Northwestern data warehouse.

## Table columns

| Name            | Postgres data type  |
| --------------- | ------------------- |
| `itemid`        | INTEGER             |
| `label`         | VARCHAR(200)        |
| `abbreviation`  | VARCHAR(100)        |
| `category`      | VARCHAR(100)        |
| `unitname`      | VARCHAR(100)        |
| `loinc`         | VARCHAR(50)         |
| `loinc_label`   | VARCHAR(200)        |
| `omop_id`       | VARCHAR(50)         |
| `author_id`     | VARCHAR(50)         |
| `reviewer_id`   | VARCHAR(50)         |

## Detailed description

### `itemid`
A unique identifier for a single measurement type in the database.
###  `label`
`label` describes the inhouse concept which is represented by the itemid from BIDMC or Northwestern.
### `abbreviation`
`abbreviation` lists a common abbreviation for the label harmonized to MIMIC's abbreviations via LOINC codes.
### `category`
`category` provides some information on the type of data the itemid corresponds harmonized to MIMIC's categories via LOINC codes.
### `unitname`
`unitname` specifies the unit of measurement used for the itemid harmonized to MIMIC's unitnames via LOINC codes.
### `loinc`
`loinc` contains the LOINC code associated with the given itemid. 
### `loinc_label`
`loinc_label` contains the LOINC Long Common Name for the loinc code.
### `omop_id`
`omop_id` is a unique identifier for each Concept across all domains in the OMOP common data model.
### `author_id`
ORCIDs that identifies the persons or groups responsible for asserting the mappings.
### `reviewer_id`
ORCIDs that identifies the persons or groups that reviewed and confirmed the mappings.
