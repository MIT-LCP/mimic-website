---
title: "admissions table"
linktitle: "admissions"
date: 2023-09-18
weight: 1
description: >
  Detailed information about hospital stays, including admission, discharge, and death times, as well as admission type, admission location, and discharge location; additionally, patient details such as insurance, language, marital status, and race are recorded at the hospital stay level.
---

The *admissions* table gives information regarding a patient's admission to the hospital. 

### Links to

* *patients* on `subject_id`

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER NOT NULL
`admittime` | TIMESTAMP NOT NULL
`dischtime` | TIMESTAMP
`deathtime` | TIMESTAMP
`admission_type` | VARCHAR(40) NOT NULL
`admission_location` | VARCHAR(60)
`discharge_location` | VARCHAR(60)
`insurance` | VARCHAR(255)
`language` | VARCHAR(10)
`marital_status` | VARCHAR(30)
`race` | VARCHAR(80)
`ethnicity` | VARCHAR(80)
`edregtime` | TIMESTAMP
`edouttime` | TIMESTAMP
`hospital_expire_flag` | SMALLINT

## Detailed description

The *admissions* table defines all hospitalizations in the database. Hospitalizations are assigned a unique random integer known as the `hadm_id`.

### `subject_id`

`subject_id` is unique identifier for each patient. `subject_id` is unique to each row and can be used to identify data associated with a specific patient. It is a cryptographic random number and each patient has a `subject_id` which is consistent across tables.

### `hadm_id`

Each row of this table contains a unique `hadm_id`, which represents a single patient's admission to the hospital. It is possible for this table to have duplicate `subject_id`, indicating that a single patient had multiple admissions to the hospital. The ADMISSIONS table can be linked to the *patients* table using `subject_id`.

### `admittime`

`admittime` provides the date and time the patient was admitted to the hospital.

### `dischtime`

`dischtime` provides the date and time the patient was discharged from the hospital.

### `deathtime`

`deathtime` provides the time of in-hospital death for the patient. Note that `deathtime` is only present if the patient died in-hospital, and if present is almost always the same as the patient’s dischtime. However, there may be some discrepancies.

### `admission_type`

`admission_type` is useful for classifying the urgency of the admission. There are 6 distinct additional admission types sourced from the NW EDW database: 'Emergency', 'Urgent', 'Elective', 'Elective-Routine', and 'Trauma'.
 
### `admission_location`

`admission_location` provides information about the hospital department into which the patient was initially admitted. There are 24 admission locations from NW EDW, including  'Neurology', 'Radiation Oncology', 'Pediatrics', 'Medicine', 'Respiratory Therapy', 'Cardiology', 'Cardiac Rehabilitation', 'Pre-Admission Testing', 'Neurological Intensive Care', 'Orthopaedic Surgery', 'Sleep Medicine', 'Gastroenterology', 'Unknown', 'Obstetrics and Gynecology', 'Emergency Medicine', 'Research', 'Intensive Care', 'Gynecology', 'Pediatric Intensive Care', 'Radiology', 'Pathology', 'Obstetrics', and 'Surgery'. Note, 'Pediatrics' is the name of the unit or room, which is not necessarily exclusively for pediatric patients. The data being shared pertains to the adult hospital, with patients aged 18 and above.


## `discharge_location`

Similarly, `discharge_location` is the disposition of the patient after they are discharged from the hospital. There are 33 discharge locations from NW EDW. Some of the 33 discharge locations are suppressed under 'Other Facility' for privacy.

NHMC discharge locations:

| Discharge Location                                      | Full Abbreviation (for clarity)     |
| ------------------------------------------------------- | --------------------------------- |
| Expired                                                 | Died                            |
| Planned Readmission - DC/transferred to acute inpatient rehab |                             |
| ED Dismissed-Never Arrived                              |                                 |
| Home with Equipment or O2                              |                                 |
| Shelter                                                |                                 |
| Expired - Hospice                                      | Died in Hospice                           |
| Home with Home Health Care                             |                                 |
| Planned Readmission - DC/transferred to skilled nursing facility |                         |
| Acute Inpatient Rehabilitation                         |                                 |
| Home or Self Care                                      |                                 |
| Group Home                                             |                                 |
| Planned Readmission - Discharged to home/self-care     |                                 |
| Left Against Medical Advice                            |                                 |
| Inpatient Hospice                                      |                                 |
| Admitted to L&D                                        | Admitted to Labor and Delivery                |
| Planned Readmission - DC/transferred to nursing home (custodial) |                     |
| unknown                                                |                                 |
| Cancer Center or Children's Hospital                   |                                 |
| Home with Outpatient Services                          |                                 |
| Critical Access Hospital                               |                                 |
| Planned Readmission - DC/transferred to other type of healthcare institution |     |
| Gift of Hope / Still a Patient                         |                                 |
| Nursing Home (Custodial)                               |                                 |
| Home with Hospice                                      |                                 |
| VA System Facility                                     |                                 |
| Planned Readmission - DC/transferred to Long-term Acute Care Hospital (LTAC) |       |
| Swing Bed                                              |                                 |
| Against Medical Advice (AMA) or Elopement              |                                 |
| Skilled Nursing Facility or Subacute Rehab Care        |                                 |
| Designated Disaster Alternative Care Site               |                                 |
| Acute Care Hospital                                    |                                 |
| Long-Term Acute Care Hospital (LTAC)                   |                                 |


### `insurance`, `language`, `marital_status`, `race`, `ethnicity`

The `insurance`, `language`, `marital_status`, and `race` and `ethnicity` columns provide information about patient demographics for the given hospitalization. Note, in BIDMC there is only one column for `race`, however we have added `ethnicity` column to federate NHMC's data.

The race column in NHMC includes:

- American Indian or Alaska Native
- Other
- Unknown
- 2 or more races
- Unable to Answer
- Native Hawaiian or Other Pacific Islander
- Asian
- White
- Declined
- Black or African American

The ethnicity column in NHMC includes:

- Not Hispanic or Latino
- Hispanic or Latino
- Declined
- Unable to Answer

### `edouttime`

The date and time at which arrival of the patient in the emergency department was registered.

### `edouttime`
The date and time at which the patient was discharged from the emergency department, either discharged from the hospital or transferred.

### `hospital_expire_flag`

This is a binary flag which indicates whether the patient died within the given hospitalization. `1` indicates death in the hospital as noted in the `dod` column as part of the *patient* table, and `0` indicates survival to hospital discharge. 
