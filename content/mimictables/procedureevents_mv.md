+++
date = "2015-09-01T19:34:46-04:00"
title = "PROCEDUREEVENTS_MV"
linktitle = "PROCEDUREEVENTS_MV"
weight = 32
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++


# The procedureevents_mv table

**Table source:** Metavision ICU database.

**Table purpose:** Contains procedures for patients

**Number of rows:** 258,066

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`

<!-- # Important considerations -->

# Table columns

Name | Postgres data type 
---- | ---- 
ROW_ID |  INT NOT NULL
SUBJECT_ID |  INT NOT NULL
HADM_ID |  INT NOT NULL
ICUSTAY_ID |  INT
STARTTIME |  TIMESTAMP(0)
ENDTIME |  TIMESTAMP(0)
ITEMID |  INT
VALUE |  DOUBLE PRECISION
VALUEUOM |  VARCHAR(30)
LOCATION |  VARCHAR(30)
LOCATIONCATEGORY |  VARCHAR(30)
STORETIME |  TIMESTAMP(0)
CGID  |  INT
ORDERID |  INT
LINKORDERID |  INT
ORDERCATEGORYNAME |  VARCHAR(100)
SECONDARYORDERCATEGORYNAME |  VARCHAR(100)
ORDERCATEGORYDESCRIPTION |  VARCHAR(50)
ISOPENBAG |  SMALLINT
CONTINUEINNEXTDEPT |  SMALLINT
CANCELREASON |  SMALLINT
STATUSDESCRIPTION |  VARCHAR(30)
COMMENTS_EDITEDBY |  VARCHAR(30)
COMMENTS_CANCELEDBY |  VARCHAR(30)
COMMENTS_DATE |  TIMESTAMP(0)

<!--
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `PROC_SEQ_NUM`

`PROC_SEQ_NUM` provides the order in which the procedures were performed.

## `ICD9_CODE`

`CODE` provides the code for the given procedure. 

-->
