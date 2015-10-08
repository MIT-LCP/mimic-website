+++
date = "2015-09-01T14:02:13-04:00"
title = "Elective surgery data extraction"
draft = true
linktitle = "Elective surgery data extraction"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++


# Elective surgery

## Motivation

This tutorial provides an introduction to defining a concept in MIMIC-III. In this case, the desired concept is *elective surgery*, where a patient is admitted to the intensive care unit either in routine preparation for a planned surgery or for stabilization after completion of a planned surgery. Elective surgery is an important covariate for many risk adjustments as patients who are admitted to the ICU for planned surgeries tend to be healthier than their counterparts.

## Tables used

The tables used in this tutorial are:

* ADMISSIONS - defines `HADM_ID` and provides information regarding patient hospital admissions
* SERVICES - provides information regarding the service a patient is admitted under, and any service transfers which may have occurred during their stay
* NOTEEVENTS - contains all free text notes associated with a patient stay

# Plan extraction of concept

Prior to extracting a concept, it is important to rigorously define it in a manner amenable to database querying. Usually this involves iterative discussion with a domain expert, such as an intensivist or nursing staff. In this case, elective surgery is defined as:

* The hospital admission was elective
* The hospital admission was for the purpose of surgery

## Elective admissions

As we are interested in high level information regarding hospital admissions, the first table to investigate is the ADMISSIONS table, which has the following columns:

* ROW_ID
* SUBJECT_ID
* HADM_ID
* ADMITTIME
* DISCHTIME
* DEATHTIME
* ADMISSION_TYPE
* ADMISSION_LOCATION
* DISCHARGE_LOCATION
* INSURANCE
* LANGUAGE
* RELIGION
* MARITAL_STATUS
* ETHNICITY
* DIAGNOSIS
* HAS_IOEVENTS_DATA
* HAS_CHARTEVENTS_DATA

The `ADMISSION_TYPE` column looks promising:

```sql
select distinct ADMISSION_TYPE
from ADMISSIONS
```

Returns:

* ELECTIVE
* URGENT
* NEWBORN
* EMERGENCY

Clearly, we can use `ADMISSION_TYPE` = 'ELECTIVE' to define elective admissions from the hospital.

## Surgical admissions

The definition of a surgical admission is less straightforward. There is no obvious solution in the ADMISSIONS table. We could use `DIAGNOSIS`, but this has two flaws: first, it would require defining diagnoses which are exclusively surgical or non-surgical, a non-trivial and perhaps impossible, and second as `DIAGNOSIS` is a free text field it will have *many* distinct values.

There are a few other tables in MIMIC-III which provide administrative data regarding hospital admissions. These tables are: CALLOUT, CPTEVENTS, DIAGNOSES_ICD, DRGCODES, PROCEDURES_ICD, SERVICES and TRANSFERS. Each of these tables need to be considered as possible sources of the information we are searching for: a definition of a hospital admission as surgical.

CALLOUT contains information regarding when an ICU discharge was planned and when the ICU discharge actually occurred. There will be no information regarding surgical status in this table.

CPTEVENTS contains current procedure terminology (CPT) codes for hospital admissions. This table could be used if we can define a set of CPT codes which are exclusive to surgery. There are two challenges to this approach: first, a list of definitions for CPT codes is unavailable as the American Medical Association has chosen to charge a licensing fee for its use. This makes it extremely difficult to define a CPT code as the only information available is a hierarchical category. Second, inspection of the CPTEVENTS table shows that no time information is available. As a result, we wouldn't know if the surgery was the purpose of the admission, or whether a patient later had a surgery in relation to their ICU stay.

DIAGNOSES_ICD provides diagnoses using the international statistical classification of diseases and related health problems (ICD) codes. This method could work but suffers from the same drawback discussed regarding the `DIAGNOSIS` column in the ADMISSIONS table: defining a set of diagnoses as surgical or non-surgical is non-trivial.

