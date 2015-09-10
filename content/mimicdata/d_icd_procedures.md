+++
date = "2015-09-01T19:34:46-04:00"
title = "D_ICD_PROCEDURES"
linktitle = "D_ICD_PROCEDURES"
weight = 18
toc = "true"

[menu]
  [menu.main]
    parent = "MIMIC data"

+++

# Overview

**Table source:** Online sources.

**Table purpose:** Definition table for ICD procedures.

**Number of rows:** 3,882

**Links to:** 

* PROCEDURES_ICD on `CODE_ICD9`

# Table columns

Name | Postgres data type 
---- | ---- 
CODE\_ICD9 | VARCHAR(10)
SHORT\_TITLE | VARCHAR(50) 
LONG\_TITLE | VARCHAR(300)
	
# Detailed Description

## CODE_ICD9

`CODE_ICD9` is the International Coding Definitions Version 9 (ICD-9) code. Each code corresponds to a single procedural concept.

## `SHORT_TITLE`, `LONG_TITLE`

The title fields provide a brief definition for the given procedure code in `CODE_ICD9`.

# Important considerations