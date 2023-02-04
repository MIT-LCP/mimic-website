---
title: "hpcsevents"
linktitle: "hcpcsevents"
weight: 1
date: 2020-08-10
description: >
  Billed events occurring during the hospitalization. Includes CPT codes.
---

## *hcpcsevents*

## Links to

* *d_hcpcs* on hcpcs_cd

<!--

# Important considerations

-->

## Table columns

Name | Postgres data type
---- | ----
`subject_id` | INTEGER NOT NULL
`hadm_id` | INTEGER NOT NULL
`chartdate` | DATE
`hcpcs_cd` | CHAR(5) NOT NULL
`seq_num` | INTEGER NOT NULL
`short_description` | VARCHAR(180)

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

### `hadm_id`

{{% include "/static/include/hadm_id.md" %}}

### `chartdate`

The date associated with the coded event.

### `hcpcs_cd`

A five character code which uniquely represents the event.
Link this to `code` in *d_hcpcs* for a longer description of the code.

### `seq_num`

An assigned order to HCPCS codes for an individual hospitalization. This order sometimes conveys meaning, e.g. sometimes higher priority, but this is not guaranteed across all codes.

### `short_description`

A short textual descriptions of the `hcpcs_cd` listed for the given row.
