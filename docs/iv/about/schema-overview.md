---
title: Schema overview
layout: default
nav_order: 20
parent: About MIMIC-IV
grand_parent: MIMIC-IV
description: An overview of the modular structure of MIMIC-IV, including the identifier system, module characteristics, and patterns for cross-module analysis.
---

# MIMIC-IV schema overview
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

Understanding the overall structure and organization of the MIMIC-IV database is crucial for effective analysis.

## Modular design

MIMIC-IV uses a modular design. The hospital (`hosp`) module contains data acquired from the hospital wide electronic health record. The ICU (`icu`) module contains data from the clinical information system used within the ICU. Additional modules (ED, CXR, ECG, Note) extend MIMIC-IV with data from other systems.

## Core identifier system

The database uses a hierarchical identifier system:

### Patient level
{% include subject_id.md %}

### Hospital admission level
{% include hadm_id.md %}

### Unit stay level
{% include stay_id.md %}

## Data flow through the hospital

Understanding how patients move through the hospital helps in understanding the data:

1. **Patient arrives** → `subject_id` assigned
2. **Hospital admission** → `hadm_id` assigned
3. **Unit transfer** → `stay_id` assigned (ICU, ED, etc.)
4. **Data collection** → Events recorded with appropriate IDs

## Module characteristics

### Hospital (hosp) module
- **Purpose**: Hospital-wide EHR data
- **Key tables**: `patients`, `admissions`, `transfers`, `labevents`, `prescriptions`, `diagnoses_icd`
- **Coverage**: All hospital patients
- **Granularity**: Order/event-level

### ICU module
- **Purpose**: Intensive care monitoring
- **Key tables**: `chartevents`, `inputevents`, `outputevents`, `procedureevents`
- **Coverage**: ICU patients only
- **Granularity**: Hour-to-hour or more frequent

### Emergency department (ED) module
- **Purpose**: Emergency department care
- **Key tables**: `edstays`, `triage`, `vitalsign`, `medrecon`, `pyxis`, `diagnosis`
- **Coverage**: ED patients only
- **Granularity**: Visit-level and event-level

### Note module
- **Purpose**: De-identified free-text clinical notes
- **Key tables**: `discharge`, `radiology` (and their detail tables)
- **Coverage**: Subset of hospitalized patients
- **Granularity**: Note-level

### CXR module
- **Purpose**: Chest x-ray images and reports linked to MIMIC-IV
- **Key tables**: lookup tables linking `subject_id` to `study_id` and `dicom_id`
- **Coverage**: ED patients with chest radiographs
- **Granularity**: Study- and image-level

### ECG module
- **Purpose**: Diagnostic 12-lead ECG waveforms and machine measurements
- **Key tables**: `record_list`, `machine_measurements`, `waveform_note_links`
- **Coverage**: Subset of patients with ECG recordings
- **Granularity**: Study-level

## Data relationships

### One-to-many relationships
- One patient → Many admissions
- One admission → Many diagnoses
- One admission → Many lab results
- One ICU stay → Many vital sign measurements

### Cross-module linking
Patients can be followed across modules using identifiers:

```sql
-- Link patient demographics to ICU data
SELECT p.gender, c.valuenum AS heart_rate
FROM `physionet-data.mimiciv_hosp.patients` p
JOIN `physionet-data.mimiciv_hosp.admissions` a ON p.subject_id = a.subject_id
JOIN `physionet-data.mimiciv_icu.icustays` i ON a.hadm_id = i.hadm_id
JOIN `physionet-data.mimiciv_icu.chartevents` c ON i.stay_id = c.stay_id
WHERE c.itemid = 220045  -- Heart rate
```

## Temporal considerations

### Time precision
- **Hosp**: Usually day or hour precision
- **ICU**: Minute-level precision common
- **ED**: Varies by event type

For more on how time is represented in MIMIC-IV, including `charttime` vs. `storetime` and date shifting, see the [Core concepts](/docs/iv/about/concepts/) page.

## Common analysis patterns

### Patient cohort selection
1. Start with the `patients` table for demographics
2. Join to `admissions` for admission criteria
3. Add module-specific criteria as needed

### Longitudinal analysis
1. Identify patient population
2. Extract events from relevant modules
3. Align timestamps for temporal analysis

### Outcome assessment
1. Define outcome from appropriate module
2. Link back to patient characteristics
3. Account for censoring and follow-up

## Best practices

### Query design
- Always include appropriate time filters
- Be mindful of data volume in the ICU module
- Use indexed columns for joins when possible

### Data validation
- Check for reasonable value ranges
- Validate identifier linkages
- Account for missing data patterns

---

{: .note }
> This schema overview provides the foundation for understanding MIMIC-IV. Each module has its own detailed documentation with table-specific information.
