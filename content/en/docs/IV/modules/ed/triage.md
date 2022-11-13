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

**Table source:** Emergency department information system.

**Table purpose:** Store information collected on triage to the emergency department.

**Number of rows:** 425,087

**Links to:**

* *edstays* on `stay_id`

## Important considerations

There is no time associated with triage observations. The closest approximation to triage time is the `intime` of the patient from the *edstays* table.

The numeric entries in this table were originally stored as free-text. As a result, the columns required deidentification. Free-text entries which could not be converted trivially were removed. Normally, the application of deidentification in MIMIC-IV is indicated using three underscores (`___`) to make it clear to users that we have modified the data. However, due to the data type restriction, we were unable to do this in this case. As a result, **missing data in the numeric columns indicates either deidentified data or no data recorded**. However, this is usually rare. Below is a table demonstrating how often data were removed for deidentification purposes:

Column | Number of NULL values inserted for deidentification | Number of rows missing data in v2.1
--- | --- | ---
`temperature` | 680 | 23415
`heartrate`   | 292 | 17090
`resprate`    | 223 | 20353
`o2sat`       | 414 | 20596
`sbp`         | 238 | 18291
`dbp`         | 214 | 19091
`acuity`      | 0   | 6987

From the above, we can see that of the 23415 rows missing a `temperature` value, only 680 had a free-text value which was deleted during deidentification (~3%).

<!--
SQL queries to generate the above:

select
 COUNT(tr_phi.temp) - COUNT(tr.temperature) AS temperature
 , COUNT(tr_phi.hr) - COUNT(tr.heartrate) AS heartrate
 , COUNT(tr_phi.rr) - COUNT(tr.resprate) AS resprate
 , COUNT(tr_phi.sao2) - COUNT(tr.o2sat) AS o2sat
 , COUNT(tr_phi.sbp) - COUNT(tr.sbp) AS sbp
 , COUNT(tr_phi.dbp) - COUNT(tr.dbp) AS dbp
 , COUNT(tr_phi.acuity) - COUNT(tr.acuity) AS acuity
from ed_phi.triage tr
left join sh.triage tr_phi
using (fiscal_num_ed)

-- if you want total rows, union to the below
UNION ALL
select
   COUNT(*) - COUNT(tr.temperature) AS temperature
 , COUNT(*) - COUNT(tr.heartrate) AS heartrate
 , COUNT(*) - COUNT(tr.resprate) AS resprate
 , COUNT(*) - COUNT(tr.o2sat) AS o2sat
 , COUNT(*) - COUNT(tr.sbp) AS sbp
 , COUNT(*) - COUNT(tr.dbp) AS dbp
 , COUNT(*) - COUNT(tr.acuity) AS acuity
from ed_phi.triage tr
;

-->
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
`pain`            | TEXT
`acuity`          | NUMERIC(10, 4)
`chiefcomplaint`  | VARCHAR(255)

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `temperature`

The patient's temperature in degrees Farenheit. Some temperatures may be incorrectly documented as Celsius.

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