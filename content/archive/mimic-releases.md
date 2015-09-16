+++
date = "2015-09-01T19:09:50-04:00"
title = "MIMIC II releases"
linktitle = "MIMIC II releases"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Archive"

+++

# Releases

List of previous releases:
http://mimic.physionet.org/database/releases.html

# MIMIC II v2.6

## Changelog

- Merge the last year of the ISM database

The last year of ISM, through September 2008, has been added, including indications of matches to waveforms.

- New dateshifts

We have given all subjects a new, random dateshift.

- Add overall SOFA score as total of each organ system's score

The individual-system SOFA scores are in CHARTEVENTS, with itemids 20002 through 20007; a new itemid, 20009, has been added, and it s for the total score. The relevant columns in ICUSTAY\_DETAIL (sofa\_first, sofa\_min, sofa\_max) indicate this total score.

- Add a column to ICUSTAY\_DETAIL indicating number of matched waveforms

A new column, matched\_waveforms\_num, has been added to ICUSTAY\_DETAIL; it gives the number of waveforms matched to the patient.

- Add waveform statistics

Basic waveform statistics and metadata have been added to the database; these are essentially the organized output of what one would see by running the WFDB utility wfdbdesc (over all of the
waveforms).

- Add LOINC codes for hospital labs

D\_LABITEMS contains two new columns, loinc\_code and loinc\_description, giving the LOINC codes and descriptions respectively.

- Add diagnosis-related groups (DRGs)

A new table, DRGEVENTS, maps subject IDs and hospital-admission IDs to DRG itemids, which are defined in D\_CODEDITEMS.

- Add procedures

PROCEDUREEVENTS contains indications of procedures performed on patients, for given hospital-admission IDs. The itemids for procedures are defined in D\_CODEDITEMS. Exact times for procedures
are not given; however, their dates are given in the proc\_dt column, and the order in which a patient's procedures are performed, for a given day, are indicated by consecutive numbers (integers) in the sequence\_num column.

- Add demographic information

DEMOGRAPHICEVENTS contains indications of marital status, type and source of admission, ethnicity, overall payor group, and religion as recorded for each patient upon admission to the hospital. The
definitions of the itemids are given in D\_CODEDITEMS.

- Add microbiology information

MICROBIOLOGYEVENTS contains information on microbiology tests performed on patients: specimen, organism, and antibacterium are indicate in the spec\_itemid, org\_itemid, and ab\_itemid columns
respectively; these itemids are defined in D\_CODEDITEMS.

- Remove duplicate mappings of waveform case IDs to subject IDs in PARAMETER\_MAPPING

- Fix the icustay\_expire\_flg in ICUSTAY\_DETAIL

icustay\_expire\_flg indicates whether the given patient died during the given ICU stay. For some patients, this column was 'Y' for all of his/her ICU stays, rather than just the last; this has been fixed.

- Fix case of hospital admission ID not unique to subject ID

Hospital admission 15449 was mapped to two different patients; this has been fixed.

- Add Exlihauser comorbidity scores

The Exlihauser comorbidity scores (calculated from DRG and ICD-9 codes) can be found in COMORBIDITY\_SCORES

## Known limitations, bugs.

- Missing data

Newly added data: DRGs, Demographics, Microbiology tests and procedures were not available for all subjects. Therefore, you will find that this data is missing for some subjects.

We were unable to complete the import of some of the text
data. Radiology, Echo and ECG reports are missing from NOTEEVENTS.


- Waveform dates

The waveform metadata contains dates from the current waveforms available on PhysioNet:

http://physionet.org/physiobank/database/mimic2db/

The dates found here will not match those found elsewhere in the
database.


# MIMIC II v2.5

## Changelog

Major changes since version 2.4 :

- Date of death after hospital discharge

Patients have been matched against the Social Security death tapes, and the date of death has been imported into MIMIC II.  For patients who died in the hospital, their respective dates of discharge were used as their dates of death. Two additional columns have been added to the D\_PATIENTS table:

- DOD                            = Date of Death
- HOSPITAL\_EXPIRE\_FLG  = Whether or not the patient deid in the hospital

The column EXPIRE\_FLG in the ADMISSION table has been removed.

- New Waveform case ID matches

