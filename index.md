---
title: Medical Information Mart for Intensive Care
layout: default
nav_exclude: true
---

# Medical Information Mart for Intensive Care

Freely available medical data for research.

[Documentation](/docs/){: .btn .btn-primary .mr-2 }
[Getting Started](/docs/gettingstarted/){: .btn .mr-2 }
[Code](https://github.com/MIT-LCP/mimic-code/){: .btn .mr-2 }

---

MIMIC-IV is separated into "modules" to reflect the provenance of the data.

## MIMIC-IV-Hosp

The Hosp module provides all data acquired from the hospital wide electronic health record.
This includes laboratory measurements, microbiology cultures, medication information, services provided, billed diagnoses and procedures, and so on.

[Hosp documentation](/docs/iv/modules/hosp/){: .btn .btn-outline }

## MIMIC-IV-ICU

The ICU module contains information collected from the clinical information system used within the ICU.
This includes highly granular information such as hour-to-hour vital signs, information about fluid management, and other charted observations.

[ICU documentation](/docs/iv/modules/icu/){: .btn .btn-outline }

## MIMIC-IV-ED

The ED module contains data for emergency department patients including a triage assessment, nurse-validated vital signs, medicine reconciliation, and treatment information.

[ED documentation](/docs/iv/modules/ed/){: .btn .btn-outline }

## MIMIC-IV-CXR

MIMIC-CXR provides chest x-ray images and radiology reports for a subset of patients admitted to the emergency department.

[CXR documentation](/docs/iv/modules/cxr/){: .btn .btn-outline }

## MIMIC-IV-Note

The Note module contains deidentified free-text clinical notes for hospitalized patients.

[Note documentation](/docs/iv/modules/note/){: .btn .btn-outline }

## MIMIC-III

MIMIC-III is an older version of MIMIC. It contains an older group of patients (ending in 2012), and a subset of the ICU and hospital information available in MIMIC-IV.
We highly recommend researchers starting new studies to use the above modules in MIMIC-IV.
We will maintain MIMIC-III for a short period to allow researchers to transition.

[MIMIC-III documentation](/docs/iii/){: .btn .btn-outline }
