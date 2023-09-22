---
title: MIMIC-Fed documentation
linktitle: MIMIC-Fed
weight: 50

cascade:
- type: "docs"
  _target:
    path: "/**"
---
MIMIC-Fed is a large, freely avaliable federated COVID-rich ICU database comprising deidentified health-related data from Beth Israel Deaconess Medical Center (BIDMC) and Northwestern Memorial Health Center (NHMC) from 2020 to 2022. The federated database adopts a similar data structure as MIMIC-IV v2.2.

Notably, Northwestern Memorial Health Center (NHMC) uses the Epic electronic medical records (EMR) system. To make the EMR data available for research and quality assurance, the NM EMR systems transfer selected data into a relational Enterprise Data Warehouse (NM EDW). 

The NM EDW tables are categorized into two primary categories, Fact and Dimension, following data warehousing conventions. As implemented in the NM EDW, Fact tables primarily contain events (such as encounters, admissions, diagnosis events, procedure orders, and medication orders), while Dimension tables describe persistent attributes of entities (patients, procedure names, the medication formulary). 

The NM EDW also includes auxiliary tables not directly related to patient care, such as a list of International Classification of Disease codes (ICD-9 and ICD-10). In response to the COVID-19/SARS-COV-2 pandemic, a COVID-19 data mart was created within the EDW to provide convenient access to information on COVID-19 patients, lab results, medications and treatments.

MIMIC-Fed is currently organized into two distinct modules to highlight the source of the data:

- [hosp](/docs/mimic-nw/modules/hosp/) - Hospital level data including patients, admissions, labs, ICD diagnoses for billing purposes, prescriptions, and electronic medication administration records.
- [icu](/docs/mimic-nw/modules/icu/) - ICU level data including icu stays, procedure events, chartevents (vital signs). 

The tables structures adopted to align with MIMIC's data structure for each module are detailed in the respective sections.