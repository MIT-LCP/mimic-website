---
title: "d_labitems"
linktitle: "d_labitems"
weight: 1
date: 2020-08-10
description: >
  Dimension table for *labevents* provides a description of all lab items.
---

## *d_labitems*

*d_labitems* contains definitions for all `itemid` associated with lab measurements in the MIMIC database. All data in *labevents* link to the *d_labitems* table. Each unique (`fluid`, `category`, `label`) tuple in the hospital database was assigned an `itemid` in this table, and the use of this `itemid` facilitates efficient storage and querying of the data.

Laboratory data contains information collected and recorded in the hospital laboratory database. This includes measurements made in wards within the hospital and clinics outside the hospital. Most concepts in this table have been mapped to LOINC codes, an openly available ontology which facilitates interoperability.

### Links to

* *labevents* on `itemid`

## Important considerations

This table used to contain a column called `loinc_code`, which stored standardized identifiers for laboratory measurements. To support ongoing improvement of these labels, the assignment of LOINC codes is now done in the [MIMIC Code Repository](https://www.github.com/MIT-LCP/mimic-code).

## Table columns

Name | Postgres data type
---- | ----
`itemid` | INTEGER
`label` | VARCHAR(50)
`fluid` | VARCHAR(50)
`category` | VARCHAR(50)

## Detailed Description

### `itemid`

A unique identifier for a laboratory concept. `itemid` is unique to each row, and can be used to identify data in labevents associated with a specific concept.

### `label`

The `label` column describes the concept which is represented by the `itemid`.

### `fluid`

`fluid` describes the substance on which the measurement was made. For example, chemistry measurements are frequently performed on blood, which is listed in this column as 'BLOOD'. Many of these measurements are also acquirable on other fluids, such as urine, and this column differentiates these distinct concepts.

### `category`

`category` provides higher level information as to the type of measurement. For example, a category of 'ABG' indicates that the measurement is an arterial blood gas.
