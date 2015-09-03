+++
date = "2015-09-01T19:34:46-04:00"
title = "D_ICD_diagnoses"
linktitle = "D_ICD_diagnoses"
weight = 7
toc = "true"

[menu]
  [menu.main]
    parent = "Table detail"

+++

# Overview

Table source: Online sources.
Table purpose: Definition table for ICD diagnoses.
Number of rows: 14,567
Links to: 
* DIAGNOSES_ICD ON `CODE_ICD9`

# Table columns

	CODE_ICD9 VARCHAR(10), 
	SHORT_TITLE VARCHAR(50), 
	LONG_TITLE VARCHAR(300)

# Detailed Description

## CODE_ICD9

`CODE_ICD9` is the International Coding Definitions Version 9 (ICD-9) code. Each code corresponds to a single diagnostic concept.

## `SHORT_TITLE`, `LONG_TITLE`

The title fields provide a brief definition for the given diagnosis code in `CODE_ICD9`.

# Important considerations