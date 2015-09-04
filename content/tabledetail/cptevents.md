+++
date = "2015-09-01T19:34:46-04:00"
title = "CPTEVENTS"
linktitle = "CPTEVENTS"
weight = 5
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Contains current procedural terminology (CPT) codes, which facilitate billing for procedures performed on patients.

**Number of rows:** 573146

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Table columns

Name | Postgres data type 
---- | ---- 
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
COSTCENTER | VARCHAR(10)
CHARTDATE | TIMESTAMP(0)
CPT\_CD | VARCHAR(10)
CPT\_NUMBER | INT
CPT\_SUFFIX | VARCHAR(5)
TICKET\_ID\_SEQ | INT
SECTIONHEADER | VARCHAR(50)
SUBSECTIONHEADER | VARCHAR(300)
DESCRIPTION | VARCHAR(200)

# Detailed Description

`CPTEVENTS` contains current procedural terminology (CPT) codes for patients as billed through either the ICU cost center or the respiratory cost center. Each code represents a distinct procedure performed on the patient during their ICU stay.

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `COSTCENTER`

`COSTCENTER` is the cost center which billed for the corresponding CPT codes. There are two possible cost centers: 'ICU' and 'Resp'. 'Resp' codes correspond to mechanical or non-invasive ventilation and were billed by the respiratory therapist. 'ICU' codes correspond to the procedures billed for by the ICU.

## `CHARTDATE`

The date at which the procedure occurred.

## `CPT_CD`, `CPT_NUMBER`, `CPT_SUFFIX`

`CPT_CD` contains the original CPT code. `CPT_NUMBER` is a numeric version of the `CPT_CD` column, which allows for easier range comparisons in querying. However, note not all `CPT_CD` are fully numeric. The `CPT_SUFFIX` column contains the text suffix when the `CPT_CD` contains non-numeric characters.

## `TICKET_ID_SEQ`

The order of the `CPT_CD`.

## `SECTIONHEADER`, `SUBSECTIONHEADER`

The section headers provide a category for the given CPT code. These headers were assigned using the D_CPT table.

## `DESCRIPTION`

In the case of a `CPT_CD` corresponding to the respiratory cost center, the description provides information about the meaning of the CPT code. Otherwise, the field is null.

# Important considerations

* The respiratory cost center bills for ventilation *regardless* of duration. That means that 30 minutes of mechanical ventilation for a single day would result in same billing code as a full 24 hours of mechanical ventilation.