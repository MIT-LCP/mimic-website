+++
date = "2015-09-01T19:34:46-04:00"
title = "SERVICES"
linktitle = "SERVICES"
weight = 34
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Lists services that a patient was admitted/transferred under.

**Number of rows:** 73,343

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

# Brief summary

The services table describes the service that a patient was admitted under. While a patient can be physicially located at a given ICU type (say MICU), they are not necessarily being cared for by the team which staffs the MICU. This can happen due to a number of reasons, including bed shortage. The SERVICES table should be used if interested in stratifying patients by their ICU type. The following is a map from services to ICU types:

Service | ICU service
--- | ---
CMED | CCU
CSURG | CSRU
DENT |
ENT |
GU |
GYN |
MED | MICU
NB | Newborn
NBB | Newborn
NMED | MICU
NSURG | SICU
OBS |
ORTHO | MICU
OMED | MICU
PSURG |
PSYCH |
SURG | SICU
TRAUM | TSICU
TSURG | TSICU
VSURG | CSRU


<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
SUBJECT\_ID | INT
HADM\_ID | INT
TRANSFERTIME | TIMESTAMP(0)
PREV\_SERVICE | VARCHAR(20)
CURR\_SERVICE | VARCHAR(20)

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `TRANSFERTIME`

`TRANSFERTIME` is the time at which the patient moved from the `PREV_SERVICE` (if present) to the `CURR_SERVICE`.

## `PREV_SERVICE`, `CURR_SERVICE`

`PREV_SERVICE` and `CURR_SERVICE` are the previous and current service that the patient resides under.
