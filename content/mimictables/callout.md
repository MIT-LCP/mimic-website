+++
date = "2015-09-01T19:34:46-04:00"
title = "CALLOUT"
linktitle = "CALLOUT"
weight = 11
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++


# Overview

**Table source:** Hospital database.

**Table purpose:** Provides information when a patient was ready for discharge, and when the patient was actually discharged.

**Number of rows:** 34499

**Links to:** 

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

# Table columns

Name | Postgres data type 
---- | ---- 
ROW\_ID | BIGINT
SUBJECT\_ID | INT
HADM\_ID | INT
SUBMIT\_WARDID | INT
SUBMIT\_CAREUNIT | VARCHAR(15)
CURR\_WARDID | INT
CURR\_CAREUNIT | VARCHAR(15)
CALLOUT\_WARDID | INT
CALLOUT\_SERVICE | VARCHAR(10)
REQUEST\_TELE | SMALLINT
REQUEST\_RESP | SMALLINT
REQUEST\_CDIFF | SMALLINT
REQUEST\_MRSA | SMALLINT
REQUEST\_VRE | SMALLINT
CALLOUT\_STATUS | VARCHAR(20)
CALLOUT\_OUTCOME | VARCHAR(20)
DISCHARGE\_WARDID | INT
ACKNOWLEDGE\_STATUS | VARCHAR(20)
CREATETIME | TIMESTAMP(0)
UPDATETIME | TIMESTAMP(0)
ACKNOWLEDGETIME | TIMESTAMP(0)
OUTCOMETIME | TIMESTAMP(0)
FIRSTRESERVATIONTIME | TIMESTAMP(0)
CURRENTRESERVATIONTIME | TIMESTAMP(0)

# Detailed description

The CALLOUT table provides information for "call out events". A call out event occurs as follows: first, a patient is ready for discharge from the ICU. A care provider creates a call out request (occurring at `CREATETIME`) stating the desired ward and any necessary precautions. The call out request is acknowledged, usually within a short period of time (`ACKNOWLEDGETIME`). When the patient is actually transferred out of the ICU, the `CALLOUT_OUTCOME` becomes 'Discharged' and the `OUTCOMETIME` column contains the time at which the patient was discharged.

## `SUBJECT_ID`, `HADM_ID`

`SUBJECT_ID` and `HADM_ID` define the patient and hospital admission corresponding to the given call out event.
? Unique

## `SUBMIT_WARDID`, `SUBMIT_CAREUNIT`

`SUBMIT_WARDID` identifies the ward from which the request was submitted. `SUBMIT_CAREUNIT` indicates whether the `SUBMIT_WARDID` corresponds an ICU cost center, and if so, what type of ICU cost center.

## `CURR_WARDID`, `CURR_CAREUNIT`

`CURR_WARDID` identifies the ward in which the patient resides when called out (i.e. prior to discharge/transfer). `CURR_CAREUNIT` indicates which ICU cost center the `CURR_WARDID` corresponds to (note: since all patients are being discharged from an ICU, all patients should reside in an ICU cost center).

## `CALLOUT_WARDID`, `CALLOUT_SERVICE`

`CALLOUT_WARDID` identifies the ward to which the patient should be discharged. Note that `CALLOUT_WARDID` = 0 represents 'Home' and `CALLOUT_WARDID` = 1 represents 'First available ward'. The remaining IDs correspond to distinct wards in the hospital. `CALLOUT_SERVICE` is the service under which the patient should be discharged to.


## `REQUEST_TELE`, `REQUEST_RESP`, `REQUEST_CDIFF`, `REQUEST_MRSA`, `REQUEST_VRE`

The request columns are binary indicators which request certain precautions for the patient in the subsequent ward where they will reside. For example, MRSA means that the patient is sensitive to MRSA, a drug resistant source of hospital acquired infections.

## `CALLOUT_STATUS`, `CALLOUT_OUTCOME`

`CALLOUT_STATUS` indicates whether the call out is still active or not: if a call out is answered it should be flagged as inactive. `CALLOUT_OUTCOME` is either 'Discharged' or 'Cancelled', indicating whether the patient finally called out (i.e. discharged) or not.

## `DISCHARGE_WARDID`

`DISCHARGE_WARDID` indicates the ward to which the patient was actually discharged. `DISCHARGE_WARDID` = 0 indicates home and other values correspond to distinct wards in the hospital.

## `ACKNOWLEDGE_STATUS`

`ACKNOWLEDGE_STATUS` indicates the response to the callout event: 'Acknowledged', 'Revised', 'Unacknowledged' or 'Reactivated'.

## `CREATETIME`, `UPDATETIME`, `ACKNOWLEDGETIME`, `OUTCOMETIME`, `FIRSTRESERVATIONTIME`, `CURRENTRESERVATIONTIME`

`CREATETIME` provides the time and date that the call out was initiated. `UPDATETIME` provides the last time at which the call out event was updated. `ACKNOWLEDGETIME` is the time at which the call out was first acknowledged.
`OUTCOMETIME` is the time at which the `CALLOUT_OUTCOME` occurred. `FIRSTRESERVATIONTIME` and `CURRENTRESERVATIONTIME` provide information regarding ward reservations.

# Important considerations

* Call out data is *not* available for all adult patients, as the data only began being collected part way through the collection of the MIMIC database
* Call out data is *never* available for neonates

