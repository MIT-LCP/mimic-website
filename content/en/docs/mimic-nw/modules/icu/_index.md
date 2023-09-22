---
title: "ICU"
linkTitle: "ICU"
date: 2023-09-18
weight: 30
description: >
  The ICU module contains information collected from the clinical information system used within the ICU. Information covered includes icu admissions, procedures, and vital signs charted information.
---

The ICU module contains data sourced from the clinical information system at the BIDMC: MetaVision (iMDSoft). MetaVision tables were denormalized to create a star schema where the icustays and d_items tables link to a set of data tables all suffixed with "events". Data documented in the icu module includes  icu admissions (icu stays) procedures (procedureevents, d_items), and vital signs charted information (chartevents, d_items). All events tables contain a stay_id column allowing identification of the associated ICU patient in icustays, and an itemid column allowing identification of the concept documented in d_items.