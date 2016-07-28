+++
date = "2015-09-01T19:34:46-04:00"
title = "SERVICES"
linktitle = "SERVICES"
weight = 34
toc = "true"

[menu]
  [menu.main]
    parent = "Tables in MIMIC"

+++

# Overview

**Table source:** Hospital database.

**Table purpose:** Lists services that a patient was admitted/transferred under.

**Number of rows:** 73,343

**Links to:**

* PATIENTS on `SUBJECT_ID`
* ADMISSIONS on `HADM_ID`

# Brief summary

The services table describes the service that a patient was admitted under. While a patient can be physicially located at a given ICU type (say MICU), they are not necessarily being cared for by the team which staffs the MICU. This can happen due to a number of reasons, including bed shortage. The SERVICES table should be used if interested in identifying the type of service a patient is receiving in the hospital. For example, if interested in identifying surgical patients, the recommended method is searching for patients admitted under a surgical service.

Each service is listed in the table as an abbreviation - this is exactly how the data is stored in the hospital database. For user convenience, we have provided a description of each service type.

Service | Description
--- | ---
CMED | Cardiac Medical - for non-surgical cardiac related admissions
CSURG | Cardiac Surgery - for surgical cardiac admissions
DENT | Dental - for dental/jaw related admissions
ENT | Ear, nose, and throat - conditions primarily affecting these areas
GU | Genitourinary - reproductive organs/urinary system
GYN | Gynecological - female reproductive systems and breasts
MED | Medical - general service for internal medicine
NB | Newborn - infants born at the hospital
NBB | Newborn baby - infants born at the hospital
NMED | Neurologic Medical - non-surgical, relating to the brain
NSURG | Neurologic Surgical - surgical, relating to the brain
OBS | Observation - not ill enough for a service but kept in hospital for observation
ORTHO | Orthopaedic - surgical, relating to the musculoskeletal system
OMED | Orthopaedic medicine - non-surgical, relating to musculoskeletal system
PSURG | Plastic - restortation/reconstruction of the human body (including cosmetic or aesthetic)
PSYCH | Psychiatric - mental disorders relating to mood, behaviour, cognition, or perceptions
SURG | Surgical - general surgical service not classified elsewhere
TRAUM | Trauma - injury or damage caused by physical harm from an external source
TSURG | Thoracic Surgical - surgery on the thorax, located between the neck and the abdomen
VSURG | Vascular Surgical - surgery relating to the circulatory system

<!-- # Important considerations -->

# Table columns

Name | Postgres data type
---- | ----
SUBJECT\_ID | INT
HADM\_ID | INT
TRANSFERTIME | TIMESTAMP(0)
PREV\_SERVICE | VARCHAR(20)
CURR\_SERVICE | VARCHAR(20)

# Detailed Description

## `SUBJECT_ID`, `HADM_ID`

Identifiers which specify the patient: `SUBJECT_ID` is unique to a patient and `HADM_ID` is unique to a patient hospital stay.

## `TRANSFERTIME`

`TRANSFERTIME` is the time at which the patient moved from the `PREV_SERVICE` (if present) to the `CURR_SERVICE`.

## `PREV_SERVICE`, `CURR_SERVICE`

`PREV_SERVICE` and `CURR_SERVICE` are the previous and current service that the patient resides under.
