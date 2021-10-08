---
title: "triage table"
date: 2020-08-10
weight: 1
description: >
  triage table
---

# The *triage* table

The *triage* table contains information about the patient when they were first triaged in the emergency department.
Patients are assessed at triage by a single care provider and asked a series of questions to assess their current health status.
Their vital signs are measured and a level of acuity is assigned. Based on the level of acuity, the patient either waits in the waiting room for later attention, or is prioritized for immediate care.

All fields in *triage* were originally free-text. For deidentification purposes, the vital sign and pain fields were converted into a numeric value. As a result, a small number of `NULL` values were introduced for text entries.

**Table source:** Emergency department database.

**Table purpose:** 

**Number of rows:** 

**Links to:**

* *edstays* on `stay_id`

# Important considerations

* There is no time associated with triage observations. The closest approximation to triage time is the `intime` of the patient from the *edstays* table.

# Table columns

Name | Postgres data type
---- | ----
`subject_id`      | INTEGER NOT NULL
`stay_id`         | INTEGER NOT NULL
`temperature`     | NUMERIC(10, 4)
`heartrate`       | NUMERIC(10, 4)
`resprate`        | NUMERIC(10, 4)
`o2sat`           | NUMERIC(10, 4)
`sbp`             | NUMERIC(10, 4)
`dbp`             | NUMERIC(10, 4)
`pain`            | NUMERIC(10, 4)
`acuity`          | NUMERIC(10, 4)
`chiefcomplaint`  | TEXT

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `temperature`

The patient's temperature in degrees Celsius. Incorrect documentation in Fahrenheit may occur.

## `heartrate`

The patient's heart rate in beats per minute.

## `resprate`

The patient's respiratory rate in breaths per minute.

## `o2sat`

The patient's peripheral oxygen saturation as a percentage.

## `sbp`, `dbp`

The patient's systolic and diastolic blood pressure, respectively, measured in millimitres of mercury (mmHg).

## `pain`

The level of pain self-reported by the patient, on a scale of 0-10.

## `acuity`

An order of priority based upon acuity utilizing the Emergency Severity Index (ESI) Five Level triage system. This priority is assigned by a registered nurse. Level 1 is the highest priority, while level 5 is the lowest priority. The levels are:

* 1
  * When Level 1 condition or patient meets ED Trigger Criteria, the triage process stops, the patient is taken directly to a room and immediate physician intervention requested.
  * Patient conditions which trigger level 1 include being unresponsive, intubated, apneic, pulseless, requiring a medication/intervention to alter ESI level e.g. narcan/adenosine/cardioversion, trauma, stroke, stemi
* 2
  * When a Level 2 condition is identified, the triage nurse notifies the resource nurse and appropriate placement will be determined.
  * Patient conditions which trigger level 2 include high risk situations, new onset confusion, suicidal/homicidal ideation, lethargy, seizures or disorientation, possible ectopic pregnancy, an immunocompromised patient with a fever, severe pain/distress, or vital sign instability
* 3
  * Includes patients requiring two or more resources (labs, EKG, x-rays, IV fluids, etc) with stable vital signs
* 4
  * Patients requiring one resource only (labs, EKG, etc)
* 5
  * Patients not requiring any resources

# `chiefcomplaint`

A deidentified free-text description of the patient's chief complaint.