A first round of waveforms with up to 8 simultaneous channels have been matched to SUBJECT\_IDs. The matches can be found in the PARAMETER\_MAPPING table where CATEGORY is "SUBJECT\_ID\_TO\_CASE\_ID", the columns PARAM1\_NUM (for the SUBJECT\_ID) and PARAM2\_STR (for the waveform case ID).

- Merge NOTEEVENTS into REPORTEVENTS

REPORTEVENTS has been merged into NOTEEVENTS. Categories have been extracted into D\_REPORTITEMS, with the ITEMID column as the foreign key, but not completely; the D\_* tables will be combined into a complete dictionary in a later release.

- New ICUSTAY\_DAYS materialized view

The ICUSTAY\_DAYS materialized view was added to divide each ICU stays into daily periods. This greatly helps computation of cumulative queries.

- Daily SOFA scores

New entries in D\_CHARTITEMS were added to represent SOFA scores (itemid = 20002), and corresponding scores were added in CHARTEVENTS.

- Daily SAPS I calculations

For each ICU stay, a daily SAPS I was added into the CHARTEVENTS table, with ITEMID 20001.

- Add a view for summarizing the D\_CHARTITEMS table

It was somewhat troublesome for users of the database to collect statistics for the parameters (ITEMIDs) in D\_CHARTITEMS. Therefore, a summarizing materialized view, D\_CHARTITEMS\_DETAIL, was added as a first introduction of all charted parameters; it describes how many patients each parameter was charted from, and various statistics such as min., max., and average.

- Clean "value1" and "value2" columns in CHARTEVENTS for numeric itemids

Some ITEMIDs in the CHARTEVENTS table that are supposed to be only numeric (such as ABP, HR) had repeated values in columns VALUE1/VALUE2 (which are VARCHAR columns) and VALUE1NUM/VALUE2NUM (NUMBER columns); VALUE1 and VALUE2 were cleaned accordingly.

- Reorganized ICUSTAY\_DETAIL materialized view

The ICUSTAY\_DETAIL view has been used as a key component in  many of computation for several researches. We added/changed some columns to reflect:

- EXPIRE\_FLG                 = Flag to indicate if the paitent is dead, either in the hospital or after discharge
- HOSPITAL\_EXPIRE\_FLG = If the patient deid in the hospital
- ICUSTAY\_EXPIRE\_FLG   = If the patient deid in the ICU
- HEIGHT                       = Patient height
- WEIGHT\_FIRST            = The first measured weight for the patient in the ICU stay 
- WEIGHT\_MIN               = The minimum weight for the ICU stay
- WEIGHT\_MAX              = The maximum weight for the ICU stay
- SAPSI\_FIRST               = The first measured SAPS-I score for the patient in the ICU stay 
- SAPSI\_MIN                  = The minimum SAPS-I score for the ICU stay
- SAPSI\_MAX                 = The maximum SAPS-I score for the ICU stay
- SOFA\_FIRST                = The first measured SOFA score for the patient in the ICU stay 
- SOFA\_MIN                   = The minimum SOFA score for the ICU stay
- SOFA\_MAX                  = The maximum SOFA score for the ICU stay

- Add an ICUSTAY\_ID column to all event tables

To facilitate queries and other computations, the ICUSTAY\_ID column has been added to event tables: CHARTEVENTS, IOEVENTS, MEDEVENTS, LABEVENTS and TOTALBALEVENTS.

- Clean duplicates in D\_CAREUNITS

There were duplicate names in the table D\_CAREUNITS that needed to be merged, and their foreign keys updated.

- Remove entries from item tables which contain no records in event tables

292 unused rows have been removed from D\_MEDITEMS; 3544 from D\_CHARTITEMS.

- Fix problems with duplicate hospital admissions

Six patients had hospital admissions with overlapping admission-to-discharge date intervals. These were fixed by examining the discharge summaries.

- Add missing foreign key for POE\_ORDER

For POE\_ORDER, columns SUBJECT\_ID and HADM\_ID were properly made to be foreign keys for the tables D\_PATIENTS and ADMISSIONS, respectively.

## Database statistics (adult records summary)

 | N* | #cases** (%unit) | mean ±std | median | IQR (Q1,Q3)