DRGCODES provides diagnosis related groups (DRG) codes, another diagnosis coding system used for billing in the hospital. Again, we face the same issue as in DIAGNOSES_ICD.

PROCEDURES_ICD lists all procedures performed during a patient's hospital stay using ICD procedural code terminology. This table could be used to define surgeries very effectively, as there is undoubtedly a hierarchy for surgical procedures which could be used. While this table does not have date information, it does list the sequence in which the procedures were performed (`PROC_SEQ_NUM`), and defining patients as surgical if one of their first ICD procedures was related to surgery could be a viable method. For now let's move on.

SERVICES captures the service, or the type of clinical team caring for the patient, which a patient is currently under. Types of services can be extracted as follows:

```sql
select distinct CURR_SERVICE
from SERVICES
```

This query returns the following (reformatted as a multicolumn table for convenience):

| Service | |
--- | ---- | ----
MED | NMED | TRAUM
CSURG | GYN | NSURG
NB | GU | TSURG
SURG | NBB | CMED
ORTHO | ENT | PSURG
VSURG | OBS | PSYCH
OMED | DENT |

Here we can see that services define surgical and non-surgical admissions, and are a reasonably simple yet likely effective method for defining elective surgery.


# Experiment with concept extraction

## Elective

Now that we have determined a good method for defining surgical admissions, the next step is to extract the information from the database. Extracting elective admissions is simple enough:

```sql
select adm.subject_id, adm.hadm_id, adm.admittime, adm.dischtime
, case when adm.ADMISSION_TYPE = 'ELECTIVE' then 1 else 0 end as ELECTIVE
from mimic2v30.admissions adm
```

This provides a table of all hospital admissions, with a binary flag `ELECTIVE` indicating where the admission was elective or not.

## Surgical

The more difficult aspect of this query will be matching surgical services for patients to their admissions in a manner that ensures that the *first* service is surgical.

First, we can extract admissions with only one service as follows:

```sql
select hadm_id, curr_service from SERVICES
-- filter down to *only* admissions with 1 service
where hadm_id in
(
  select hadm_id from SERVICES group by hadm_id having count(*)<2
)
```

This results in only `HADM_ID` where there is only one service for the entire stay. We can use the aggregate operator COUNT() to get an idea of what proportion of hospital admissions have only one service.


```sql
-- table with all hospital admissions who only ever had 1 service
with singleservice as
(
  select hadm_id, curr_service from mimic2v30.services
  -- filter down to *only* admissions with 1 service
  where hadm_id in
  (
    select hadm_id from mimic2v30.services group by hadm_id having count(*)<2
  )
)
select
  count(adm.hadm_id) as NumAdm
, count(ss.curr_service) as NumSingleService
, round(count(ss.curr_service)/count(adm.hadm_id)*100,2) as PercentWithSingleService
from mimic2v30.admissions adm
left join singleservice ss
  on adm.hadm_id = ss.hadm_id;
```

which results in:

NumAdm | NumSingleService | PercentWithSingleService
---- | ---- | ----
58976 | 48079 | 81.52

So we can see that 80% of hospital admissions have only one service. In these cases it is trivial to define elective surgery, as the patient is only admitted under one service (which will have the suffix 'SURG') and will have 'ELECTIVE' as their `ADMISSION_TYPE`.

For the remaining admissions, we must determine a method of defining their surgical status. One method could be defining a patient as surgical if their *first* service is surgical. This could be accomplished as follows:


