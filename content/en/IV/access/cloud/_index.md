---
title: "Cloud"
linktitle: "Cloud"
date: 2020-11-25
weight: 1
description: >
  Access MIMIC on the Cloud
---

MIMIC-III and MIMIC-IV are made available via Physionet: [MIMIC-III](https://physionet.org/content/mimiciii/), [MIMIC-IV](https://physionet.org/content/mimiciv/). Beyond directly downloading the dataset from PhysioNet, there are a few mechanisms for accessing the data:

* Accessing the data in BigQuery
* Accessing the data on AWS (MIMIC-III)
* Accessing the data in a Google Cloud storage bucket (MIMIC-IV)

We **highly** recommend using MIMIC in BigQuery for the following reasons:

* No setup required
* Updates will be integrated into BigQuery when they are available
* Derived concepts from the [MIMIC code repository](https://www.github.com/MIT-LCP/mimic-code) are precomputed and available on the `mimic_derived` dataset

If absolutely necessary, it is possible to download the data from a Google cloud bucket; instructions are provided at the end of the document.
Please do keep in mind that the PhysioNet team is covering the cost of downloading the dataset.

## Accessing data on the cloud

There are three steps to accessing data on the cloud:

1. Link your cloud account to your PhysioNet profile
2. Request access to the cloud resource
3. Log-in to the appropriate service and navigate to the resource

These steps assume you are already credentialed and have signed the data use agreement for MIMIC-IV.
If you have not, read this page for instructions on gaining access to [MIMIC-III](/iii/gettingstarted/cloud) or [MIMIC-IV](/iv/access).
