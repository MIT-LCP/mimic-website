+++
date = "2015-09-01T19:34:46-04:00"
title = "PATIENTS"
linktitle = "PATIENTS"
weight = 29
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Contains all charted data for all patients.

**Number of rows:** 46,520

**Links to:**

* ADMISSIONS on `SUBJECT_ID`
* ICUSTAYEVENTS on `SUBJECT_ID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
GENDER | VARCHAR(5)
DOB | TIMESTAMP(0)
DOD | TIMESTAMP(0)
DOD\_HOSP | TIMESTAMP(0)
DOD\_SSN | TIMESTAMP(0)
HOSPITAL\_EXPIRE\_FLAG | VARCHAR(5)
	
# Detailed Description

## `SUBJECT_ID`

`SUBJECT_ID` is a unique identifier which specifies an individual patient. `SUBJECT_ID` is a candidate key for the table, so is unique for each row. Information that is consistent for the lifetime of a patient is stored in this table.

## `GENDER`

`GENDER` is the genotypical sex of the patient.

## `DOB`

`DOB` is the date of birth of the given patient. Patients who are older than 89 years old at any time in the database have had their date of birth shifted to obscure their age and comply with HIPAA. The shift process was as follows: the patient's age at their first admission was determined. The date of birth was then set to exactly 210 years before their first admission. <!-- As a result, all patients-->

## `DOD`, `DOD_HOSP`, `DOD_SSN`

`DOD` is the date of death for the given patient. `DOD_HOSP` is the date of death as recorded in the hospital database. `DOD_SSN` is the date of death from the social security database. Note that `DOD` merged together `DOD_HOSP` and `DOD_SSN`, giving priority to `DOD_HOSP` if both were recorded. 

## `HOSPITAL_EXPIRE_FLAG`

`HOSPITAL_EXPIRE_FLAG` indicates whether the patient died within the hospital. Note that if `DOD_HOSP` is present, then the last admission for the patient will have `HOSPITAL_EXPIRE_FLAG` = 'Y'.

# Important considerations

* `DOB` has been shifted for patients older than 89. The median age for the patients whose date of birth was shifted is 91.4.
