+++
date = "2015-09-01T19:33:17-04:00"
title = "MIMIC-ICU"
linktitle = "About"
weight = 10
toc = false

+++

The ICU module contains data sourced from the clinical information system at the BIDMC: MetaVision (iMDSoft). MetaVision tables were denormalized to create a star schema where the icustays and d_items tables link to a set of data tables all suffixed with "events". Data documented in the icu module includes intravenous and fluid inputs (inputevents), patient outputs (outputevents), procedures (procedureevents), information documented as a date or time (datetimeevents), and other charted information (chartevents). All events tables contain a stay_id column allowing identification of the associated ICU patient in icustays, and an itemid column allowing identification of the concept documented in d_items.

{{% alert title="Tables" color="primary" %}}
This section provides a description of the MIMIC-ICU module. Detailed table information is found in the [Tables](/iv/datasets/icu) section. 
{{% /alert %}}
