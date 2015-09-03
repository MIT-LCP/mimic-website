+++
date = "2015-09-01T19:34:46-04:00"
title = "Caregivers"
linktitle = "Caregivers"
weight = 3
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"
+++


# Overview

**Table source:** CareVue and Metavision ICU databases.

**Table purpose:** Defines the role of caregivers.

**Number of rows:** 8221

**Links to:** 
* CHARTEVENTS on `CGID`

# Table columns

ROW\_ID
CGID
LABEL
DESCRIPTION

# Detailed Description

The CAREGIVERS table provides information regarding the type of caregiver. Each caregiver is represented by a unique integer which maps to this table.

## `CGID`

`CGID` is a unique identifier for each distinct caregiver present in the database. `CGID` is sourced from two tables in the raw data: the CareVue and Metavision ICU databases. Due to imprecision in the storage of unique identifiers across the database, it is possible that two distinct caregivers (e.g. RN Susan Jones and RN Sarah Jones) would be considered as the same caregiver. However, this is an unlikely occurrence.

## `LABEL`

`LABEL` defines the type of caregiver: e.g. RN, MD, PharmD, etc. Note that `LABEL` is a free text field and as such contains many typographical errors and spelling variants of the same concept (e.g. MD, MDs, M.D.).

## `DESCRIPTION`

`DESCRIPTION` is less frequently present than `LABEL`, and provides additional information regarding the caregiver. This column is much more structured, and contains only 17 unique values as of MIMIC III v1.0.
