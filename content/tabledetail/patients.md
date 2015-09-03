+++
date = "2015-09-01T19:34:46-04:00"
title = "Patients"
linktitle = "Patients"
weight = 19
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

Table source: CareVue and Metavision ICU databases.
Table purpose: Contains all charted data for all patients.
Number of rows: 
Links to: 
* ADMISSIONS on `SUBJECT_ID`
* ICUSTAYEVENTS on `SUBJECT_ID`

# Table columns

	SUBJECT_ID INT, 
	GENDER VARCHAR(5), 
	DOB TIMESTAMP(0), 
	DOD TIMESTAMP(0), 
	DOD_HOSP TIMESTAMP(0), 
	DOD_SSN TIMESTAMP(0), 
	HOSPITAL_EXPIRE_FLAG VARCHAR(5)
	
# Detailed Description

## `SUBJECT_ID`

`SUBJECT_ID` is a unique identifier which specifies an individual patient. `SUBJECT_ID` is an alternate primary key to this table; each row contains a unique `SUBJECT_ID`. Information which is consistent for the lifetime of a patient is stored in this table.

## `GENDER`

`GENDER` is the genotypical sex of the patient.

## `DOB`

`DOB` is the date of birth of the given patient. Patients who are older than 89 years old at any time in the database have had their date of birth shifted to obscure their age and comply with HIPAA. The shift process was as follows: the patient's age at their first admission was determined. The date of birth was then set to exactly 210 years before their first admission. As a result, all patients

## `DOD`, `DOD_HOSP`, `DOD_SSN`

## `HOSPITAL_EXPIRE_FLAG`


# Important considerations