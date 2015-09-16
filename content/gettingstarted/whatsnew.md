+++
date = "2015-09-01T13:37:00-04:00"
title = "MIMIC II to MIMIC III"
linktitle = "MIMIC II to MIMIC III"
weight = 3
toc = "true"

[menu]
  [menu.main]
    parent = "Getting started"

+++

# MIMIC II vs MIMIC III

Many users familiar with MIMIC II will be happy to find MIMIC III has a very similar architecture, however there are key differences to be aware of.
MIMIC III is an extension of MIMIC II: it incorporates the data contained in MIMIC II (collected between 2001 - 2008) and augments it with newly collected data between 2008 - 2012. Further to this, many data elements have been re-extracted in a more robust manner to improve the quality of the underlying data. A key difficulty in the addition of new data was a change in data management software which occurred at the Beth Israel Deaconess Medical Center (BIDMC): the original CareVue data management system (which archived data from 2001 - 2008) was replaced with the new Metavision data management system (which continues to be used to the present). Many efforts have been made to merge these databases seamlessly: this has been successful in some instances, and continues to be a work in progress for others. This page aims to facilitate the transition for researchers familiar with MIMIC II who would like to continue their research with the updated MIMIC III.

# New tables

## CALLOUT

## PROCEDURES_ICD


# Schema changes

## ADMISSIONS


## CENSUSEVENTS replaced by TRANSFERS

The CENSUSEVENTS table was used in MIMIC II to track patient hospital admissions. The original source of this table was the ICU database which recorded when patients were admitted and discharged from the ICU. In MIMIC III, this table has been removed and replaced with the TRANSFERS table. The TRANSFERS table is sourced from the hospital admission, discharge, transfer (ADT) data. This has a number of advantages:

 - The ADT data tracks a patient throughout the *entire* hospital stay, providing greater granularity and easier tracking of a patient's hospital course
 - The ADT data provides information regarding ward location
 - The ADT data has fewer erroneous admissions: frequently the ICU database contained erroneous entries corresponding to accidental admission/discharges
 - The ADT data is available for all patients in the ICU database


## D_CHARTITEMS, D_IOITEMS and D_MEDITEMS merged into D_ITEMS 

## DEMOGRAPHIC_DETAIL merged into ADMISSIONS

The DEMOGRAPHIC_DETAIL provided extra static information regarding a patient which rarely changed throughout an admission (e.g. age, ethnicity). This data was originally sourced from the ICU database. The new ADMISSIONS table is sourced entirely from the hospital database, and contained the same set of demographics. Instead of creating a new table for this demographics, it was decided to maintain the demographics within the ADMISSIONS table in the same format as it exists in the raw data.

## DRGEVENTS renamed DRGCODES

The DRGEVENTS table has been renamed DRGCODES. The table still corresponds to diagnostic related groups, however the clarity of the data has been improved. First, a column corresponding to the DRG system has been provided. Second, if available, additional information regarding the DRG severity and mortality risk have been added. Finally, the DRG code has been mapped to a description based upon the underlying version. Due to frequent updates in the DRG coding system, it is non-trivial to map DRG codes to a description. To ease the use of this data, each DRG code has been mapped to a free text description which has been added to the table.

## ICD9 renamed DIAGNOSES_ICD

To clarify the content of the table, the ICD9 table has been renamed to DIAGNOSES_ICD. The table contains diagnoses sourced from the hospital databased codified by ICD, usually ICD-9.

## IOEVENTS, ADDITIVES, DELIVERIES and MEDEVENTS merged into IOEVENTS

The data in IOEVENTS and MEDEVENTS has been merged into the IOEVENTS table. As all the medications in the MEDEVENTS table were continuous infusions, they were all associated with an entry in IOEVENTS. MEDEVENTS would specify the drug rate, while IOEVENTS would specify the volume given. These tables have been consolidated to ease querying for drug deliveries.

## POE_MED_ORDER and POE_DRUG_ORDER merged into PRESCRIPTIONS

The term POE, or provider order entry, is vague and references a hospital specific database which users may not be familiar with. To clarify the content of these tables, they have been merged into a single table named PRESCRIPTIONS.

# Table changes

## IOEVENTS

The IOEVENTS contains a large number of columns which were not present in the table of the same name in MIMIC II. This is due to two reasons: the drastically different storage methodology used in the Metavision database, and the merging of many tables in CareVue into the single IOEVENTS table. Due to the complicated merging undertaken and the importance of the IOEVENTS table, the methodology has been detailed in its own section.

# Identifier changes

## `SUBJECT_ID`, `HADM_ID` and `ICUSTAY_ID`

`SUBJECT_ID` between MIMIC II v2.6 and MIMIC III have been kept consistent, for example, `SUBJECT_ID` 788 is corresponds to the same patient in MIMIC II v2.6 as it does in MIMIC III.

`HADM_ID` have been regenerated in MIMIC III. `HADM_ID` in MIMIC II v2.6 will *not* match any `HADM_ID` in MIMIC III. The newly generated `HADM_ID` range from 100,000 - 199,999 to help differentiate these IDs from others.

`ICUSTAY_ID` have been regenerated in MIMIC III. `ICUSTAY_ID` in MIMIC II v2.6 will *not* match any `ICUSTAY_ID` in MIMIC III. Note that the newly generated `ICUSTAY_IF` range between 200,000 - 299,999 to prevent confusion with other IDs.

<!--
## `ITEMID`, `IOITEMID`

There were multiple `ITEMID` in the MIMIC II database which caused confusion. Particularly, the IOEVENTS table contained an `ITEMID` and an `IOITEMID`. Each concept now has a unique `ITEMID` with differing ranges.

-->

<!-- 

 
# Detailed changelog

# Primary changes at a glance

 - `HADM_ID` and `ICUSTAY_ID` have been regenerated for *all* patients, `SUBJECT_ID` has not changed
 - `CENSUSEVENTS` has been rehauled:
 	- The table is now referred to as `TRANSFERS`
 	- The data now includes all out of ICU activity, and covers patient ward visits for their entire hospital stay
 - `ADMISSIONS` and `TRANSFERS` are now sourced entirely from the hospital admission database (they were previously sourced from the ICU database)
 - `DEMOGRAPHIC_DETAIL` has been merged into `ADMISSIONS`
 
 - A number of duplicate `SUBJECT_ID` contained in MIMIC II have been coalesced
 - All `ICUSTAY_ID` have a corresponding `HADM_ID`
 - All `HADM_ID` have a corresponding `SUBJECT_ID`
 - Hospital admission dates now have times
 - Hospital discharge disposition is now available in a structured form
 
The comparison of patients, admissions, and icustays between v2.6 and v3.0 is listed below:

Table name (Primary key column) | Count (MIMIC2 v2.6)
--------- | --------- | --------- 
```D_Patients``` (```subject_id```) | 32,536
```Admissions``` (```hadm_id```) | 36,095
```ICUStayEvents``` (```icustay_id```) | 40,426 

-->
