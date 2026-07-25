---
title: Your first MIMIC query
layout: default
nav_order: 5
parent: Tutorials
grand_parent: MIMIC-IV
description: A walkthrough of writing your first SQL queries against MIMIC-IV, covering patient counts, demographics, and joining the admissions table.
---

# Your first MIMIC query
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

Learn how to write your first query against the MIMIC-IV database. This tutorial assumes you have already gained access to MIMIC data.

## Prerequisites

- Access to MIMIC data (see [Getting Started](/docs/gettingstarted/))
- Basic SQL knowledge
- Access to a query environment (BigQuery, PostgreSQL, etc.)

## Understanding the basic structure

MIMIC-IV is organized into modules. Let's start with the most fundamental table: `patients` in the `hosp` module.

### The patients table

The `patients` table contains basic demographic information. Each row corresponds to a single patient, identified by their `subject_id`.

{% include subject_id.md %}

## Your first query

Let's count how many patients are in the database:

```sql
SELECT COUNT(*) AS total_patients
FROM `physionet-data.mimiciv_hosp.patients`;
```

{: .note }
> This example uses BigQuery syntax. Adjust the table name format for your platform.

### Expected result

You should see roughly 300,000+ patients in MIMIC-IV.

## Exploring patient demographics

Let's look at the gender distribution:

```sql
SELECT
    gender,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM `physionet-data.mimiciv_hosp.patients`
GROUP BY gender
ORDER BY count DESC;
```

## Adding hospital admissions

Now let's join with the `admissions` table to see admission patterns:

```sql
SELECT
    p.gender,
    COUNT(DISTINCT a.hadm_id) AS total_admissions,
    COUNT(DISTINCT p.subject_id) AS unique_patients,
    ROUND(COUNT(DISTINCT a.hadm_id) / COUNT(DISTINCT p.subject_id), 2) AS avg_admissions_per_patient
FROM `physionet-data.mimiciv_hosp.patients` p
JOIN `physionet-data.mimiciv_hosp.admissions` a
    ON p.subject_id = a.subject_id
GROUP BY p.gender;
```

### Key concepts

- {% include subject_id.md %}
- {% include hadm_id.md %}

## Next steps

Now that you've run your first queries:

1. **Explore other tables** - Try querying [ICU stays](/docs/iv/modules/icu/icustays/)
2. **Learn the schema** - Review the [schema overview](/docs/iv/about/schema-overview/)
3. **Try BigQuery** - Read the longer [BigQuery tutorial](/docs/iv/tutorials/bigquery/)

## Common issues

### Query timeout
If your query times out, try adding `LIMIT 1000` to test on a smaller dataset first.

### Permission errors
Ensure you've properly signed the data use agreement for the modules you're querying.

### Different platforms
- **PostgreSQL**: Remove backticks and use `schema.table` format
- **AWS**: Use appropriate S3 bucket references
- **Local**: Adjust paths to your local database

---

{: .highlight }
> **Well done!** You've successfully run your first MIMIC queries. Understanding these basic patterns will help you tackle more complex analyses.
