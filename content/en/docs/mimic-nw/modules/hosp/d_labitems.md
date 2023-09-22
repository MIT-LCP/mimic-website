---
title: "d_labitems"
linktitle: "d_labitems"
weight: 4
date: 2023-09-18
description: >
  Dimension table for *labevents* provides a description of all lab items.
---

## *d_labitems*

*d_labitems* contains definitions for all `itemid` associated with lab measurements in the MIMIC database. All data in *labevents* link to the *d_labitems* table. Each unique (`fluid`, `category`, `label`) tuple in the hospital database was assigned an `itemid` in this table, and the use of this `itemid` facilitates efficient storage and querying of the data.

Laboratory data contains information collected and recorded in the hospital laboratory database. This includes measurements made in wards within the hospital and clinics outside the hospital. Most concepts in this table have been mapped to LOINC codes, an openly available ontology which facilitates interoperability.

For the data sourced from NHMC, Illinois law defines certain categories of information as Sensitive Protected Health Information (SPHI) which require special treatment. SPHI includes genetic counseling but does not include genetic testing.

To facilitate further federation processes, the lab mappings to standard terminologies (LOINC)  will be released.

### Links to

* *labevents* on `itemid`

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

We provide a list of common COVID-19 tests and measurements in the database, as defined by LOINC terminology, below:

- SARS-CoV-2 (COVID-19) [Presence] in Specimen by Organism specific culture
- SARS-CoV-2 (COVID-19) Ag [Presence] in Respiratory specimen by Rapid immunoassay
- SARS-CoV-2 (COVID-19) N gene [Cycle Threshold #] in Specimen by NAA with probe detection
- SARS-CoV-2 (COVID-19) E gene [Cycle Threshold #] in Respiratory specimen by NAA with probe detection


### `fluid`

`fluid` describes the substance on which the measurement was made. These include blood, cerebrospinal fluid, joint fluid, ascites, urine and other body fluid.

### `category`

`category` provides higher level information as to the type of measurement. These categories include hematology, chemistry, and blood gas. For example, a category of 'ABG' indicates that the measurement is an arterial blood gas. 
