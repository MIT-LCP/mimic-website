---
title: "ECG Record Table"
linktitle: "record_list"
date: 2023-10-02
weight: 10
description: >
  The table which lists all available records in this module.
---

This table lists all records in the MIMIC-IV-ECG module.
Each diagnostic ECG study has a waveform file (in WFDB format) and is assigned a unique `study_id`.
This table contains the path (`path`) to the waveform file. The `study_id` can be used to link to the machine measurement and note information in the other lookup tables.

# Important considerations

- Diagnostic ECGs are available for patients from the MIMIC-IV Clinical Database. These ECGs were collected between 2008 - 2019 but have been date shifted (for de-identification) per the convention across MIMIC.
- For a given subject, all available diagnostic ECGs (inpatient and outpatient) were pulled. Therefore, a large number of the waveforms will overlap with visits in the Clinical Database but some will not.

# Table columns

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `study_id`

A unique identifier for the diagnostic ECG study.  

## `file_name`

The name of the `.hea` and `.dat` WFDB files for a given study. 

## `ecg_time`

The time that the diagnostic ECG was collected.

## `path`

The path to the waveform file.