+++
date = "2015-09-01T19:34:46-04:00"
title = "MICROBIOLOGYEVENTS"
linktitle = "MICROBIOLOGYEVENTS"
weight = 27
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# The microbiologyevents table

**Table source:** Hospital database.

**Table purpose:** Contains microbiology information, including tests performed and sensitivities.

**Number of rows:** 631,726

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`
* D\_ITEMS on `SPEC_ITEMID`
* D\_ITEMS on `ORG_ITEMID`
* D\_ITEMS on `AB_ITEMID`

# Important considerations

* If the organism is null, then the culture had no growth reported.

# Table columns

Name | Postgres data type
---- | ----
ROW\_ID | INT
SUBJECT\_ID | INT
HADM\_ID | INT
CHARTDATE | TIMESTAMP(0)
CHARTTIME | TIMESTAMP(0)
SPEC\_ITEMID | INT
SPEC\_TYPE\_DESC | VARCHAR(100)
ORG\_ITEMID | INT
ORG\_NAME | VARCHAR(100)
ISOLATE\_NUM | SMALLINT
AB\_ITEMID | INT
AB\_NAME | VARCHAR(30)
DILUTION\_TEXT | VARCHAR(10)
DILUTION\_COMPARISON | VARCHAR(20)
DILUTION\_VALUE | DOUBLE PRECISION
INTERPRETATION | VARCHAR(5)

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `CHARTDATE`, `CHARTTIME`

`CHARTTIME` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured.
`CHARTDATE` is the same as `CHARTTIME`, except there is no time available.

`CHARTDATE` was included as time information is not always available for microbiology measurements: in order to be clear about when this occurs, `CHARTTIME` is null, and `CHARTDATE` contains the date of the measurement.

In the cases where both `CHARTTIME` and `CHARTDATE` exists, `CHARTDATE` is equal to a truncated version of `CHARTTIME` (i.e. `CHARTTIME` without the timing information). Not all observations have a `CHARTTIME`, but all observations have a `CHARTDATE`.

## `SPEC_ITEMID`, `SPEC_TYPE_DESC`

Specimen which is tested for bacterial growth.

## `ORG_ITEMID`, `ORG_NAME`

The organism, if any, which grew when tested. If NULL, no organism grew (i.e. negative culture).

## `ISOLATE_NUM`

For testing antibiotics, the isolated colony (integer; starts at 1).

## `AB_ITEMID`, `AB_NAME`

If an antibiotic was tested against the given organism for sensitivity, the name is listed here.

## `DILUTION_TEXT`, `DILUTION_COMPARISON`, `DILUTION_VALUE`

Dilution values when testing antibiotic sensitivity.

## `INTERPRETATION`

`INTERPRETATION` of the antibiotic sensitivity, and indicates the results of the test. "S" is sensitive, "R" is resistant, "I" is intermediate, and "P" is pending.
