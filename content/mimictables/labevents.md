+++
date = "2015-09-01T19:34:46-04:00"
title = "LABEVENTS"
linktitle = "LABEVENTS"
weight = 26
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC tables"

+++


# Overview

**Table source:** Hospital database.

**Table purpose:** Contains all laboratory measurements for a given patient, including out patient data.

**Number of rows:** 27,872,575

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D_LABITEMS on `ITEMID`

# Table columns

Name | Postgres data type 
---- | ---- 
SUBJECT\_ID | INT
HADM\_ID | INT
ITEMID | INT
CHARTTIME | TIMESTAMP(0)
VALUE | VARCHAR(200)
VALUENUM | DOUBLE PRECISION
UOM | VARCHAR(20)
FLAG | VARCHAR(20)
	
# Detailed Description

The `LABEVENTS` data contains information regarding laboratory based measurements. The process for acquiring a lab measurement is as follows: first, a member of the clinical staff acquires a fluid from a site in the patient's body (e.g. blood from an arterial line, urine from a catheter, etc). Next, the fluid is bar coded to associate it with the patient *and* timestamped to record the time of the fluid acquisition. The lab analyses the data and returns a result within 4-12 hours.

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `ITEMID`

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` (e.g. 212) corresponds to an instantiation of the same measurement (e.g. heart rate).

## `CHARTTIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured.
Note that because the data is directly sourced from the laboratory database, it is *not* validated by ICU clinical staff, and as a result there is no associated `STORETIME`.

## `VALUE`, `VALUENUM`

`VALUE` contains the value measured for the concept identified by the `ITEMID`. If this value is numeric, then `VALUENUM` contains the same data in a numeric format. If this data is not numeric, `VALUENUM` is null. In some cases (e.g. scores like Glasgow Coma Scale, Richmond Sedation Agitation Scale and Code Status), `VALUENUM` contains the score and `VALUE` contains the score and text describing the meaning of the score.

## `UOM`

`UOM` is the unit of measurement for the `VALUE`, if appropriate.

## `FLAG`

`FLAG` indicates whether the laboratory value is considered abnormal or not, using pre-defined thresholds.

# Important considerations

* Note that the time associated with this result is the time of the fluid *acquisition*, not the time that the values were made available to the clinical staff. 
* The labevents table contains both in-hospital laboratory measurements *and* out of hospital laboratory measurements from clinics which the patient has visited (since the patient is not "in" a hospital when visiting a clinic, these patients often referred to as "out patients" and the data is often called "out patient" data).
* In MIMIC III v1.0, there is a subset of patients for which the outpatient lab data is not available. They can be identified by checking for patients whose data *always* has an `HADM_ID`.
* In MIMIC III v1.0, there is a subset of patients for which text laboratory data is missing. This primarily affects the blood gas type recorded with blood gases.