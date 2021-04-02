+++
date = "2015-09-01T19:33:17-04:00"
title = "Release notes"
linktitle = "Releases of MIMIC-III"
weight = 2
toc = "true"

+++

This page lists the current version of MIMIC-III, and all previous versions which have existed, in sequential, reverse chronological order. Each version will address a finite set of updates which are tracked using a unique issue number, usually of the form #100, #101, etc.

Note that the changes between MIMIC-II and MIMIC-III are not listed here, due to the large number of differences between the databases. A separate document has been provided for that purpose [here](/iii/mimicdata/whatsnew). The release notes for MIMIC-II versions is available [here](/iii/archive/mimic-releases).

# Current version

The current version of the database is v1.4. When referencing this version, we recommend using the full title: MIMIC-III v1.4.

## MIMIC-III v1.4


MIMIC-III v1.4 was released on 2 September 2016. It was a major release enhancing data quality and providing a large amount of additional data for Metavision patients.  

Issues addressed include:  

* #88 - Text data sourced from drop down menus or "pick lists" has been added to the database for Metavision patients. Users interested in the exact concepts added can query them as follows:  
    `select * from d_items  `  
    `where linksto = 'chartevents'`  
    `and dbsource = 'metavision'`   
    `and param_type = 'Text'`.  
All data was added to the `chartevents` table, increasing the raw (uncompressed) size of the datafile by 5 GB.  
* #201 - Data in tables may now only occur within 1 year of a patient's hospital admission `admittime` and `dischtime`. Observations outside this range corresponded to typographical errors in the `charttime`, and this unreliable data has been removed.  
* #197 - A small issue where a single observation was duplicated and assigned to two `icustay_id` (and sometimes two `hadm_id`) has been corrected: this affected 37 `icustay_id` and 80 `hadm_id`. Thanks @matteobonvini on GitHub for the report.  
* #191 - A subset of patients were missing data due to the transition from CareVue to Metavision: this data has been restored.  
* #193 - Some laboratory concepts (particularly CD counts) were conflated (i.e. percentages mixed with counts) - these have been corrected. Thanks Yuqi Si for the report (via StackExchange).  
* #196 - The `amount` column in `inputevents_mv` did not correspond to `amountuom` (unit of measurement) - instead it corresponded to a "base" unit (e.g. grams instead of milligrams). Data in the `amount` has been updated to match the `amountuom` where appropriate. This also effected the `procedureevents_mv` table. Thanks @ngageorange on GitHub for the report.  
* #198 - NULL values for character fields are now properly represented in the CSV file as empty fields with no double quotes. Database systems such as PostgreSQL will now recognize these fields as null when copying with the NULL '' qualifier.  
* #199 - Addendums to discharge summaries in the notes can now be distinguished in the `noteevents` table: their `category` has remained 'Discharge summary', but their description has been changed from 'Report' to 'Addendum'  
* #194 - The LOINC code for Total CO2 has been corrected (was 1959-6 total bicarb, is now 34728-6 total CO2)  
* #186 - Data has been harmonized into EST.  
* #180 - Some patients were erroneously labelled as in care unit `TSICU`: these have been corrected to `CSRU`  
* #189 - Schema change: The `has_ioevents_data` column in `admissions` has been removed as it was no longer meaningful.  
* #185 - Three text concepts (GCS, code status, RASS) had a null `linksto` field in `d_items`, even though the data existed in `chartevents`. This has been corrected. Note these were the only three text concepts available for Metavision patients in MIMIC-III v1.3 (see #88).  
* #60 - The date shift for dates in the `text` field of `noteevents` has been corrected: before it corresponded to a different date shifted used in MIMIC-II (easily identifiable by years occurring between 2500-3500). It now matches the dates in the structured data.  
* #188 - Negative microbiology cultures are now recorded in `micriobiologyevents` - negative cultures can be identified by a NULL value for the organism name (`org_name`).  

Be sure to validate the checksum of the resultant file to ensure you have the correct version.

# Past versions  

This section lists past versions in reverse chronological order.


## MIMIC-III v1.3

MIMIC-III v1.3 was released on 10 December 2015. It was a minor release enhancing the consistency of the dataset.

Issues addressed include:

* #175 - A new value for ```DRG_VERSION``` was added to the `DRGCODES` table to clarify why the same code matched to multiple descriptions.
* #174 - The ```EDTIMEOUT``` column was renamed to ```EDOUTTIME``` in the `ADMISSIONS` table for consistency with other timestamp columns.
* #173 - The `UOM` column was renamed to `VALUEUOM` in the `CHARTEVENTS`, `DATETIMEEVENTS`, and `LABEVENTS` tables for consistency with other `UOM` columns.
* #172, #177 - Several careunit acronyms were merged in the `TRANSFERS` and `ICUSTAYS` tables for ease of interpretation.
* #168 - A set of `ITEMID`s in the `INPUTEVENTS_CV` table were inappropriately low (<30000), they have no been corrected.
* #167 - Duplicate radiology reports were removed from the `NOTEEVENTS` table. These duplicates were present in the raw data.
* #166 - The `DBSOURCE` column was corrected from Metavision to CareVue for a set of patients in the `TRANSFERS` and `ICUSTAYS` tables.


