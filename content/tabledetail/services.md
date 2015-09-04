+++
date = "2015-09-01T19:34:46-04:00"
title = "Services"
linktitle = "Services"
weight = 22
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

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
SUBJECT_ID | INT
HADM_ID | INT
TRANSFERTIME | TIMESTAMP(0)
PREV_SERVICE | VARCHAR(20)
CURR_SERVICE | VARCHAR(20)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `TRANSFERTIME`

## `PREV_SERVICE`, `CURR_SERVICE`


# Important considerations