---
title: ICU
layout: default
nav_order: 30
description: The ICU module contains information collected from the clinical information
  system used within the ICU. Documented data includes intravenous administrations,
  ventilator settings, and other charted items.
has_children: true
parent: MIMIC-IV
---


The ICU module contains data sourced from the clinical information system at the BIDMC: MetaVision (iMDSoft). MetaVision tables were denormalized to create a star schema where the icustays and d_items tables link to a set of data tables all suffixed with "events". Data documented in the icu module includes intravenous and fluid inputs (inputevents), ingredients of the aforementioned inputs (ingredientevents), patient outputs (outputevents), procedures (procedureevents), information documented as a date or time (datetimeevents), and other charted information (chartevents). All events tables contain a stay_id column allowing identification of the associated ICU patient in icustays, and an itemid column allowing identification of the concept documented in d_items.
