---
title: "MIMIC-Northwestern documentation"
linktitle: Multi-center
weight: 45

cascade:
- type: "docs"
  _target:
    path: "/**"

description: >
  MIMIC-Northwestern: A Harmonized Multi-center COVID-rich ICU Database
---
We introduce MIMIC-Northwestern, a large harmonized multi-center COVID-rich ICU database. It  comprises deidentified health-related data from Beth Israel Deaconess Medical Center (BIDMC) and Northwestern Memorial HealthCare (NMHC) spanning 2020 to 2022, capturing the data distribution shifts during this critical period. The database adopts a similar data structure as MIMIC-IV v2.2.

Notably, Northwestern Memorial HealthCare (NMHC) uses the Epic electronic medical records (EMR) system. To make the EMR data available for research and quality assurance, the NM EMR systems transfer selected data into a relational Enterprise Data Warehouse (NM EDW). 

The NM EDW tables are categorized into two primary categories, Fact and Dimension, following data warehousing conventions. As implemented in the NM EDW, Fact tables primarily contain events (such as encounters, admissions, diagnosis events, procedure orders, and medication orders), while Dimension tables describe persistent attributes of entities (patients, procedure names, the medication formulary). 

The NM EDW also includes auxiliary tables not directly related to patient care, such as a list of International Classification of Disease codes (ICD-9 and ICD-10). In response to the COVID-19/SARS-COV-2 pandemic, a COVID-19 data mart was created within the EDW to provide convenient access to information on COVID-19 patients, lab results, medications and treatments.

The MIMIC-Northwestern database is currently organized into two distinct modules to highlight the source of the data:

- [Hosp](/docs/mimic-northwestern/modules/hosp/) - Hospital level data including patients, admissions, labs, ICD diagnoses for billing purposes, prescriptions, and electronic medication administration records.
- [ICU](/docs/mimic-northwestern/modules/icu/) - ICU level data including icu stays, procedure events, chartevents (vital signs). 

{{% pageinfo %}}
The MIMIC-Northwestern database is not yet released and its structure is subject to change.
{{% /pageinfo %}}

The tables structures adopted to align with MIMIC's data structure for each module are detailed in the respective sections. Additionally, we have incorporated COVID-related concepts and standard terminologies (LOINC, RxNorm, SNOMED, ICD-9/10) and derived mappings (for drug administration) into the dataset. This integration not only facilitates current multi-center initiatives, but also facilities interoperability, allowing for seamless data exchange and collaboration across healthcare systems.
