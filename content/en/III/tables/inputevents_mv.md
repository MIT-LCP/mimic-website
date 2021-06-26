+++
date = "2015-09-01T19:34:46-04:00"
title = "The inputevents_mv table"
linktitle = "INPUTEVENTS_MV"
weight = 25
toc = "true"

+++

**Table source:** Metavision ICU databases.

**Table purpose:** Input data for patients.

**Number of rows:** 3,618,991

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* ICUSTAYS on `ICUSTAY_ID`
* D_ITEMS on `ITEMID`
* CAREGIVERS on `CGID`

A high level description of the data is available [here](/docs/iii/about/io).

# Important considerations

* A bolus will be listed as ending one minute after it started, i.e. `ENDTIME` = `STARTTIME` + 1 minute

# Table columns

Name | Postgres data type
---- | ----
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
ICUSTAY\_ID | INT
STARTTIME | TIMESTAMP(0)
ENDTIME | TIMESTAMP(0)
ITEMID | INT
AMOUNT | DOUBLE PRECISION
AMOUNTUOM | VARCHAR(30)
RATE | DOUBLE PRECISION
RATEUOM | VARCHAR(30)
STORETIME | TIMESTAMP(0)
CGID | BIGINT
ORDERID | BIGINT
LINKORDERID | BIGINT
ORDERCATEGORYNAME | VARCHAR(100)
SECONDARYORDERCATEGORYNAME | VARCHAR(100)
ORDERCOMPONENTTYPEDESCRIPTION | VARCHAR(200)
ORDERCATEGORYDESCRIPTION | VARCHAR(50)
PATIENTWEIGHT | DOUBLE PRECISION
TOTALAMOUNT | DOUBLE PRECISION
TOTALAMOUNTUOM | VARCHAR(50)
ISOPENBAG | SMALLINT
CONTINUEINNEXTDEPT | SMALLINT
CANCELREASON | SMALLINT
STATUSDESCRIPTION | VARCHAR(30)
COMMENTS\_STATUS | VARCHAR(30)
COMMENTS\_TITLE | VARCHAR(100)
COMMENTS\_DATE | TIMESTAMP(0)
ORIGINALAMOUNT | DOUBLE PRECISION
ORIGINALRATE | DOUBLE PRECISION

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`, `ICUSTAY_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient, `HADM_ID` is unique to a patient hospital stay and `ICUSTAY_ID` is unique to a patient ICU stay.

## `STARTTIME`, `ENDTIME`

`STARTTIME` and `ENDTIME` record the start and end time of an input/output event.

## ITEMID

Identifier for a single measurement type in the database. Each row associated with one `ITEMID` which corresponds to an instantiation of the same measurement (e.g. norepinephrine).
MetaVision `ITEMID` values are all above 220000. Since this data only contains data from MetaVision, it only contains `ITEMID` above 220000 (see [here](/docs/about/sources/metavision/) for details about MetaVision)

## AMOUNT, AMOUNTUOM

`AMOUNT` and `AMOUNTUOM` list the amount of a drug or substance administered to the patient either between the `STARTTIME` and `ENDTIME`.

## RATE, RATEUOM

`RATE` and `RATEUOM` list the rate at which the drug or substance was administered to the patient either between the `STARTTIME` and `ENDTIME`.

## STORETIME

`STORETIME` records the time at which an observation was manually input or manually validated by a member of the clinical staff.

## CGID

`CGID` is the identifier for the caregiver who validated the given measurement.

## ORDERID, LINKORDERID

`ORDERID` links multiple items contained in the same solution together. For example, when a solution of noradrenaline and normal saline is administered both noradrenaline and normal saline occur on distinct rows but will have the same `ORDERID`.

`LINKORDERID` links the same order across multiple instantiations: for example, if the rate of delivery for the solution with noradrenaline and normal saline is changed, two new rows which share the same new `ORDERID` will be generated, but the `LINKORDERID` will be the same.

## ORDERCATEGORYNAME, SECONDARYORDERCATEGORYNAME, ORDERCOMPONENTTYPEDESCRIPTION, ORDERCATEGORYDESCRIPTION

These columns provide higher level information about the order the medication/solution is a part of. Categories represent the type of administration, while the `ORDERCOMPONENTTYPEDESCRIPTION` describes the role of the substance in the solution (i.e. main order parameter, additive, or mixed solution)

## PATIENTWEIGHT

The patient weight in kilograms.

## TOTALAMOUNT, TOTALAMOUNTUOM

Intravenous administrations are usually given by hanging a bag of fluid at the bedside for continuous infusion over a certain period of time. These columns list the total amount of the fluid in the bag containing the solution.

## STATUSDESCRIPTION

```STATUSDESCRIPTION``` states the ultimate status of the item, or more specifically, row. It is used to indicate why the delivery of the compound has ended. There are only six possible statuses:

* Changed - The current delivery has ended as some aspect of it has changed (most frequently, the rate has been changed)
* Paused - The current delivery has been paused
* FinishedRunning - The delivery of the item has finished (most frequently, the bag containing the compound is empty)
* Stopped - The delivery of the item been terminated by the caregiver
* Rewritten - Incorrect information was input, and so the information in this row was rewritten (these rows are primarily useful for auditing purposes - the rates/amounts described were *not* delivered and so should not be used if determining what compounds a patient has received)
* Flushed - A line was flushed.

## ISOPENBAG

Whether the order was from an open bag.

## CONTINUEINNEXTDEPT

If the order ended on patient transfer, this field indicates if it continued into the next department (e.g. a floor).

## CANCELREASON

If the order was canceled, this column provides some explanation.

## COMMENTS\_STATUS, COMMENTS\_TITLE, COMMENTS_DATE

Specifies if the order was edited or canceled, and if so, the date and job title of the care giver who canceled or edited it.

## ORIGINALAMOUNT

Drugs are usually mixed within a solution and delivered continuously from the same bag. This column represents the amount of the drug contained in the bag at `STARTTIME`. For the first infusion of a new bag, `ORIGINALAMOUNT` = `TOTALAMOUNT`. Later on, if the rate is changed, then the amount of the drug in the bag will be lower (as some has been administered to the patient). As a result, `ORIGINALAMOUNT` < `TOTALAMOUNT`, and `ORIGINALAMOUNT` will be the amount of drug leftover in the bag at that `STARTTIME`.

## ORIGINALRATE

This is the rate that was input by the care provider. Note that this may differ from `RATE` because of various reasons: `ORIGINALRATE` was the original planned rate, while the `RATE` column will be the true rate delivered. For example, if a a bag is about to run out and the care giver decides to push the rest of the fluid, then `RATE` > `ORIGINALRATE`.
However, these two columns are usually the same, but have minor non-clinically significant differences due to rounding error.