## MIMIC-III v1.2

MIMIC-III v1.2 was released on 10 November 2015. MIMIC-III v1.2 was a major release providing both bug fixes and a large amount of additional data.

Major issues addressed, including additional data made available:

* #130 and #135 - Duplicate data in various events tables with `CGID` has been removed
* #132 - Hospital expire flag was in the wrong table - now moved to `ADMISSIONS` table. `EXPIRE_FLAG` added to `PATIENTS` table.
* #137 - The `ITEMID` for input/output items has been properly shifted to range between 30000-40000. Previously it incorrectly ranged between 1-5000, and as a result did not match the dictionary entries in `D_ITEMS`.
* #141 - `CHARTTIME` and `STORETIME` have been added to `NOTEEVENTS`, if available. No times were available for ECG and echo reports (only the date).
* #144 - Dates of birth for patients > 89 are now shifted by 300 years for clarity.
* #151 - The time of emergency department registration and exit has been added to the admissions table, where available.
* #154 - A new table, `PROCEDUREEVENTS_MV`, has been added. This table contains information regarding the start and stop time for various procedures for Metavision patients. Procedures include x-rays, ventilation, dialysis, and others.
* #158 - The `IOEVENTS` table has been split into three tables: `INPUTEVENTS_CV` (CareVue patients only), `INPUTEVENTS_MV` (Metavision patients only), and `OUTPUTEVENTS` (all patients).
* #162 - 5,795,842 rows of data corresponding to yes/no answers have been added for Metavision patients
* #164 - 10,140 rows of "Non Iv meds" (e.g. vancomycin) have been added for Metavision patients

Minor issues addressed:

* #126 - `ROW_ID`, `CGID`, `ORDERID` and `LINKORDERID` now stored as `INT` instead of `BIGINT`
* #134 - The CR/LF characters which prefixed notes in `NOTEEVENTS` have been removed
* #136 - The `VOLUME` column in the events tables for inputs has been changed to `AMOUNT`
* #139 - The units for certain solution volumes, erroneously recorded as rate units, have been corrected
* #140 - The `ORIGINALAMOUNT` column no longer exists for rows with drug rates, only with drug volumes
* #148 - Removed `RECORD_ID` from `NOTEEVENTS` as it was redundant
* #149 - `ICUSTAYEVENTS` has been renamed `ICUSTAYS`
* #152 - The `STARTTIME` and `ENDTIME` columns have been renamed `STARTDATE` and `ENDDATE` for the `PRESCRIPTIONS` table to reflect the lack of time information.
* #155 - `LINKSTO` column in `D_ITEMS` has been corrected: now correctly refers to `PROCEDUREEVENTS_MV`, `INPUTEVENTS_MV`, `INPUTEVENTS_CV`, and `OUTPUTEVENTS`.
* #156 - The `SEQUENCE` column in `DIAGNOSES_ICD` and `PROCEDURES_ICD` has been renamed `SEQ_NUM`.
* #159 - A `CONCEPTID` column has been added to D_ITEMS for future ontology mapping/data harmonization.
* #163 - The `CODE` column has been removed from `MICROBIOLOGYEVENTS` and `D_ITEMS` as it was redundant to `ITEMID`

## MIMIC-III v1.1

MIMIC-III v1.1 was released on 24 September 2015. It was primarily a bug fix release, and addresses the following issues:

* #116 - `CGID` was incorrect in the `DATETIMEEVENTS`, `CHARTEVENTS`, `IOEVENTS` and `NOTEEVENTS` tables. It has now been corrected.
* #117 - `VALUENUM` for GCS verbal response measurements has been corrected for Metavision (it was offset by -1).
* #118 - `VALUENUM` for all GCS measurements in CareVue is no longer null, and contains the appropriate value in the scale.
* #120 - `DOD` was incorrectly set to `DOB` - this has been fixed.
* #121 - IOEVENTS contained incorrect units for certain drugs (sometimes the unit was a rate when the actual observation was an amount, e.g. listed as "mcgkgmin" when it should have been "mg").
* #122 - `DBSOURCE` in the `TRANSFERS` and `ICUSTAYEVENTS` tables has been corrected - originally it only contained 'metavision' when a patient was in the ICU, so the same patient would be listed as 'carevue' when out of the ICU and 'metavision' when inside the ICU.
* #123 - Precision in the `IOEVENTS` table has been fixed at 10 decimal places.

## MIMIC-III v1.0

MIMIC-III v1.0 was released on 25 August 2015. It was a preliminary version and not widely publicized to allow for internal testing. As this was the first release of the database, and the successor of the MIMIC-II database, no changes are listed here. An overview of changes between MIMIC-II and MIMIC-III is provided [here](/iii/mimicdata/whatsnew).
