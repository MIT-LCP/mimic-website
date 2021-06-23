+++
date = "2017-01-01T00:00:00-04:00"
title = "CareVue"
linktitle = "CareVue"
weight = 3
toc = "false"

+++

CareVue is a clinical information system provided by Philips which archived and displayed clinical data at the bedside for intensive care unit patients admitted to the Beth Israel Deaconess Medical Center. Part of the MIMIC-III database is extracted from the CareVue system, the other part is extracted from the [MetaVision system](/iii/mimicdata/metavision/). The immediate consequence of this is that data for the entire duration of the MIMIC-III database needs to be extracted using special steps of different `ITEMID` in order to get data from both systems. The MIMIC-IV data is comprised solely of data from Metavision.

CareVue is frequently referenced in the documentation because:

* Patients in the CareVue system are admitted between 2001-2008 (one example of a consequence is that these patients have a longer follow-up for date of death)
* Patients in the CareVue system have data archived a different format
* All `ITEMID` for CareVue patients will differ from MetaVision patients
