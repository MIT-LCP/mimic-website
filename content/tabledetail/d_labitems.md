+++
date = "2015-09-01T19:34:46-04:00"
title = "D_LABITEMS"
linktitle = "D_LABITEMS"
weight = 10
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Definition table for all laboratory measurements.

**Number of rows:** 755

**Links to:** 

* LABEVENTS on `ITEMID`

# Table columns

Name | Postgres data type 
---- | ---- 
ITEMID | INT
LABEL | VARCHAR(100) 
FLUID | VARCHAR(100)
CATEGORY | VARCHAR(100)
LOINC_CODE | VARCHAR(100)
	
# Detailed Description

`D_LABITEMS` contains definitions for all `ITEMID` associated with lab measurements in the MIMIC database. All data in LABEVENTS link to the D\_LABITEMS table. Each unique `LABEL` in the hospital database was assigned an `ITEMID` in this table, and the use of this `ITEMID` facilitates efficient storage and querying of the data. Note that lab items are kept separate while most definitions are contained in the D_ITEMS table, and there were good reasons to keep the lab items separate. As the laboratory data is acquired from the hospital database, the data is consistent across all years in the database. Consequently, there is usually only one `ITEMID` associated with each concept in the database (e.g. only `ITEMID`, ???, is used for the Troponin-I measurement). Furthermore, the data contains information collected in departments outside the ICU. This includes both wards within the hospital and clinics outside the hospital. Most concepts in this table have been mapped to LOINC codes, an openly available ontology which provides a rich amount of information about the laboratory measurement including reference ranges, common units of measurement and other further detail regarding the measurement.

## `ITEMID`

As an alternate primary key to the table, `ITEMID` is unique to each row.

## `LABEL`

The `LABEL` column describes the concept which is represented by the `ITEMID`.

## `FLUID`

`FLUID` describes the substance on which the measurement was made. For example, chemistry measurements are frequently performed on blood, which is listed in this column as 'BLOOD'. Many of these measurements are also acquirable on other fluids, such as urine, and this column differentiates these distinct concepts.

## `CATEGORY`

`CATEGORY` provides higher level information as to the type of measurement. For example, a category of 'ABG' indicates that the measurement is an arterial blood gas.

## `LOINC_CODE`

`LOINC_CODE` contains the LOINC code associated with the given `ITEMID`. LOINC is an ontology which originally specified laboratory measurements but has since expanded to cover a wide range of clinically relevant concepts. LOINC openly provide a table which contains a large amount of detail about each LOINC code. This table is freely available online or can be provided by the guardians of the database.

# Important considerations

* The `ITEMID` from MIMIC III v1.0 does *not* match the `ITEMID` from MIMIC II v2.6. If a mapping between the two is necessary, please contact the guardians of the database.
* Many of the LOINC codes were assigned during a project to standardize the ontology of lab measurements in the MIMIC database. Consequently, the codes were assigned post-hoc, and may not be present for every lab measurement. We welcome improvements to the present codes or assignment of LOINC codes to unmapped data elements from the community.