```sql
-- table with all hospital admissions who only ever had 1 service
with singleservice as
(
  select hadm_id, curr_service from mimic2v30.services
  -- filter down to *only* admissions with 1 service
  where hadm_id in
  (
    select hadm_id from mimic2v30.services group by hadm_id having count(*)<2
  )
)
-- table with hospital admissions who had multiple services
, multipleservice as
(
  select s.hadm_id, s.TRANSFERTIME, s.PREV_SERVICE, s.CURR_SERVICE
  -- create an integer which starts at 1 for each hospital admission and increments for each consecutive service
  , ROW_NUMBER() over (partition by s.hadm_id ORDER BY s.transfertime) as ServiceOrder
  from mimic2v30.services s
  -- join to single services table to filter these HADM_ID out
  left join singleservice ss
    on s.hadm_id = ss.hadm_id
  where ss.hadm_id is null
)
select
  count(adm.hadm_id) as NumAdm
, count(ss.curr_service) as NumSingleService
, round(count(ss.curr_service)/count(adm.hadm_id)*100,2) as PercentWithSingleService
, count(ms.curr_service) as NumMultiService
, round( ( count(ss.curr_service) + count(ms.curr_service) )/count(adm.hadm_id)*100,2) as PercentWithSingleService
from mimic2v30.admissions adm
left join singleservice ss
  on adm.hadm_id = ss.hadm_id
left join multipleservice ms
  on adm.hadm_id = ms.hadm_id and ServiceOrder = 1;
```

which returns:

NumAdm | NumSingleService | % with single services | NumMultiService | % with multiple services
---- | ---- | ---- | ---- | ----
58976 | 48079 | 81.52 | 10847 | 99.92

Here we can see that this method gives us a definition of surgical status for 99.92%. When performing retrospective data analysis, 99.92% data completion is a very nice number to see.
However, we have made an assumption with this extraction: we assumed that all patients whose first service was surgical were admitted for a pre-planned elective surgery. This sounds reasonable, but all assumptions should be validated before they are used in an analysis. We can investigate the number of elective admissions under a variety of constraints as follows:

```sql
-- table with all hospital admissions who only ever had 1 service
with singleservice as
(
  select hadm_id, curr_service from mimic2v30.services
  -- filter down to *only* admissions with 1 service
  where hadm_id in
  (
    select hadm_id from mimic2v30.services group by hadm_id having count(*)<2
  )
)
-- table with hospital admissions who had multiple services
, multipleservice as
(
  select s.hadm_id, s.TRANSFERTIME, s.PREV_SERVICE, s.CURR_SERVICE
  , ROW_NUMBER() over (partition by s.hadm_id ORDER BY s.transfertime) as ServiceOrder
  from mimic2v30.services s
  -- join to single services table to filter these HADM_ID out
  left join singleservice ss
    on s.hadm_id = ss.hadm_id
  where ss.hadm_id is null
)
select

-- How many admissions are there?
 count(distinct adm.hadm_id) as NumAdm

-- How many admissions have only a single service?
, count(ss.curr_service) as NumSingleService

-- How many admissions have multiple services?
, count(case when serviceorder = 1 then ms.curr_service else null end)
    as NumMS

-- How many of these admissions had their first service being surgical?
, sum(case when serviceorder = 1 and ms.curr_service like '%SURG' then 1 else 0 end)
    as NumMS_Surgical

-- How many of these admissions had their *FIRST* surgical service within 8 hours of their admission?
, sum(case when serviceorder = 1 and ms.transfertime between adm.admittime-8/24 and adm.admittime+8/24 and ms.curr_service like '%SURG' then 1 else 0 end)
    as NumMS_FirstSurg8hr

-- How many of these admissions had their *ANY* surgical service within 8 hours of their admission?
, sum(case when ms.transfertime between adm.admittime-8/24 and adm.admittime+8/24 and ms.curr_service like '%SURG' then 1 else 0 end)
    as NumMS_AnySurg8hr

-- How many of *ELECTIVE* admissions had their *FIRST* surgical service within 8 hours of their admission?
, sum(case when adm.admission_type = 'ELECTIVE' and serviceorder = 1 and ms.transfertime between adm.admittime-8/24 and adm.admittime+8/24 and ms.curr_service like '%SURG' then 1 else 0 end)
    as NumMSElect_FirstSurg8hr

-- How many of *ELECTIVE* admissions had their *ANY* surgical service within 8 hours of their admission?
, sum(case when adm.admission_type = 'ELECTIVE' and ms.transfertime between adm.admittime-8/24 and adm.admittime+8/24 and ms.curr_service like '%SURG' then 1 else 0 end)
    as NumMSElect_AnySurg8hr

from mimic2v30.admissions adm
left join singleservice ss
  on adm.hadm_id = ss.hadm_id
left join multipleservice ms
  on adm.hadm_id = ms.hadm_id;
```

This results in the following table (transposed for reading convenience)

Name | Description | count
---- | ---- | ----
NumAdm | Admissions | 58976
NumSingleService | .. with single service | 48079
NumMS  | .. with multiple services | 10847
NumMS_Surgical  | .... and the first service is surgical | 1800
NumMS_FirstSurg8hr | ...... and it occurrs within 8 hours of admission | 1715
NumMSElect_FirstSurg8hr | ........ and it's an elective admission | 239
NumMS_AnySurg8hr | Number of admissions with surgical services within 8 hours of admission | 2264
NumMSElect_AnySurg8hr | .. and it's an elective admission  | 278

Since there are only 40 `HADM_ID` who had a service within 8 hours that was *not* their first service, it's a small enough task that we can investigate the discharge summaries associated with these admissions to determine whether they are truly surgical admissions.

```sql
select adm.hadm_id, adm.admittime, adm.dischtime
, ne.chartdate, ne.category, ne.description
, ne.text
from mimic2v30.admissions adm
left join mimic2v30.noteevents ne
  on adm.hadm_id = ne.hadm_id and ne.category = 'Discharge summary'
where adm.hadm_id = 100010
order by hadm_id;
```

# Final query

```sql

-- table with all hospital admissions who only ever had 1 service
with singleservice as
(
  select hadm_id, curr_service from mimic2v30.services
  -- filter down to *only* admissions with 1 service
  where hadm_id in
  (
    select hadm_id from mimic2v30.services group by hadm_id having count(*)<2
  )
)
-- table with hospital admissions who had multiple services
, multipleservice as
(
  select s.hadm_id, s.TRANSFERTIME, s.PREV_SERVICE, s.CURR_SERVICE
  , ROW_NUMBER() over (partition by s.hadm_id ORDER BY s.transfertime) as ServiceOrder
  from mimic2v30.services s
  -- join to single services table to filter these HADM_ID out
  left join singleservice ss
    on s.hadm_id = ss.hadm_id
  where ss.hadm_id is null
)
select
  adm.subject_id, adm.hadm_id, adm.admittime, adm.dischtime
, case when adm.ADMISSION_TYPE != 'ELECTIVE' then 0
    when ss.curr_service is not null and ss.curr_service like '%SURG%' then 1
    when ms.curr_service is not null and ms.curr_service like '%SURG%' then 1
    else 0
  end as ElectiveSurgery

from mimic2v30.admissions adm
left join singleservice ss
  on adm.hadm_id = ss.hadm_id
left join multipleservice ms
  on adm.hadm_id = ms.hadm_id and ServiceOrder = 1;

 ```

 This query could be simplified by collapsing the single service and multiple service queries into a single query which extracts the first service, regardless of the number of services a patient has, as follows:

```sql
-- table with all hospital admissions and their services
with ss as
(
 select s.hadm_id, s.TRANSFERTIME, s.PREV_SERVICE, s.CURR_SERVICE
 , ROW_NUMBER() over (partition by s.hadm_id ORDER BY s.transfertime) as ServiceOrder
 from mimic2v30.services s
)
select
 adm.subject_id, adm.hadm_id, adm.admittime, adm.dischtime
 , adm.admission_type, ss.curr_service
, case when adm.ADMISSION_TYPE != 'ELECTIVE' then 0
   when ss.curr_service is not null and ss.curr_service like '%SURG%' then 1
   else 0
 end as ElectiveSurgery

from mimic2v30.admissions adm
left join ss
 on adm.hadm_id = ss.hadm_id and ServiceOrder = 1;
```
