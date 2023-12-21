---
title: "ECG"
linkTitle: "ECG"
date: 2023-10-02
weight: 60
description: >
  The ECG module provides waveform data, and lookup tables which can be used to link subjects to other MIMIC-IV modules via `subject_id`. A `study_id` allows for linking within the ECG module while `note_id` allows linking to the cardiologist note in the MIMIC-IV-Note module.   
---

The MIMIC-IV-ECG module contains approximately 800,000 diagnostic electrocardiograms across nearly 160,000 unique patients. 

There are three lookup tables in this module:
- A records file, `record-list.csv`, provides a mapping between the study (`study_id`), the path to the diagnostic ECG waveform (`path`), and the patient (`subject_id`).
- A machine measurements file, `machine_measurements.csv`, provides the information generated from the ECG machine including global (across all 12 leads) summary measurements (RR interval, QRS onset, etc.), the machine generated report, as well as machine and cart information. It also provides a study (`study_id`) and patient (`subject_id`) identifier.
- A note linking file, `waveform_note_links.csv`, provides a `note_id` for each waveform that has an available free-text cardiologist note in the MIMIC-IV-Note module. It also provides a study (`study_id`) and patient (`subject_id`) identifier.

Additional details for each lookup table are provided in the pages below.

{{% pageinfo %}}
Please note that the free-text cardiologist notes for the ECG module will be publicly released in the MIMIC-IV-Note module at a later date.
{{% /pageinfo %}}

**For additional information about this project please see the MIMIC-IV-ECG project on physionet.org.**
