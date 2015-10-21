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


# Overview of the MIMIC-III data

MIMIC is a relational database containing tables of data relating to patients who stayed within the intensive care units at Beth Israel Deaconess Medical Center. For example, the IOEVENTS table contains all measurements related to intake and output for a given patient. 

The tables are linked by identifiers which usually have the suffix "ID". For example `HADM_ID` refers to a unique hospital admission and `SUBJECT_ID` refers to a unique patient. One exception is `ROW_ID`, which is simply a row identifier unique to that table.

Tables pre-fixed with "D_" are dictionaries and provide definitions for identifiers. For example, every row of IOEVENTS is associated with a single `ITEMID` which represents the concept measured, but it does *not* contain the actual name of the drug. By joining IOEVENTS and D_ITEMS on `ITEMID`, it is possible to identify what concept a given `ITEMID` represents.

# List of tables

The following tables are used to define and track patient stays:

 - **ADMISSIONS**: Every unique hospitalization for each patient in the database (defines `HADM_ID`)
 - **CALLOUT**: Defines when a patient was scheduled for ICU discharge and when the patient was actually discharged
 - **ICUSTAYEVENTS**: Every unique ICU stay in the database (defines `ICUSTAY_ID`)
 - **PATIENTS**: Every unique patient in the database (defines `SUBJECT_ID`)
 - **SERVICES**: The service under which a patient received care
 - **TRANSFERS**: Patient movement within the hospital, including admission and discharge to the ICU

Each `ICUSTAY_ID` corresponds to a single `HADM_ID` and a single `SUBJECT_ID`. Each `HADM_ID` corresponds to a single `SUBJECT_ID`. A single `SUBJECT_ID` can correspond to multiple `HADM_ID` (multiple hospitalizations of the same patient), and multiple `ICUSTAY_ID` (multiple ICU stays either within the same hospitalization, or across multiple hospitalizations, or both).
 
The following tables contain data associated with each patient:

 - **CAREGIVERS**: Every caregiver who has recorded data in the database (defines `CGID`)
 - **CHARTEVENTS**: All charted observations for all patients
 - **CPTEVENTS**: Procedures recorded as Current Procedural Terminology (CPT) codes
 - **DATETIMEEVENTS**: Recorded observations which relate to dates (anonymized).
 - **DIAGNOSES_ICD**: Hospital assigned diagnoses as classified by the international classification of diseases and related health problems (ICD)
 - **DRGCODES**: Diagnosis Related Groups (DRGs) which are used for hospital billing for patient stays
 - **IOEVENTS**: Intake and output information for patients while in the ICU
 - **LABEVENTS**: Laboratory measurements for patients both within the hospital and in out patient clinics
 - **MICROBIOLOGYEVENTS**: Microbiology measurements and sensitivities from the hospital database
 - **NOTEEVENTS**: Deidentified notes, including nursing notes, ECG reports, echo reports, and discharge summaries
 - **PRESCRIPTIONS**: Medications ordered, and not necessarily administered, for a given patient
 - **PROCEDURES_ICD**: Patient procedures performed as coded by the international classification of diseases and related health problems (ICD) system
 
The following tables are dictionaries:
 
 - **D_CPT**: High-level dictionary of Current Procedural Terminology (CPT) codes
 - **D_ICD_DIAGNOSES**: Dictionary of International Classification of Diseases (ICD) codes relating to diagnoses
 - **D_ICD_PROCEDURES**: Dictionary of International Classification of Diseases (ICD) codes relating to procedures
 - **D_ITEMS**: Describes `ITEMID`s in the ICU database
 - **D_LABITEMS**: Describes `ITEMID`s in the laboratory database

