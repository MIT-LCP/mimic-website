+++
date = "2015-09-01T19:34:46-04:00"
title = "Overview"
linktitle = "Overview"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC data"

+++


# Data organization

MIMIC is organized in a table structure. There are 23 tables, each of which pertaining to a certain type of data collected. For example, the IOEVENTS table contains all measurements related to intake and output for a given patient. These tables make querying the data easier as certain concepts, such as drug infusions, are only logically extracted from the correct table type, in this case IOEVENTS. Data is linked together between tables using an identifier (which usually has the suffix "ID") depending on the data. Note however that `ROW_ID`, present in every table, *does not link any table together*, and is just a row identifier (for those familiar with SQL, `ROW_ID` is the primary key for each table).

A table pre-fixed with "D_" is a dictionary and defines a single identifier. For example, every row of IOEVENTS is associated with a single `ITEMID` which represents the concept measured, but it does *not* contain the actual name of the drug. By joining IOEVENTS and D_ITEMS on `ITEMID`, it is possible to identify what concept a given `ITEMID` represents.

# List of tables

The following tables are used to define and track patient stays:

 - PATIENTS - Every unique patient in the database (defines `SUBJECT_ID`)
 - ADMISSIONS - Every unique hospitalization for each patient in the database (defines `HADM_ID`)
 - ICUSTAYEVENTS - Every unique ICU stay in the database (defines `ICUSTAY_ID`)
 - SERVICES - The service under which a patient is currently cared for
 - TRANSFERS - Patient movement within the hospital, including admission and discharge to the ICU

Each `ICUSTAY_ID` corresponds to a single `HADM_ID` and a single `SUBJECT_ID`. Each `HADM_ID` corresponds to a single `SUBJECT_ID`. A single `SUBJECT_ID` can correspond to multiple `HADM_ID` (multiple hospitalizations of the same patient), and multiple `ICUSTAY_ID` (multiple ICU stays either within the same hospitalization, or across multiple hospitalizations, or both).
 
The following tables contain data associated with each patient:

 - CALLOUT - Information regarding when a patient was scheduled for ICU discharge and when the patient was actually discharged
 - CAREGIVERS - Every caregiver who has recorded data in the database (defines `CGID`)
 - CHARTEVENTS - All charted observations for all patients
 - CPTEVENTS - Procedure codes for all procedures done for patients in the ICU
 - DATETIMEEVENTS - All recorded observations which are dates. These observations have been anonymized.
 - DIAGNOSES_ICD - Hospital assigned diagnoses as classified by the international classification of diseases and related health problems (ICD)
 - DRGCODES - Diagnosis related groups (DRG) which are used for hospital billing for patient stays
 - IOEVENTS - Intake and output information for patients while in the ICU
 - LABEVENTS - Laboratory measurements for patients both within the hospital and in out patient clinics
 - MICROBIOLOGYEVENTS - Microbiology measurements and sensitivities from the hospital database
 - NOTEEVENTS - De-identified notes, including nursing notes, ECG reports, echo reports, and discharge summaries
 - PRESCRIPTIONS - Medications ordered, and not necessarily administered, for a given patient
 - PROCEDURES_ICD - Patient procedures performed as coded by the international classification of diseases and related health problems (ICD) system
 
The following dictionary tables exist in the database:
 
 - D_CPT - Provides high level information regarding current procedural terminology (CPT) codes
 - D_ICD_DIAGNOSES - Brief description for each ICD code related to a diagnosis
 - D_ICD_PROCEDURES - Brief description for each ICD code related to a procedure
 - D_ITEMS - Defines each `ITEMID` in the ICU database, which are used to represent concepts
 - D_LABITEMS - Defines each `ITEMID` in the laboratory database sourced from the hospital

