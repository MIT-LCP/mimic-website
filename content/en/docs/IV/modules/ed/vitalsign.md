---
title: "vitalsign table"
date: 2020-08-10
weight: 1
description: >
  vitalsign table
---

# The *vitalsign* table

Patients admitted to the emergency department have routine vital signs taken ever 1-4 hours. These vital signs are stored in the *vitalsign* table.

**Table source:** Emergency department information system.

**Table purpose:** Provides nurse documented vital signs.

**Number of rows:** 1,564,610

**Links to:**

* *edstays* on `stay_id`

## Important considerations

The numeric entries in this table were originally stored as free-text. As a result, the columns required deidentification. Free-text entries which could not be converted trivially were removed. Normally, the application of deidentification in MIMIC-IV is indicated using three underscores (`___`) to make it clear to users that we have modified the data. We decided it was better to omit this modification than to add confusion and difficulty to users by sharing the majority numeric data as text. As a result, **missing data in the numeric columns indicates either deidentified data or no data recorded**. However, for the most part, missing data indicates that no information was documented. Below is a table demonstrating how often data were removed for deidentification purposes:

Column | Number of NULL values inserted for deidentification | Number of rows missing data in v2.1
--- | --- | ---
`temperature` | 11048 | 564968
`heartrate`   | 3282  | 69710
`resprate`    | 1330  | 89393
`o2sat`       | 46620 | 135836
`sbp`         | 2854  | 81256
`dbp`         | 2854  | 81256

From the above, we can see that of the 564968 rows missing a `temperature` value, 11048 had a free-text value which was deleted during deidentification (~2%).

<!--
SQL queries to generate the above:

select
   COUNT(vs_phi.temp)   - COUNT(vs.temperature) AS temperature
 , COUNT(vs_phi.pulse)  - COUNT(vs.heartrate) AS heartrate
 , COUNT(vs_phi.rr)     - COUNT(vs.resprate) AS resprate
 , COUNT(vs_phi.o2sat)  - COUNT(vs.o2sat) AS o2sat
 , COUNT(vs_phi.bp)     - COUNT(vs.sbp) AS sbp
 , COUNT(vs_phi.bp)     - COUNT(vs.dbp) AS dbp
from ed_phi.vitalsign vs
left join sh.vitalsign vs_phi
using (fiscal_num_ed, charttime)

-- if you want total rows, union to the below
UNION ALL
select
   COUNT(*) - COUNT(vs.temperature) AS temperature
 , COUNT(*) - COUNT(vs.heartrate) AS heartrate
 , COUNT(*) - COUNT(vs.resprate) AS resprate
 , COUNT(*) - COUNT(vs.o2sat) AS o2sat
 , COUNT(*) - COUNT(vs.sbp) AS sbp
 , COUNT(*) - COUNT(vs.dbp) AS dbp
from ed_phi.vitalsign vs
;

-->

## Table columns

Name | Postgres data type
---- | ----
`subject_id`  | INTEGER NOT NULL
`stay_id`     | INTEGER NOT NULL
`charttime`   | TIMESTAMP(0)
`temperature` | NUMERIC(10, 4)
`heartrate`   | NUMERIC(10, 4)
`resprate`    | NUMERIC(10, 4)
`o2sat`       | NUMERIC(10, 4)
`sbp`         | INTEGER
`dbp`         | INTEGER
`rhythm`      | TEXT
`pain`        | TEXT

## `subject_id`

`subject_id` is a unique identifier which specifies an individual patient. Any rows associated with a single `subject_id` pertain to the same individual.

## `stay_id`

An identifier which uniquely identifies a single emergency department stay for a single patient.

## `charttime`

The time at which the vital signs were charted.

## `temperature`

The patient's temperature in degrees Farenheit. Some temperatures may be incorrectly documented as Celsius.

## `heartrate`

The patient's heart rate in beats per minute.

## `resprate`

The patient's respiratory rate in breaths per minute.

## `o2sat`

The patient's oxygen saturation measured as a percentage.

## `sbp`, `dbp`

The patient's systolic (sbp) and diastolic (dbp) blood pressure measured in millimetres of mercury (mmHg).

<!-- o2flow -->

## `rhythm`

The patient's heart rhythm.

## `pain`

The patient's self-reported level of pain on a scale from 0-10. The pain is documented as free-text and may contain non-numeric entries.