---
title: "procedureevents"
linktitle: "procedureevents"
weight: 10
date: 2020-08-10
description: >
  Procedures documented during the ICU stay (e.g. ventilation), though not necessarily conducted within the ICU (e.g. x-ray imaging).
---


# The procedureevents_mv table

**Table source:** MetaVision ICU database.

**Table purpose:** Contains procedures for patients

**Number of rows:** 592,932

**Links to:**

* patients on `subject_id`
* admissions on `hadm_id`
* icustays on `stay_id`
* d_items on `itemid`

<!-- # Important considerations -->

# Table columns


Name | Data type
---- | --------
subject\_id | Integer
hadm\_id | Integer
stay\_id | Integer
itemid | Integer
charttime | Date with times
storetime | Date with times
value | Text
valuenum | Decimal number
valueuom | Text
warning | Binary (0 or 1)
location |  VARCHAR(30)
locationcategory |  VARCHAR(30)
storetime |  TIMESTAMP(0)
cgid  |  INT
orderid |  INT
linkorderid |  INT
ordercategoryname |  VARCHAR(100)
secondaryordercategoryname |  VARCHAR(100)
ordercategorydescription |  VARCHAR(50)
isopenbag |  SMALLINT
continueinnextdept |  SMALLINT
cancelreason |  SMALLINT
statusdescription |  VARCHAR(30)
comments_editedby |  VARCHAR(30)
comments_canceledby |  VARCHAR(30)
comments_date |  TIMESTAMP(0)

<!--

# Detailed Description

## `subject_id`, `hadm_id`

Identifiers which specify the patient: `subject_id` is unique to a patient and `hadm_id` is unique to a patient hospital stay.

## `PROC_SEQ_NUM`

`PROC_SEQ_NUM` provides the order in which the procedures were performed.

## `ICD9_CODE`

`CODE` provides the code for the given procedure. 

-->


<!-- 
## `CGID`

`CGID` is the identifier for the caregiver who validated the given measurement.

-->
