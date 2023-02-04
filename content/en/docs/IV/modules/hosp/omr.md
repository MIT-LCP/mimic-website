---
title: "omr table"
linktitle: "omr"
date: 2023-02-03
weight: 1
description: >
  The Online Medical Record (OMR) table contains miscellaneous information from the EHR.
---

## *omr*

The Online Medical Record (OMR) table stores miscellaneous information documented in the electronic health record.
It is a useful source of outpatient measurements such as blood pressure, weight, height, and body mass index.

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`chartdate` | DATE NOT NULL
`seq_num` | INTEGER NOT NULL
`result_name` | VARCHAR(100) NOT NULL
`result_value` | TEXT NOT NULL

## Detailed Description

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

## `chartdate`

The date on which the observation was recorded.

## `seq_num`

An monotonically increasing integer which uniquely distinguishes results of the same type recorded on the same day.
For example, if two blood pressure measurements occur on the same day, `seq_num` orders them chronologically.

## `result_name`

Each row provides detail regarding a single observation in the EHR.  `result_name` provides a human interpretable description of the observation. As of MIMIC-IV v2.2, the following table lists the number of observations and the most common value.

result_name | number of observations | example value
--- | --- | ---
eGFR | 240 | >60
Blood Pressure Lying | 2764 | 120/70
Blood Pressure Sitting | 3400 | 120/70
Blood Pressure Standing (1 min) | 2560 | 90/60
Blood Pressure Standing | 523 | 110/70
Blood Pressure Standing (3 mins) | 626 | 80/50
BMI (kg/m2) | 1662112 | 26.6
Weight (Lbs) | 1889542 | 150
Blood Pressure | 2169549 | 110/70
Height (Inches) | 706906 | 64
BMI | 554 | 25.0
Weight | 354 | 150.00
Height | 39 | 64.50

### `result_value`

`result_value` is the value associated with the given OMR observation. For example, for the `result_name` of 'Blood Pressure', the `field_value` column contains the recorded blood pressure (120/80, 130/70, and so on).

