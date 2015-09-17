+++
date = "2015-09-01T19:34:46-04:00"
title = "D_ITEMS"
linktitle = "D_ITEMS"
weight = 19
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Definition table for all items in the ICU databases.

**Number of rows:** 15,492

**Links to:**

* CHARTEVENTS on `ITEMID`
* DATETIMEEVENTS on `ITEMID`
* IOEVENTS on `ITEMID`
* MICROBIOLOGYEVENTS on `ITEMID`

# Table columns

Name | Postgres data type 
---- | ---- 
ITEMID | INT
LABEL | VARCHAR(200)
ABBREVIATION | VARCHAR(100)
DBSOURCE | VARCHAR(20)
LINKSTO | VARCHAR(50)
CODE | VARCHAR(20)
CATEGORY | VARCHAR(100)
UNITNAME | VARCHAR(100)
PARAM\_TYPE | VARCHAR(30)
LOWNORMALVALUE | DOUBLE PRECISION
HIGHNORMALVALUE | DOUBLE PRECISION

# Detailed Description

The D_ITEMS table defines `ITEMID`, which represents measurements in the database. Measurements of the same type (e.g. heart rate) will have the same `ITEMID` (e.g. 211). The `ITEMID` column is an alternate primary key to this table: it is unique to each row. 

Note that the D_ITEMS table is sourced from two ICU databases: Metavision and CareVue. Each system had its own set of `ITEMID` to identify concepts. As a result, there are multiple `ITEMID` which correspond to the same concept. For CareVue data, `ITEMID` = 211 is used to identify heart rates, whereas for Metavision data, `ITEMID` = 220045 is used. All Metavision `ITEMID`s will have a value > 220000.

Note that the D\_ITEMS table does *not* link to the LABEVENTS table, as this data was acquired separately from the hospital database. The D\_ITEMS table was acquired from the ICU databases.

## `ITEMID`

As an alternate primary key to the table, `ITEMID` is unique to each row.

## `LABEL`, `ABBREVIATION`

The `LABEL` column describes the concept which is represented by the `ITEMID`. The `ABBREVIATION` column, only available in Metavision, lists a common abbreviation for the label.

## `DBSOURCE`

The `DBSOURCE` column was generated to clarify which database the given `ITEMID` was sourced from: 'carevue' indicates the `ITEMID` was sourced from CareVue, while 'metavision' indicated the `ITEMID` was sourced from Metavision. 

## `LINKSTO`

`LINKSTO` provides the table name which the data links to. For example, a value of 'chartevents' indicates that the `ITEMID` of the given row is contained in CHARTEVENTS. A single `ITEMID` is only used in one event table, that is, if an `ITEMID` is contained in CHARTEVENTS it will *not* be contained in any other event table (e.g. IOEVENTS, CHARTEVENTS, etc).

## `CODE`

`CODE` is a microbiology specific column used for identifying the organism tested again.

## `CATEGORY`

`CATEGORY` provides some information of the type of data the `ITEMID` corresponds to. Examples include 'ABG', which indicates the measurement is sourced from an arterial blood gas, 'IV Medication', which indicates that the medication is administered through an intravenous line, and so on.

## `UNITNAME`

`UNITNAME` specifies the unit of measurement used for the `ITEMID`. This column is not always available, and this may be because the unit of measurement varies, a unit of measurement does not make sense for the given data type, or the unit of measurement is simply missing. Note that there is sometimes additional information on the unit of measurement in the associated event table, e.g. the `UOM` column in CHARTEVENTS.

## `PARAM_TYPE`

`PARAM_TYPE` describes the type of data which is recorded: a date, a number or a text field.

## `LOWNORMALVALUE`, `HIGHNORMALVALUE`

`LOWNORMALVALUE` and `HIGHNORMALVALUE` provide a reference range for measurements which have a known operating range.

# Important considerations

* D_ITEMS is sourced from two *distinct* ICU databases. The main consequence is that there are duplicate `ITEMID` for each concept. For example, heart rate is captured both as an `ITEMID` of 212 (CareVue) and as an `ITEMID` of 220045 (Metavision). As a result, it is necessary to search for multiple `ITEMID` to capture a single concept across the entire database. This can be tedious, and it is an active project to coalesce these `ITEMID` - one which welcomes any and all help provided by the community!
* Another source of duplicate `ITEMID` is due to the free text nature of data entry in CareVue - as a result there are additional `ITEMID` which correspond to misspellings or synonymous descriptions of a single concept. It is important to search for all possible abbreviations and descriptions of a concept to capture all associated `ITEMID`.
