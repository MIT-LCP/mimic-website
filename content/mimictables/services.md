+++
date = "2015-09-01T19:34:46-04:00"
title = "SERVICES"
linktitle = "SERVICES"
weight = 32
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC data"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Lists services that a patient was admitted/transferred under.

**Number of rows:** 73,344

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

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
# Important considerations