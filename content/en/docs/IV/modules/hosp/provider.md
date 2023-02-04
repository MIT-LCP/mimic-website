---
title: "provider table"
linktitle: "provider"
date: 2023-02-03
weight: 1
description: >
  The provider table lists deidentified provider identifiers used in the database.
---

## *provider*

A description table for providers in the database referenced by *provider_id*.
As of MIMIC-IV v2.2, this table simply lists all unique `provider_id` in the database.

Note that most tables contain a prefix before `provider_id`. All columns with a suffix link to `provider_id`, including:

* `admit_provider_id`
* `enter_provider_id`
* `order_provider_id`

## Table columns

Name | Postgres data type
---- | ----
provider_id | VARCHAR(10) NOT NULL

### `provider_id`

`provider_id` lists all possible identifiers for providers used throughout the database.
{{% include "/static/include/provider_id.md" %}}
