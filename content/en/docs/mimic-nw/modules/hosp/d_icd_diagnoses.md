---
title: "d_icd_diagnoses"
linktitle: "d_icd_diagnoses"
weight: 6
date: 2023-09-18
description: >
  Dimension table for *diagnoses_icd*; provides a description of ICD-9/ICD-10 billed diagnoses.
---

The *d_icd_diagnoses* table defines International Classification of Diseases (ICD) Version 9 and 10 codes for **diagnoses**. These codes are assigned at the end of the patient's stay and are used by the hospital to bill for care provided.

### Links to

* *diagnoses_icd* ON `icd_code` and `icd_version`

## Table columns

Name | Postgres data type
---- | ----
`icd_code` | CHAR(7) NOT NULL
`icd_version` | INTEGER NOT NULL
`long_title`  | VARCHAR(255)

## Detailed Description

### `icd_code`

`icd_code` is the International Coding Definitions (ICD) code.

### `icd_version`
There are two versions for this coding system: version 9 (ICD-9) and version 10 (ICD-10). These can be differentiated using the `icd_version` column. [ICD-9](https://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes) and [ICD-10](https://www.cms.gov/Medicare/Coding/ICD10/2019-ICD-10-CM.html) diagnosis codes are acquired from Centers for Medicare & Medicaid Services (CMS).

In general, ICD-10 codes are more detailed, though code mappings (or "cross-walks") exist which convert ICD-9 codes to ICD-10 codes.

Both ICD-9 and ICD-10 codes are often presented with a decimal. This decimal is not required for interpretation of an ICD code; i.e. the `icd_code` of '0010' is equivalent to '001.0'.

ICD-9 and ICD-10 codes have distinct formats: ICD-9 codes are 5 character long strings which are entirely numeric (with the exception of codes prefixed with "E" or "V" which are used for external causes of injury or supplemental classification). Importantly, ICD-9 codes are retained as strings in the database as the leading 0s in codes are meaningful.

ICD-10 codes are 3-7 characters long and always prefixed by a letter followed by a set of numeric values.

ICD-11 became the official [WHO standard](https://www.who.int/standards/classifications/classification-of-diseases) on January 1, 2022  but has not been adopted in the US. The US Center for Medicare and Medicaid services (CMS) and HIPAA require ICD-10 since October 1, 2015.

### `long_title`

The `long_title` provides a description of the ICD code. For example, the ICD-10 code U07.1 has `long_title` "COVID-19 (confirmed by laboratory testing)".

In the tables below, we provide ICD-10 codes related to covid or long covid.

ICD-10 COVID markers terminologies:

| icd_code | long_title                                                |
| -------- | -------------------------------------------------------- |
| U07.1    | COVID-19 (confirmed by laboratory testing)              |
| U07.2    | COVID-19, virus not identified                         |
| U10.9    | Multisystem inflammatory syndrome associated with COVID-19 |
| J12.81   | Pneumonia due to SARS-associated coronavirus           |


ICD-10 Long COVID markers terminologies:

| icd_code | long_title                                      |
| -------- | ---------------------------------------------- |
| U09.9    | Post COVID-19 condition, unspecified            |

ICD-10 Other COVID related terminologies:

| icd_code | long_title                                                                                               |
|----------|-----------------------------------------------------------------------------------------------------------|
| U08.9    | Personal history of COVID-19, unspecified (not a marker)                                                  |
| B97.2    | Coronavirus as the cause of diseases classified elsewhere (not necessarily COVID-19)                  |
| B97.21   | SARS-associated coronavirus as the cause of diseases classified elsewhere                                 |
| Z28.31   | Underimmunization for COVID-19 status (see detailed codes below)                                           |
| Z28.310  | Unvaccinated for COVID-19                                                                               |
| Z28.311  | Partially vaccinated for COVID-19                                                                       |
| B97.29   | Other coronavirus as the cause of diseases classified elsewhere (SUPERSEDED; early coding guidelines)   |
| Z20.822  | Contact with and (suspected) exposure to COVID-19 (unconfirmed)                                           |
| Z86.16   | Personal history of COVID-19                                                                           |
