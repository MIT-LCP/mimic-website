---
title: MIMIC-IV documentation
linktitle: MIMIC-IV
weight: 50

cascade:
- type: "docs"
  _target:
    path: "/**"
---

MIMIC-IV is a relational database containing real hospital stays for patients admitted to a tertiary academic medical center in Boston, MA, USA. MIMIC-IV contains comprehensive information for each patient while they were in the hospital: laboratory measurements, medications administered, vital signs documented, and so on.
The database is intended to support a wide variety of research in healthcare.
MIMIC-IV builds upon the success of [MIMIC-III](/docs/iii), and incorporates numerous improvements over MIMIC-III.

MIMIC-IV is separated into "modules" to reflect the provenance of the data. There are currently five modules:

- [core](/docs/iv/modules/core) - patient stay information (i.e. admissions and transfers)
- [hosp](/docs/iv/modules/hosp) - hospital level data for patients: labs, micro, and electronic medication administration
- [icu](/docs/iv/modules/icu) - ICU level data. These are the event tables, and are identical in structure to MIMIC-III (chartevents, etc)
- [ed](/docs/iv/modules/ed) - data from the emergency department
- [cxr](/docs/iv/modules/cxr) - lookup tables and meta-data from MIMIC-CXR, allowing linking to MIMIC-IV
- [note](/docs/iv/modules/note) - deidentified free-text clinical notes

{{% pageinfo %}}
MIMIC-Note is currently not publicly available and the structure is subject to change.
{{% /pageinfo %}}

All patients across all datasets are in `mimic_core`. However, not all ICU patients have ED data, not all ICU patients have CXRs, not all ED patients have hospital data, and so on. Within an individual dataset, there are also incomplete tables as certain electronic systems did not exist in the past. For example, eMAR data is only available from 2015 onward.

Tables for each module are detailed in the respective sections.