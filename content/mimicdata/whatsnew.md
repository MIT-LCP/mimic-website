+++
date = "2015-09-01T13:37:00-04:00"
title = "MIMIC-II to MIMIC-III"
linktitle = "MIMIC-II to MIMIC-III"
weight = 2
toc = "true"

[menu]
  [menu.main]
    parent = "Data details"

+++

# MIMIC-II vs MIMIC-III

MIMIC-III is an extension of MIMIC-II: it incorporates the data contained in MIMIC-II (collected between 2001 - 2008) and augments it with newly collected data between 2008 - 2012. In addition, many data elements have been regenerated from the raw data in a more robust manner to improve the quality of the underlying data.

One of the challenges of adding new data resulted from a change in data management software at the Beth Israel Deaconess Medical Center. The original Philips CareVue system (which archived data from 2001 - 2008) was replaced with the new Metavision data management system (which continues to be used to the present). This page aims to facilitate the transition for researchers familiar with MIMIC-II who would like to continue their research with the updated MIMIC-III.

# Lab ITEMID mapping

The `ITEMID` for laboratory measurements in the D_LABITEMS and LABEVENTS tables in MIMIC-II do *not* match the `ITEMID` for laboratory measurements in MIMIC-III. For previous users' benefit, we have provided a mapping table to facilitate the updating of queries which use this table. This mapping can be found at the GitHub repository dedicated to sharing mimic-code:

https://github.com/MIT-LCP/mimic-code/blob/master/migrating/labid.csv

Furthermore, note that much of the data has been mapped to LOINC codes. LOINC codes are advantageous as they provide an ontology for recorded lab values. However, careful inspection shows that the LOINC code for an `ITEMID` in MIMIC-III is, in rare occassions, different from the LOINC code for the same concept in MIMIC-II. This is usually attributable to the laboratory assigning a new LOINC code, which is done for many reasons, including changing the reagents of a laboratory test, changing the technique used to acquire the result or because the previous LOINC code was made redundant.

# Schema changes

## ADMISSIONS



## CENSUSEVENTS replaced by TRANSFERS

The CENSUSEVENTS table was used in MIMIC-II to track patient hospital admissions. The original source of this table was the ICU database which recorded when patients were admitted and discharged from the ICU. In MIMIC-III, this table has been removed and replaced with the TRANSFERS table. The TRANSFERS table is sourced from the hospital admission, discharge, transfer (ADT) data. This has a number of advantages:

 - The ADT data tracks a patient throughout the *entire* hospital stay, providing greater granularity and easier tracking of a patient's hospital course
 - The ADT data provides information regarding ward location
 - The ADT data has fewer erroneous admissions: frequently the ICU database contained erroneous entries corresponding to accidental admission/discharges
 - The ADT data is available for all patients in the ICU database


## D_CHARTITEMS, D_IOITEMS and D_MEDITEMS merged into D_ITEMS

D_CHARTITEMS, D_IOITEMS, and D_MEDITEMS were all sourced from the same data source: the ICU database (specfically Philips CareVue). In contrast, iMDSoft Metavision only has a single table to define most `ITEMID` concepts. In order to simplify the schema and coalesce the databases, it was decided to merge together all the `ITEMID` dictionary tables into a single table, *except* D_LABITEMS. D_LABITEMS was kept separate as the laboratory data is sourced from the hospital database.

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

The IOEVENTS contains a large number of columns which were not present in the table of the same name in MIMIC-II. This is due to two reasons: the drastically different storage methodology used in the Metavision database, and the merging of many tables in CareVue into the single IOEVENTS table. Due to the complicated merging undertaken and the importance of the IOEVENTS table, the methodology has been detailed in its own section [here](mimicdata/ioevents).

# Identifier changes

## `SUBJECT_ID`, `HADM_ID` and `ICUSTAY_ID`

