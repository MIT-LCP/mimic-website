+++
title = "Guidelines for creating derived datasets and models"
linktitle = "Derived data"
weight = 30
toc = "true"
+++

We recognize that there is value in creating datasets or models that are either derived from MIMIC or which augment MIMIC in some way (for example, by adding annotations). Here are some guidelines on creating these datasets and models:

- Any derived datasets or models should be treated as containing sensitive information. If you wish to share these resources, they should be shared on PhysioNet under the same agreement as the source data.
- If your dataset is derived from MIMIC and you would like to use the MIMIC acronym in its name, please include the letters "Ext" (for example, MIMIC-IV-Ext-YOUR-DATASET"). 
  - Ext may either indicate "extracted" (e.g. a derived subset) or "extended" (e.g. annotations), depending on your use case.
