+++
title = "Guidelines for reviewers and authors"
linktitle = "Paper Guidelines"
weight = 2
toc = "true"

+++

Authoring or reviewing a MIMIC-III paper can be challenging due to the complex nature of the data.
Our recommendations for authors when writing papers, or for reviewers when reviewing papers, are:

1. The version of MIMIC-III should be specified. The current version is MIMIC-III v1.4. If researchers are using an older version, inquire why, as MIMIC-III v1.4 was released 2 years ago.
2. It is easy to conflate an ICU admission with a hospital admission. Ensure that it is clear.
3. Mortality is a common outcome, but can be defined in a number of ways. Some researchers define 30-day mortality from *admission*, whereas others define it from *discharge*. Ensure the manuscript is clear. We recommend using 30-days from admission, as this better reflects the severity of illness of the patient on admision to the ICU.
4. Avoid vague criteria. For example, "removed patients missing data" is unclear, whereas "removed patients with no heart rate measurements in the first 24 hours of their stay" is much more interpretable.
5. Verify that both the MIMIC-III paper and the MIMIC-III data citation are referenced. See the [acknowledgement](/about/acknowledgements) page for details.

Most of important of all, code should be included with the paper. The MIMIC-III data use agreement requires researchers to publish code with their paper, and there is no substitute for code in explicitly describing the methodology.
e.g. guidelines for reviewers: