---
title: "patients table"
linktitle: "patients"
date: 2023-09-18
weight: 2
description: >
  Detailed information about a patient's age, gender and date of death.
---
The *patients* table gives information regarding a patient's gender, age, and date of death. 

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`gender` | VARCHAR(1) NOT NULL
`anchor_age` | INTEGER NOT NULL
`anchor_year` | INTEGER NOT NULL
`anchor_year_group` | VARCHAR(255) NOT NULL
`dod` | TIMESTAMP(0)

## Detailed Description

### `subject_id`

`subject_id` is unique identifier for each patient. `subject_id` is unique to each row and can be used to identify data associated with a specific patient. It is a cryptographic random number and each patient has a `subject_id` which is consistent across tables.

### `gender`

The patient's administrative `gender`, sourced from the NW EDW and stored in the *patient* table, is represented as follows: F (Female), M (Male). 

### `anchor_age`

`anchor_age` is the age of the patient as of their admission date (earliest admission date if more than one). If a patient’s `anchor_age` is over 89 in the anchor_year then their anchor_age is set to 91. 

This ensures that the statistical anonymity of a patient is maintained and that the  data shared complies with the [HIPPA](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html) standards, specifically:

'(C) All elements of dates (except year) for dates that are directly related to an individual, including birth date, admission date, discharge date, death date, and all ages over 89 and all elements of dates (including year) indicative of such age, except that such ages and elements may be aggregated into a single category of age 90 or older.'

### `anchor_year`,
`anchor_year` is the shifted year based on the patient's shifted earliest admission date.

### `anchor_year_group`

`anchor_year_group` is the sequence of three years including the the year in which a patient was admitted. For example, if a patient was admitted in 2020, 2021, or 2022,  the `anchor_year_group` will be '2020-2022'.

### `dod`

The patient's date of death `dod` is shifted. Note, the `dod` is censored one year after discharge. Hence, if the death date is unknown it will be NULL.  If this date is missing, `dod` will be NULL. If the date is not missing, and if the date is within 365 days after the latest discharge date, this date will be used as DOD. If the date is not missing and is 365 or more days after the latest discharge date, then DOD will be NULL.
Note, the BIDMC database also includes out of hospital data from the state, as part of dod sourced externally from the [Massachusetts State Registry of Vital Records and Statistics](https://www.mass.gov/orgs/registry-of-vital-records-and-statistics), by using identifiers including name, social security number and date of birth.