---- | ---- | ---- | ---- | ---- | ---- 
Hospital admissions | 22,870 | | | |
ICU Stays | 25,328 | | | |
Age (years) | 25,328 | | 63.3 ±17.7 | 65.20 | 26.1 (51.3,77.4)
Gender (male) | 25,328 | 14,259 (56.3%) | | | 
ICU Los (days) | 25,328 | | 4.7 ±11 | 2.20 | 3.3 (1.1,4.4)
Hospital Los (days) | 22,870 | | 10.7 ±13 | 7.00 | 9 (4,13)
SAPS I - day 1 *** | 20,142 | | 13.4 ±5.3 | 13.00 | 7 (10,17)
Mechanical ventilation | 25,328 | 11,969 (47.3%) | | | 
Invasive Swan-Ganz hemodynamic monitoring | 25,328 | 5,637 (22.3%) | | | 
Invasive arterial blood pressure monitoring | 25,328 | 14,054 (55.5%) | | | 
Use of vaso-active medications | 25,328 | 8,693 (34.3%) | | | 
Hospital mortality | 22,870 | 2,666 (11.7%) | | | 

\* N = The number of ICUStays or Hospitalizations. that were included in the calculation for the given ICU Unit.

** #cases = The number of ICUStays orHospitalizations that match the category criteria. For example: In Gender, #cases will be the number of male ICUStays in a unit.

*** Only ICUStays where they have all 14 SAPS parameters were included

# MIMIC II v2.4

## Changelog

- Bug #5: Fix problems with icustay generation
- Bug #13: Fix in "Unknown" service type in icustay\_detail
- Bug #21: Rename ORDER column in PARAMETER\_MAPPING table
- Bug #26: Make event date fields consistent
- Bug #27: Rename d\_labitems.lab\_category to category for consistency with other item tables
- Bug #40: Modify SAPS I calculation to correctly account for ventilated patients
- Feature #11: Delete the materialized view VITAL\_SIGNS\_RAW, because this was just a temporal data  to  be used by some statistics calculations.
- Feature #12: Add indices on cgid, itemid to chartevents
- Feature #14: Add AKI materialized view
- Feature #15: Add organ system failure materialized view
- Feature #16: Restore the Physionet 2009 challenge patients
- Feature #34: Re-generate SAPS scores after fixing Icustay problems
- Change request #36: Make the "Length Of Stay" columns consistent in minutes
- Change request #37: Replace ICUSTAY materialized view with ICUSTAYEVENTS table
- Change request #38: Make consistent some column names in ICUSTAY_DETAIL


## Database statistics (adult records summary)


 | N* | #cases** (%unit) | mean ±std | median | IQR (Q1,Q3)
---- | ---- | ---- | ---- | ---- | ----
Hospital admissions | 22,870 | | | | 
ICU Stays | 25,328 | | | | 
Age (years) | 25,328 | | 63.3 ±17.7 | 65.20 | 26.1 (51.3,77.4)
Gender (male) | 25,328 | 14,259 (56.3%) |  |  |  | 
ICU Los (days) | 25,328 | |  4.7 ±11 | 2.20 | 3.3 (1.1,4.4)
Hospital Los (days) | 22,870 | |  10.7 ±13 | 7.00 | 9 (4,13)
SAPS I - day 1 *** | 20,142 | |  13.4 ±5.3 | 13.00 | 7 (10,17)
SAPS I - day 2 *** | 13,495 | |  11.8 ±4.6 | 11.00 | 6 (9,15)
SAPS I - day 3 *** | 9,070 | |  12.2 ±4.5 | 12.00 | 6 (9,15)
Mechanical ventilation | 25,328 | 11,969 (47.3%) | | | 
Invasive Swan-Ganz hemodynamic monitoring | 25,328 | 5,637 (22.3%) | | |
Invasive arterial blood pressure monitoring | 25,328 | 14,054 (55.5%) | | |
Use of vaso-active medications | 25,328 | 8,693 (34.3%) | | |
Hospital mortality | 22,870 | 2,666 (11.7%) | | |

\* N = The number of ICUStays or Hospitalizations. that were included in the calculation for the given ICU Unit.

** #cases = The number of ICUStays orHospitalizations that match the category criteria. For example: In Gender, #cases will be the number of male ICUStays in a unit.

*** Only ICUStays where they have all 14 SAPS parameters were included. 2nd and 3rd day data comes from version 2.5 of the database.
