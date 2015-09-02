+++
date = "2015-09-01T07:32:25-04:00"
draft = true
title = "d_items"

+++

# Overview

Table source: CareVue and Metavision ICU databases.
Table purpose: Definition table for all items in the ICU databases.
Number of rows: 15,492
Links to: 
* CHARTEVENTS on `ITEMID`
* DATETIMEEVENTS on `ITEMID`
* IOEVENTS on `ITEMID`
* MICROBIOLOGYEVENTS on `ITEMID`

# Table columns

	ITEMID INT, 
	LABEL VARCHAR(200), 
	ABBREVIATION VARCHAR(100), 
	DBSOURCE VARCHAR(20), 
	LINKSTO VARCHAR(50), 
	CODE VARCHAR(20), 
	CATEGORY VARCHAR(100), 
	UNITNAME VARCHAR(100), 
	PARAM_TYPE VARCHAR(30), 
	LOWNORMALVALUE DOUBLE PRECISION, 
	HIGHNORMALVALUE DOUBLE PRECISION
	
# Detailed Description

The `D_ITEMS` table defines `ITEMID`, which represents measurements in the database. Measurements of the same type (e.g. heart rate) will have the same `ITEMID` (e.g. 211). The `ITEMID` column is an alternate primary key to this table: it is unique to each row. 

Note that the `D_ITEMS` table is sourced from two ICU databases: Metavision and CareVue. Each system had its own set of `ITEMID` to identify concepts. As a result, there are multiple `ITEMID` which correspond to the same concept. For CareVue data, `ITEMID` = 211 is used to identify heart rates, whereas for Metavision data, `ITEMID` = 220045 is used. All Metavision `ITEMID` will have a value > 220000.

## `ITEMID`

As an alternate primary key to the table, `ITEMID` is unique to each row.

## `LABEL`, `ABBREVIATION`

The `LABEL` column describes the concept which is represented by the `ITEMID`. The `ABBREVIATION` column, only available in Metavision, lists a common abbreviation for the label.

## `DBSOURCE`

The `DBSOURCE` column was generated to clarify which database the given `ITEMID` was sourced from: 'carevue' indicates the `ITEMID` was sourced from CareVue, while 'metavision' indicated the `ITEMID` was sourced from Metavision. 

## `LINKSTO`

## `CODE`

## `CATEGORY`

## `UNITNAME`

## `PARAM_TYPE`

## `LOWNORMALVALUE`, `HIGHNORMALVALUE`

# Important considerations

