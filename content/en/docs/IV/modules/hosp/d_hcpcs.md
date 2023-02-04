---
title: "d_hcpcs"
linktitle: "d_hcpcs"
weight: 1
date: 2020-08-10
description: >
  Dimension table for *hcpcsevents*; provides a description of CPT codes.
---

## The *d_hcpcs* table

The *d_hcpcs* table is used to acquire human readable definitions for the codes used in the *hcpcsevents* table. The concepts primarily correspond to hospital billing, and are mostly CPT codes. Unfortunately due to licensing restrictions not all code definitions are available.

### Links to

* *hcpcsevents* on `code`

<!--

# Important considerations

-->

## Table columns

Name | Postgres data type
---- | ----
`code` | CHAR(5) NOT NULL
`category` | SMALLINT
`long_description` | TEXT
`short_description` | VARCHAR(180)

## Detailed description

### `code`

A five character code which uniquely represents the event.

### `category`

Broad classification of the code.

### `long_description`, `short_description`

Textual descriptions of the `code` listed for the given row.
