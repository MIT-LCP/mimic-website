+++
date = "2015-09-01T19:34:46-04:00"
title = "D_CPT"
linktitle = "D_CPT"
weight = 6
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++


# Overview

**Table source:** Online definitions.

**Table purpose:** High-level definitions for current procedural terminology (CPT) codes.

**Number of rows:** 134

**Links to:**

* CPTEVENTS on `CPT_CD` between `MINCODEINSUBSECTION` and `MAXCODEINSUBSECTION`

# Table columns

Name | Postgres data type
---- | --------
CATEGORY | SMALLINT
SECTIONRANGE | VARCHAR(100)
SECTIONHEADER | VARCHAR(50) 
SUBSECTIONRANGE | VARCHAR(100) 
SUBSECTIONHEADER | VARCHAR(300) 
CODESUFFIX | VARCHAR(5)
MINCODEINSUBSECTION | INT
MAXCODEINSUBSECTION | INT
	
# Detailed Description

`D_CPT` provides information about CPT codes, specifically it provides the overall purpose of the procedure and in some cases the body system related to the procedure. 

## CATEGORY

`CATEGORY` is a integer which identifies the category of the CPT code.

## `SECTIONRANGE`, `SECTIONHEADER`

`SECTIONRANGE` defines the range of codes for the given section, and `SECTIONHEADER` provides the description of the given section. There are 8 possible sections:

* Evaluation and management
* Surgery
* Radiology
* Anesthesia
* Emerging technology
* Pathology and laboratory
* Performance measurement
* Medicine

Note that the evaluation and management tends to represent administrative or generic costs.

## `SUBSECTIONRANGE`, `SUBSECTIONHEADER`

Similarly as for the sections, `SUBSECTIONRANGE` defines the range of codes for the given subsection, and `SUBSECTIONHEADER` provides the description of the given subsection. The subsection provides extra detail which can be useful, for example, when the section header is 'Anesthesia' the subsection provides information on the general anatomical region for the anesthesia.

## `MINCODEINSUBSECTION`, `MAXCODEINSUBSECTION`

These columns provide numeric representations of minimum and maximum value in the `SUBSECTIONRANGE` column. This facilitates joining the `CPTEVENTS` table to the `D_CPT` table on `CPT_CD`.

# Important considerations

* Unlike all other definition tables, `D_CPT` does *not* have a one to one mapping with the corresponding `CPT_CD` in `CPTEVENTS`, rather each row of `D_CPT` maps to a range of `CPT_CD`.
