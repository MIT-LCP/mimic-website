---
title: "d_items"
linktitle: "d_items"
weight: 2
date: 2023-09-18
description: >
  Dimension table describing itemid. Defines concepts recorded in the events table in the ICU module.
---

**Links to:** 

* *chartevents* on `itemid`
* *procedureevents* on `itemid`

# Table columns

Name | Postgres data type
---- | ----
itemid | INTEGER
label | VARCHAR(200)
abbreviation | VARCHAR(100)
linksto | VARCHAR(50)
category | VARCHAR(100)
unitname | VARCHAR(100)
param\_type | VARCHAR(30)
lownormalvalue | FLOAT
highnormalvalue | FLOAT

# Detailed Description

The *d_items* table defines `itemid`, which represents measurements in the database. Measurements of the same type (e.g. heart rate) will have the same `itemid` (e.g. 220045). Values in the `itemid` column are unique to each row. All `itemid`s will have a value > 220000.

To faciliate future federation processes, we will release mappings within charted events (including vital signs) to standard terminologies (LOINC) and mappings for procedure events to standard terminologies (SNOMED).


We provide a list of common vital sign labels in the database, as defined by LOINC terminology, below:

- Heart rate	
- Respiratory rate
- Oxygen saturation in Arterial blood by Pulse oximetry	

We provide a list of common procedure labels in the database, as defined by SNOMED terminology, below:

- Plain chest X-ray	
- Invasive ventilation	
- Noninvasive ventilation	

### `itemid`

As an alternate primary key to the table, `itemid` is unique to each row.

### `label`

The `label` column describes the concept which is represented by the `itemid`. 

###  `abbreviation`

The `abbreviation` column, lists a common abbreviation for the label.

### `linksto`

`linksto` provides the table name which the data links to. For example, a value of 'chartevents' indicates that the `itemid` of the given row is contained in CHARTEVENTS. A single `itemid` is only used in one event table, that is, if an `itemid` is contained in CHARTEVENTS it will *not* be contained in any other event table (e.g. *procedureevents*, etc).

### `category`

`category` provides some information of the type of data the `itemid` corresponds to. Examples include 'ABG', which indicates the measurement is sourced from an arterial blood gas, 'IV Medication', which indicates that the medication is administered through an intravenous line, and so on.

### `unitname`

`unitname` specifies the unit of measurement used for the `itemid`. This column is not always available, and this may be because the unit of measurement varies, a unit of measurement does not make sense for the given data type, or the unit of measurement is simply missing. Note that there is sometimes additional information on the unit of measurement in the associated event table, e.g. the `valueuom` column in *chartevents*.

### `param_type`

`param_type` describes the type of data which is recorded: a date, a number or a text field.

### `lownormalvalue`, `highnormalvalue`

These columns store reference ranges for the measurement. Note that a reference range encompasses the *expected* value of a measurement: values outside of this may still be physiologically plausible, but are considered unusual.