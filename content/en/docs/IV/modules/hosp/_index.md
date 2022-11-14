---
title: "Hosp"
linkTitle: "Hosp"
date: 2020-08-10
weight: 20
description: >
  The Hosp module provides all data acquired from the hospital wide electronic health record. Information covered includes patient and admission information, laboratory measurements, microbiology, medication administration, and billed diagnoses.
---

The hosp module contains data derived from the hospital wide EHR. These measurements are predominantly recorded during the hospital stay, though some tables include data from outside the hospital as well (e.g. outpatient laboratory tests in labevents).
Information includes patient and admission details (patients, admissions, transfers), laboratory measurements (labevents, d_labitems), microbiology cultures (microbiologyevents), provider orders (poe, poe_detail), medication administration (emar, emar_detail), medication prescription (prescriptions, pharmacy), hospital billing information (diagnoses_icd, d_icd_diagnoses, procedures_icd, d_icd_procedures, hcpcsevents, d_hcpcs, drgcodes), and hospital service related information (services).
