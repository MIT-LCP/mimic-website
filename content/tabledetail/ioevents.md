+++
date = "2015-09-01T19:34:46-04:00"
title = "IOevents"
linktitle = "IOevents"
weight = 15
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"
+++


# Overview

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Input/output data for patients.

**Number of rows:** 25,889,251

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYEVENTS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

# Table columns

	SUBJECT_ID INT, 
	HADM_ID INT, 
	ICUSTAY_ID INT, 
	STARTTIME TIMESTAMP(0), 
	ENDTIME TIMESTAMP(0), 
	ITEMID INT, 
	VOLUME DOUBLE PRECISION, 
	VOLUMEUOM VARCHAR(30), 
	RATE DOUBLE PRECISION, 
	RATEUOM VARCHAR(30), 
	STORETIME TIMESTAMP(0), 
	CGID BIGINT, 
	ORDERID BIGINT, 
	LINKORDERID BIGINT, 
	ORDERCATEGORYNAME VARCHAR(100), 
	SECONDARYORDERCATEGORYNAME VARCHAR(100), 
	ORDERCOMPONENTTYPEDESCRIPTION VARCHAR(200), 
	ORDERCATEGORYDESCRIPTION VARCHAR(50), 
	PATIENTWEIGHT DOUBLE PRECISION, 
	TOTALVOLUME DOUBLE PRECISION, 
	TOTALVOLUMEUOM VARCHAR(50), 
	STATUSDESCRIPTION VARCHAR(30), 
	STOPPED VARCHAR(30), 
	NEWBOTTLE INT, 
	ISOPENBAG SMALLINT, 
	CONTINUEINNEXTDEPT SMALLINT, 
	CANCELREASON SMALLINT, 
	COMMENTS_STATUS VARCHAR(30), 
	COMMENTS_TITLE VARCHAR(100), 
	COMMENTS_DATE TIMESTAMP(0), 
	ORIGINALCHARTTIME TIMESTAMP(0), 
	ORIGINALAMOUNT DOUBLE PRECISION, 
	ORIGINALAMOUNTUOM VARCHAR(30), 
	ORIGINALROUTE VARCHAR(30), 
	ORIGINALRATE DOUBLE PRECISION, 
	ORIGINALRATEUOM VARCHAR(30), 
	ORIGINALSITE VARCHAR(30)
	
# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `CHARTTIME`, `STORETIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured. `STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

# Important considerations