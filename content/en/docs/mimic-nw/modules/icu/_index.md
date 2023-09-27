---
title: "ICU"
linkTitle: "ICU"
date: 2023-09-18
weight: 30
description: >
  The ICU module contains information collected from the clinical information system of both BIDMC and NHMC used within the ICU. Information covered includes icu admissions, procedures, and charted vital sign data.
---

The ICU module contains data sourced from the clinical information system at the BIDMC (MetaVision (iMDSoft)) and NHMC. MetaVision tables in BIDMC were denormalized to create a star schema where the icustays and d_items tables link to a set of data tables all suffixed with *events*.

Data documented in the ICU module includes icu admissions (*icu stays*), procedures (*procedureevents*, *d_items*), and charted vital sign data (*chartevents*, *d_items*). All events tables contain a `stay_id` column allowing identification of the associated ICU patient in *icustays*, and an `itemid` column allowing identification of the concept documented in *d_items*.