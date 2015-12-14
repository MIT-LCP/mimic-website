+++
date = "2015-09-01T19:34:46-04:00"
title = "Patient identifiers"
linktitle = "Patient identifiers"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Data details"

+++

# Types of data in the database

Data within MIMIC were recorded during routine clinical care and *not* explicitly for the purpose of retrospective data analysis. This is a key point to keep in mind when analyzing the data.

There are two types of data in the database: static data and dynamic data. Static data is recorded once for a given identifier. An example of static data is the `DOB` column in the PATIENTS table. Each patient has only one date of birth, which does not change over time and is not recorded with an associated timestamp. An example of dynamic data is a patient's blood pressure, which is periodically measured during a hospital stay. 

This distinction between static data and dynamic data is merely a helpful conceptual construct: there is *no* strict technical distinction between date of birth and heart rate. However, static data tends to not have an associated `ITEMID` (as there is no need to repeatedly record values for static data), whereas dynamic data have an `ITEMID` to facilitate efficient storage of repeated measurements.

# Static data

## `SUBJECT_ID`

The following is a list of static data available in the database for `SUBJECT_ID` in the PATIENTS table:

The only static data available for patients are their gender (`GENDER`), date of birth (`DOB`) and various dates of death (`DOD`, `DOD_HOSP`, `DOD_SSN`). These columns all occur in the PATIENTS table.

## `HADM_ID`

The following is a list of static data available in the database for `HADM_ID` in the ADMISSIONS table:

* Admission time
* Discharge time
* Death time
* Admission type

## `ICUSTAY_ID`

The following is a list of static data available in the database for `ICUSTAY_ID` in the ICUSTAYS table:

* `INTIME` - Time entered the ICU
* `OUTTIME` - Time left the ICU
* First care unit
* Last care unit

# Hospital acquired data

The following tables were sourced from the hospital database, and contain information recorded in the hospital, but not necessarily during the patient's ICU stay:

* ADMISSIONS
* CALLOUT
* CPTEVENTS
* DIAGNOSES_ICD
* DRGCODES
* ICUSTAYS
* LABEVENTS
* MICROBIOLOGYEVENTS
* PATIENTS
* PRESCRIPTIONS
* PROCEDURES_ICD
* SERVICES
* TRANSFERS

# ICU acquired data

The following tables were sourced from the ICU databases, and contain information only during a patient's ICU stay:

* DATETIMEEVENTS
* INPUTEVENTS_CV
* INPUTEVENTS_MV
* NOTEEVENTS
* OUTPUTEVENTS
* PROCEDUREEVENTS_MV

# Externally acquired data

The `DOD_SSN` (which also contributes to the `DOD` column) is acquired from the social security death registry. It contains dates of death up to 90 days in the future for Metavision patients. It contains dates of death up to 4 years in the future for CareVue patients.

<!--

# Manual input of data

Not all data in the ICU is recorded automatically by monitors and synchronized with the database. For example the Glasgow Coma Scale, a measurement of neurological dysfunction, requires interaction and observation with the patient by a member of the clinical staff. These observations must be manually recorded in the database. Typical workflow for data of this type is to record the observation on paper, and later transcribe a batch of data to the database. Again, the data would appear with a `CHARTTIME` corresponding to the hour of the measurement, and data entered contemporaneously would share the same `STORETIME`.

-->
