---
title: "ICU stays"
linktitle: "icustays"
weight: 1
date: 2023-09-18
description: >
  Tracking information for ICU stays including admission and discharge times.
---

Defines each ICU stay in the database using `stay_id`.

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`

# Table columns

Name | Postgres data type
---- | ----
subject\_id | INT
hadm\_id | INT
stay\_id | INT
first\_careunit | VARCHAR(20)
last\_careunit | VARCHAR(20)
intime | TIMESTAMP(0)
outtime | TIMESTAMP(0)
los | DOUBLE PRECISION

# Detailed Description

### `subject_id`, `hadm_id`

Identifiers which specify the patient: `subject_id` is unique to a patient, `hadm_id` is unique to a patient hospital stay.

### `stay_id`

`stay_id` is an integer identifier which uniquely identifies each ICU admission within a hospital admission. Each hospital admission `hadm_id` must have at least one ICU admission `stay_id` but may include more than one. If the time between two ICU stays is less than 24 hours, the two stays will be merged into one.

### `first_careunit`, `last_careunit`

`first_careunit` and `last_careunit` contain, respectively, the first and last ICU type in which the patient was cared for. 

NHMC definitions for `first_careunit` and `last_careunit`:

| first_careunit/last_careunit        | Full abbreviation (Epic)         |
|------------------------------------|----------------------------------|
| ORTHOPEDICS                        | Emergency Medicine service       |
| CCU                                | General Medicine ICU service     |
| NSICU                              | Neuro Step Down service          |
| ICU OVERFLOW                       | Internal Medicine service        |
| IMCU                               | Neuro ICU service                |
| MTU                                | General Medicine service         |
| MICU                               | Medicine service                 |
| PICU                               |                                  |
| BOARDERS                           | Internal Medicine service        |
| CICU                               | Surgery service                  |
| NICU                               |                                  |
| NEUROSCIENCE INPATIENT             | Neurosurgery service             |
| SICU                               | Surgery ICU service              |
| ICU                                |                                  |
| INPATIENT                          |                                  |
| CTICU                              | Cardiology ICU                   |
| CTU                                | CARDIAC TELEMETRY UNIT, General Medicine service |
| RADIOLOGY                          |                                  |

Note, the addition of ICU overflow in both BIDMC and NHMC as a `first_careunit` and/or `last_careunit`. In the context of COVID-19, an 'ICU overflow' typically refers to a situation in which intensive care units (ICUs) in a hospital or healthcare facility have reached or exceeded their capacity due to a surge in COVID-19 patients requiring critical care. This overflow occurs when the number of patients needing intensive care for COVID-19 exceeds the available ICU beds.

### `intime`, `outtime`

`intime` provides the date and time the patient was transferred into the ICU. `outtime` provides the date and time the patient was transferred out of the ICU.

### `los`

`los` is the length of stay for the patient for the given ICU stay, which may include one or more ICU units. The length of stay is measured in fractional days.
