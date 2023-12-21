---
title: "Waveform Note Links Table"
linktitle: "waveform_note_links"
date: 2023-10-02
weight: 30
description: >
  A table which provides links between waveforms and available cardiologist notes.
---

{{% pageinfo %}}
Please note that the free-text cardiologist notes for the ECG module will be publicly released in the MIMIC-IV-Note module at a later date.
{{% /pageinfo %}}

This table provides links to the cardiologist's note, when available, for a given diagnostic ECG waveform.
Each diagnostic ECG study has a waveform file (in WFDB format) and is assigned a unique `study_id`. Not all waveforms get read by a cardiologist.  This is the primary reason that there are fewer notes than waveforms.
This table provides the link between the path to a given waveform (`waveform_path`) and the note identifer (`note_id`). The `study_id` can be used to link to the record list and machine measurement information in the other lookup tables.

# Table columns

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `study_id`

A unique identifier for the diagnostic ECG study.  

## `waveform_path`

The path to the diagnostic ECG waveform. 

## `note_id`

The unique identifier for the note that is associated with a given ECG study. This identifier can be used to link to the free-text cardiologist ECG note in the MIMIC-IV-Note module.

## `note_seq`

A monotonically increasing integer which chronologically sorts the notes. That is, notes can be ordered sequentially by note_seq.

## `charttime`
The time at which the note was charted - this is usually the most relevant time for interpreting the content of the note, but it is not necessarily when the note was fully written.



