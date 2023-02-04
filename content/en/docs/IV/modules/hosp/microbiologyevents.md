---
title: "microbiologyevents"
linktitle: "microbiologyevents"
weight: 1
date: 2020-08-10
description: >
  Microbiology cultures.
---

## *microbiologyevents*

Microbiology tests are a common procedure to check for infectious growth and to assess which antibiotic treatments are most effective.

The table is best explained with a demonstrative example. If a blood culture is requested for a patient, then a blood sample will be taken and sent to the microbiology lab.
The time at which this blood sample is taken is the `charttime`.
The `spec_type_desc` will indicate that this is a blood sample.
Bacteria will be cultured on the blood sample, and the remaining columns depend on the outcome of this growth:

* If no growth is found, the remaining columns will be NULL
* If bacteria is found, then each organism of bacteria will be present in `org_name`, resulting in multiple rows for the single specimen (i.e. multiple rows for the given `spec_type_desc`).
* If antibiotics are tested on a given bacterial organism, then each antibiotic tested will be present in the `ab_name` column (i.e. multiple rows for the given `org_name` associated with the given `spec_type_desc`). Antibiotic parameters and sensitivities are present in the remaining columns (`dilution_text`, `dilution_comparison`, `dilution_value`, `interpretation`).

## Important considerations

Typically, negative values are indicated by a NULL value. However, `itemid` 90856 has a value of "NEGATIVE", and should be included in queries which seek to segregate microbiology data based on positive/negative findings.

`hadm_id` is assigned to observations using the administrative transfer table. However this does not always perfectly capture labs around the hospital stay.
To be specific, as of v2.1, it is possible to assign 1,449,547 observations with an `hadm_id` using a join to *admissions* with `subject_id`,  `admittime`, and `dischtime`. However, only 1,396,224 (96%) of these observations have an `hadm_id` actually stored in the *microbiologyevents* table. Users wishing to ensure capture of labs proximal to hospital stays should be aware of this, and use joins with time as necessary.

<!--

select 
  count(adm.hadm_id) as num_obs_in_hosp
  , count(me.subject_id) as num_obs_with_subject_id
  , count(me.hadm_id) as num_obs_with_hadm_id
  , count(me.hadm_id)*100.0/count(me.subject_id) as percent_obs_assigned_hadm_id
from hosp.admissions adm
left join hosp.microbiologyevents me
on adm.subject_id = me.subject_id
and me.charttime between adm.admittime and adm.dischtime
WHERE me.subject_id IS NOT NULL;

-->
## Table columns

Name | Postgres data type | Example value
---- | ---- | ----
`microevent_id` | INTEGER NOT NULL | 1234567
`subject_id` | INTEGER NOT NULL | 12078372
`hadm_id` | INTEGER | 29450599
`micro_specimen_id` | INTEGER NOT NULL | 6386644
`order_provider_id` | VARCHAR(10) | P12ABC
`chartdate` | TIMESTAMP(0) NOT NULL | 2130-04-01 00:00:00
`charttime` | TIMESTAMP(0) | 2130-04-01 16:00:00
`spec_itemid` | INTEGER NOT NULL | 70012
`spec_type_desc` | VARCHAR(100) NOT NULL | BLOOD CULTURE
`test_seq` | INTEGER NOT NULL | 2
`storedate` | TIMESTAMP(0) | 2130-04-05 00:00:00
`storetime` | TIMESTAMP(0) | 2130-04-05 14:46:00
`test_itemid` | INTEGER | 90117
`test_name` | VARCHAR(100) | ANAEROBIC BOTTLE
`org_itemid` | INTEGER | 80155
`org_name` | VARCHAR(100) | STAPHYLOCOCCUS, COAGULASE NEGATIVE
`isolate_num` | SMALLINT | 1
`quantity` | VARCHAR(50) | 
`ab_itemid` | INTEGER | 90025
`ab_name` | VARCHAR(30) | LEVOFLOXACIN
`dilution_text` | VARCHAR(10) | <=0.12
`dilution_comparison` | VARCHAR(20) | <=
`dilution_value` | DOUBLE PRECISION | 0.12
`interpretation` | VARCHAR(5) | S
`comments` | TEXT | ___

### `microevent_id`

A unique integer denoting the row.

### `subject_id`

{{% include "/static/include/subject_id.md" %}}

### `hadm_id`

{{% include "/static/include/hadm_id.md" %}}


### `micro_specimen_id`

Uniquely denoted the specimen from which the microbiology measurement was made. Most microbiology measurements are made on patient derived samples (specimens) such as blood, urine, and so on.
Often multiple measurements are made on the same sample. The `micro_specimen_id` will group measurements made on the same sample, e.g. organisms which grew from the same blood sample.

### `order_provider_id`

`order_provider_id` provides an anonymous identifier for the provider who ordered the microbiology test.
{{% include "/static/include/provider_id.md" %}}

## `chartdate`, `charttime`

`charttime` records the time at which an observation was charted, and is usually the closest proxy to the time the data was actually measured.
`chartdate` is the same as `charttime`, except there is no time available.

`chartdate` was included as time information is not always available for microbiology measurements: in order to be clear about when this occurs, `charttime` is null, and `chartdate` contains the date of the measurement.

In the cases where both `charttime` and `chartdate` exists, `chartdate` is equal to a truncated version of `charttime` (i.e. `charttime` without the timing information). Not all observations have a `charttime`, but all observations have a `chartdate`.

## `spec_itemid`, `spec_type_desc`

The specimen which is tested for bacterial growth.
The specimen is a sample derived from a patient; e.g. blood, urine, sputum, etc.

## `test_seq`

If multiple samples are drawn, the `test_seq` will delineate them. For example, if an aerobic and anerobic culture bottle are used for the same specimen, they will have distinct `test_seq` values (likely 1 and 2).

## `storedate`, `storetime`

The date (`storedate`) or date and time (`storetime`) of when the microbiology result was available. While many interim results are made available during the process of assessing a microbiology culture, the times here are the time of the *last* known update.

## `test_itemid`, `test_name`

The test performed on the given specimen.

## `org_itemid`, `org_name`

The organism, if any, which grew when tested. If NULL, no organism grew (i.e. a negative culture).

## `isolate_num`

For testing antibiotics, the isolated colony (integer; starts at 1).

## `ab_itemid`, `ab_name`

If an antibiotic was tested against the given organism for sensitivity, the antibiotic is listed here.

## `dilution_text`, `dilution_comparison`, `dilution_value`

Dilution values when testing antibiotic sensitivity.

## `interpretation`

`interpretation` of the antibiotic sensitivity, and indicates the results of the test. "S" is sensitive, "R" is resistant, "I" is intermediate, and "P" is pending.

### `comments`

Deidentified free-text comments associated with the microbiology measurement. Usually these provide information about the sample, whether any notifications were made to care providers regarding the results, considerations for interpretation, or in some cases the comments contain the result of the measurement itself. Comments which have been fully deidentified (i.e. no information content retained) are present as three underscores: `___`. A `NULL` comment indicates no comment was made for the row.
