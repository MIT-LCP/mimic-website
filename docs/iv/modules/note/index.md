---
title: Note
layout: default
nav_order: 80
description: The Note module contains deidentified free-text clinical notes for hospitalized
  patients, including discharge summaries and radiology reports.
has_children: true
parent: MIMIC-IV
---


The Note module (MIMIC-IV-Note) contains deidentified free-text clinical notes for hospitalized patients. As of MIMIC-IV-Note v2.2, the module includes notes from the hospital wide EHR. The module contains:

- **discharge** - Discharge summaries
- **discharge_detail** - Information related to discharge summaries
- **radiology** - Radiology reports
- **radiology_detail** - Information related to radiology reports

All notes have been deidentified to protect patient privacy while preserving clinical content for research. Deidentified entities are replaced with three underscores (`___`).

The Note module is published separately on PhysioNet: [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/). It can be linked to the rest of MIMIC-IV via `subject_id` and `hadm_id`.