`SUBJECT_ID` between MIMIC-II v2.6 and MIMIC-III have been kept consistent, for example, `SUBJECT_ID` 788 is corresponds to the same patient in MIMIC-II v2.6 as it does in MIMIC-III.

`HADM_ID` have been regenerated in MIMIC-III. `HADM_ID` in MIMIC-II v2.6 will *not* match any `HADM_ID` in MIMIC-III. The newly generated `HADM_ID` range from 100,000 - 199,999 to help differentiate these IDs from others.

`ICUSTAY_ID` have been regenerated in MIMIC-III. `ICUSTAY_ID` in MIMIC-II v2.6 will *not* match any `ICUSTAY_ID` in MIMIC-III. Note that the newly generated `ICUSTAY_IF` range between 200,000 - 299,999 to prevent confusion with other IDs.


# New tables

## CALLOUT

The CALLOUT table contains information about ICU discharge planning and execution. Each patient is "called out" of the ICU: which involves alerting hospital administrative staff that a bed, usually on the floor, is required for a patient currently in the ICU. The call out event also includes any precautions that the patient may require (such as susceptibility to MRSA or respiratory support). The table provides information both on when the patient was deemed ready for discharge and when the patient actually left the ICU.

## PROCEDURES_ICD



# Removed tables

There were many tables in MIMIC-II which are no longer present in MIMIC-III. In most cases, these tables were generated from the raw data for user convenience. We have transitioned from the approach of creating flat files of these tables to providing the source code necessary to regenerate them. This has two advantages: first it is much more efficient in terms of data transfer, and second it clarifies that these data are not "raw" in that they are not acquired directly from the databases but rather synthesized views of this data.

# COMORBIDITY_SCORES

This table is frequently used to define the comorbid status for patients. Code for generating this table will be provided in the GitHub repository. The comorbidities will be defined using ICD-9 codes and DRG codes as proposed by Elixhauser et al.

# DEMOGRAPHICEVENTS, D_DEMOGRAPHICITEMS

These tables were specific to the older CareVue database. As these tables are not present in the Metavision data, and the same information has been acquired from the hospital database (see the ADMISSIONS and D\_PATIENTS tables), these tables have been removed.

# D_CAREUNITS

The care unit identifier, CUID, has been removed from the various tables as it was unavailable in the Metavision ICU database. Care unit can be ascertained at the patient level, rather than the observation level, using the ICUSTAYEVENTS and TRANSFERS table.

# D_CODEDITEMS

This was a generated table to facilitate the interpretation of various coding systems, including microbiology, DRG, etc. The database has been restructured to have explicit definitions for these codes where appropriate, and so this table was made redundant.

# D_PARAMMAP_ITEMS

This table is no longer needed as all `ITEMID` concepts have been consolidated in D_ITEMS.

# ICUSTAY_DAYS

This table was used in the generation of severity scores which were originally imputed into the raw data. The table is no longer necessary as the severity scores are no longer imputed into the database.

# ICUSTAY_DETAILS

A script to generate ICUSTAY_DETAILS will be provided on the GitHub repository shortly.

# PARAMETER_MAPPING

This table is no longer needed as all `ITEMID` concepts have been consolidated in D_ITEMS.

# WAVEFORM_*, D_WAVEFORM_SIGNALS

D\_WAVEFORM\_SIGNALS, WAVEFORM\_METADATA, WAVEFORM\_SEGMENTS, WAVEFORM\_SEG\_SIG, WAVEFORM\_SIGNALS, WAVEFORM\_TRENDS, WAVEFORM\_TREND\_SIGNALS have been removed.
The mapping to the waveform data is no longer provided within the relative database for clarity.

<!--
## `ITEMID`, `IOITEMID`

There were multiple `ITEMID` in the MIMIC-II database which caused confusion. Particularly, the IOEVENTS table contained an `ITEMID` and an `IOITEMID`. Each concept now has a unique `ITEMID` with differing ranges.

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

 - A number of duplicate `SUBJECT_ID` contained in MIMIC-II have been coalesced
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
