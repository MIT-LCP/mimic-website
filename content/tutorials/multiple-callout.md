+++
date = "2015-10-08T07:01:22-04:00"
title = "Multiple callouts"
draft = true
linktitle = "Multiple callouts"
weight = 3
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++

# Multiple callouts

There are many patients who have multiple callouts, that is they are called to be discharge from the ICU multiple times. It's worthwhile to quantify why this occurrs so that no undetected biases creep into analyses using the callout table.

# Hospital admissions investigated

Before investigating the CALLOUT table, we should create a cohort of patients who we believe *should* have data in the CALLOUT table. We will filter hospital admissions using some prior information: the data only begins a few years after the start of MIMIC data collection, there are admissions in the ADMISSIONS table with no corresponding ICU data, and the data does not contain any information for neonates.

This is query extracts only admissions who were admitted *after* call out data began being collected:

```sql
select count(*), sum(HAS_CHARTEVENTS_DATA)
from mimic2v30.admissions adm
where adm.hadm_id in
(
select hadm_id from mimic2v30_phi_release.admissions
where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
);
```

`COUNT(*)` returns 39543. Note the use of a PHI table which only I have! It contains the real dates. Note also that there is a column called `HAS_CHARTEVENTS_DATA`. This column is provided for convenience: it informs the user if a `HADM_ID` ever has data in the CHARTEVENTS table.
<!-- The primary reason for a patient not having data in CHARTEVENTS is likely due to a mismatch in the hospital identifiers, perhaps due to a human typographical error. These admissions can be considered missing at random (since the patient characteristics are probably unrelated to a care giver's typing skills), so they won't bias any studies by being missing. Furthermore, since the CALLOUT table is collected from the hospital, and the ADMISSIONS table is collected from the hospital, this shouldn't even be necessary, because the data come from the same source. However, we are paranoid, so we apply this filter anyway. -->
This filter will remove 'dummy' hospital admissions with no associated data; e.g. organ donor accounts.
The result of the summation is 38763, indicating that there are 38763 hospital admissions admitted after the start date of call out data collection.

We know that neonates do not have any call out data. So we should filter these admissions.

```sql
select count(*), sum(HAS_CHARTEVENTS_DATA)
from mimic2v30.admissions adm
inner join mimic2v30.patients pat
  on adm.subject_id = pat.subject_id
where adm.hadm_id in
(
select hadm_id from mimic2v30_phi.admissions
where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
)
and months_between(adm.intime,pat.dob) > 1;
```

Returns 36140 total rows, and 35407 with data. Note `months_between` is Oracle specific, you may need to adapt this command to your own version of SQL.

Let's see how many have an observation in the CALLOUT table:

```sql
select
  count(adm.hadm_id) as NumAdmissions
  , count(ca.hadm_id) as NumAdmWithCallout
  , sum(HAS_CHARTEVENTS_DATA) as NumAdmWithICUData
  , count(case when HAS_CHARTEVENTS_DATA = 1 then ca.hadm_id else null end) as NumAdmWithICUDataAndCallout
from mimic2v30.admissions adm
inner join mimic2v30.patients pat
  on adm.subject_id = pat.subject_id


left join
  -- subquery ensures there is only 1 subject_id/hadm_id pair to join against
  ( select subject_id, hadm_id from mimic2v30.callout group by subject_id, hadm_id ) ca
  on adm.subject_id = ca.subject_id and adm.hadm_id = ca.hadm_id

where adm.hadm_id in
(
select hadm_id from mimic2v30_phi_release.admissions
where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
)
and months_between(adm.admittime,pat.dob) > 1;
```

Column | Count | Percent
---- | ---- | ----
Number of admissions | 36140 |
.. with callout | 28695 | 79%
Number of admissions with ICU data | 35407 |
.. with callout | 28623 | 81%

So clearly we have quite a few ICU admissions who do not have an entry in the call out table: almost 20%! These patients likely died in the ICU. This can be a little tricky to define because we only have information on death in hospital, not death in the ICU. We will have to use the time of death and proximity to ICU discharge to estimate whether the patient died in the ICU.

# Multiple call outs for a single hospital admission

These could occur because:

1. A patient was accidentally called out
2. A patient deteriorated and was no longer fit to stay on the ward


```sql
with ca as
(
select
  adm.SUBJECT_ID, adm.HADM_ID

  , call.HADM_ID as callout_hadm_id

  , adm.admittime, adm.dischtime
  -- callout variables
  , call.createtime as CALLOUT_TIME

  -- this is when a coordinator acknowledged the call out request
  , call.acknowledge_status, call.acknowledgetime

  -- this is the status of the call out
  , call.callout_status

  -- any updates done to the call out...
  , call.updatetime

  -- the final outcome (discharged or cancelled) for the call out
  , call.callout_outcome, call.outcometime

  , HAS_CHARTEVENTS_DATA

  from mimic2v30.admissions adm
  inner join mimic2v30.patients pat
    on adm.subject_id = pat.subject_id
  left join  mimic2v30.callout call
    on adm.subject_id = call.subject_id and adm.hadm_id = call.hadm_id

  -- filter to only patients admitted after call out data collection began
  where adm.hadm_id in
  (
  select hadm_id from mimic2v30_phi_release.admissions
  where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
  and months_between(adm.admittime,pat.dob) > 1
)
select
SUBJECT_ID, HADM_ID, CALLOUT_HADM_ID
, ACKNOWLEDGE_STATUS, ACKNOWLEDGETIME
, UPDATETIME
, CALLOUT_STATUS
, CALLOUT_TIME
, CALLOUT_OUTCOME
, OUTCOMETIME
--  count(hadm_id) as NumAdmissions
--  , sum(HAS_CHARTEVENTS_DATA) as NumAdmWithICUData
--  , count(callout_hadm_id) as NumAdmWithCallout
--  , count(case when HAS_CHARTEVENTS_DATA = 1 then callout_hadm_id else null end) as NumAdmWithICUDataAndCallout
from ca
where hadm_id in (select hadm_id from ca group by hadm_id having count(*)>1)
order by hadm_id, admittime, CALLOUT_TIME;
```

## Investigation of single hospital admissions

A lot of information about a table can be gleaned from investigating single patients and understanding the context of their admission from various notes. Here we investigate `HADM_ID` = 100007.

```sql
with ca as
(
select
  adm.SUBJECT_ID, adm.HADM_ID

  , call.HADM_ID as callout_hadm_id

  , adm.admittime, adm.dischtime
  -- callout variables
  , call.createtime as CALLOUT_TIME

  -- this is when a coordinator acknowledged the call out request
  , call.acknowledge_status, call.acknowledgetime

  -- this is the status of the call out
  , call.callout_status

  -- any updates done to the call out...
  , call.updatetime

  -- the final outcome (discharged or cancelled) for the call out
  , call.callout_outcome, call.outcometime

  , HAS_CHARTEVENTS_DATA

  from mimic2v30.admissions adm
  inner join mimic2v30.patients pat
    on adm.subject_id = pat.subject_id
  left join  mimic2v30.callout call
    on adm.subject_id = call.subject_id and adm.hadm_id = call.hadm_id

  -- filter to only patients admitted after call out data collection began
  where adm.hadm_id in
  (
  select hadm_id from mimic2v30_phi_release.admissions
  where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
  and months_between(adm.admittime,pat.dob) > 1
)
select
SUBJECT_ID, HADM_ID, CALLOUT_HADM_ID
, ACKNOWLEDGE_STATUS, ACKNOWLEDGETIME
, UPDATETIME
, CALLOUT_STATUS
, CALLOUT_TIME
, CALLOUT_OUTCOME
, OUTCOMETIME
from ca
where hadm_id = 100007
order by hadm_id, admittime, CALLOUT_TIME;
```

The result is:

SUBJECT_ID | HADM_ID | ADMITTIME | DISCHTIME
---- | ---- | ---- | ----
23018 | 100007 | 2145-03-31 05:33:00 | 2145-04-07 12:40:00

ACKNOWLEDGE STATUS | ACKNOWLEDGE TIME | UPDATE TIME | CALLOUT STATUS | CALLOUT TIME | OUTCOME STATUS | OUTCOME TIME
---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
Revised |  | 04-01 15:12:03 | Inactive | 04-01 08:52:08 | Discharged | 04-01 18:10:04
Acknowledged | 04-03 11:28:20 | 04-03 13:16:56 | Inactive | 04-03 08:33:47 | Cancelled | 04-03 13:16:56
Acknowledged | 04-04 08:42:26 | 04-04 08:02:54 | Inactive | 04-04 08:02:54 | Discharged | 04-04 12:55:02

<!-- Two points to make with the above table:
1) Short (<1 day) readmissions can be captured by the call out table
2) Canceled call outs are poorly understood
-->

### Unexpected readmission

Looking at the same patient in the transfers table:

```sql
select
  eventtype, icustay_id, curr_careunit, intime, outtime
from mimic2v30.transfers where hadm_id = 100007;
```

Event | ICUSTAY_ID | Care unit | In time | Out time
---- | ---- | ---- | ---- | ----
admit |  |  | 2145-03-31 05:34:18 | 2145-03-31 10:17:23
transfer | 217937 | SICU | 2145-03-31 10:17:23 | 2145-04-01 17:46:05
transfer |  |  | 2145-04-01 17:46:05 | 2145-04-01 23:59:49
transfer |  |  | 2145-04-01 23:59:49 | 2145-04-02 16:11:46
transfer | 217937 | TSICU | 2145-04-02 16:11:46 | 2145-04-04 12:41:10
transfer |  |  | 2145-04-04 12:41:10 | 2145-04-07 12:41:04
discharge |  |  | 2145-04-07 12:41:04 |

We can see that we have assigned the patient the same `ICUSTAY_ID` using our rule of readmission within one day. However they were called out between 04-01 and 04-02, implying that perhaps they were discharged and readmitted. Let's investigate the notes.

```sql
select * from mimic2v30.noteevents ne
where hadm_id = 100007
order by chartdate, charttime;
```

The end of a note at 2145-04-01 15:26:00 states: "Transfer pt to [Hospital Ward Name 53] 9 when telemetry bed becomes available".  

A note during the subsequent transfer to the TSICU states: "small bowel resection with new pneumonia (??aspiration) and confusion. P: continue current antibiotics." So it appears this is an unexpected readmission! So, this implies we could define ICU stays using the call out table, rather than the TRANSFERS table. Unfortunately, this would only work for patients admitted after 2005.


### Canceled callout

`HADM_ID` 100007 has a call out event at 04-03 08:33:47 that was cancelled at 04-03 13:16:56.
If we investigate a nursing note at 04-03 05:13:00 the last phrase is "Transfer to floor.". The subsequent note describes the patient's condition but does not make it clear whether they deteriorated and it was decided to keep them on the unit.

`HADM_ID` 100131 has an `ACKNOWLEDGE_TIME` occurring 7 minutes after their `OUTCOME_TIME` for a cancelled callout. Perhaps this was an accidental call out as it was cancelled 13 seconds after it was input.

`HADM_ID` 100137 (CCU patient) has " ?C/O to floor if groin stable. " before a call out event that is cancelled 3 hours after it is created. The subsequent note reads "CV - pt c/o chest pain as well as l arm pain x 3 this am, occuring during rest.  Pt rec'd sl ntg x1 w/ relief for each incident.  No ecg changes noted.  Decision by team and pt, for further intervention on RCA.  Unable to perform today."

`HADM_ID` 100160 was called out at 16:15 but has a clear nursing note at 17:00 to "REMAIN IN MICU."

`HADM_ID` 100242 on 2161-09-18 00:00:00 "To floor at 1730". No nursing notes earlier. Was in CVICU between 09-01 to 09-03, then 09-06 to 09-07, but no call out information there???

### Final definition

Given the above, we will adjust our definition to be the first *non-cancelled* call out event for the patient's first ICU stay.



#### Queries used

```sql
select
  eventtype, icustay_id, curr_careunit, intime, outtime
from mimic2v30_phi_release.transfers where hadm_id = 100242;
```

```sql
with ca as
(
select
  adm.SUBJECT_ID, adm.HADM_ID

  , call.HADM_ID as callout_hadm_id

  , adm.admittime, adm.dischtime
  -- callout variables
  , call.createtime as CALLOUT_TIME

  -- this is when a coordinator acknowledged the call out request
  , call.acknowledge_status, call.acknowledgetime

  -- this is the status of the call out
  , call.callout_status

  -- any updates done to the call out...
  , call.updatetime

  -- the final outcome (discharged or cancelled) for the call out
  , call.callout_outcome, call.outcometime

  , HAS_CHARTEVENTS_DATA

  from mimic2v30.admissions adm
  inner join mimic2v30.patients pat
    on adm.subject_id = pat.subject_id
  left join  mimic2v30.callout call
    on adm.subject_id = call.subject_id and adm.hadm_id = call.hadm_id

  -- filter to only patients admitted after call out data collection began
  where months_between(adm.admittime,pat.dob) > 1
)
select
SUBJECT_ID, HADM_ID, CALLOUT_HADM_ID
, ACKNOWLEDGE_STATUS, ACKNOWLEDGETIME
, UPDATETIME
, CALLOUT_STATUS
, CALLOUT_TIME
, CALLOUT_OUTCOME
, OUTCOMETIME
--  count(hadm_id) as NumAdmissions
--  , sum(HAS_CHARTEVENTS_DATA) as NumAdmWithICUData
--  , count(callout_hadm_id) as NumAdmWithCallout
--  , count(case when HAS_CHARTEVENTS_DATA = 1 then callout_hadm_id else null end) as NumAdmWithICUDataAndCallout
from ca
where hadm_id in (select hadm_id from ca group by hadm_id having count(*)>1)
order by hadm_id, admittime, CALLOUT_TIME;
```

## Histograms

Knowing what time of day a patient is discharged can be very interesting. Here we have a query which groups call out times and discharge times by the hour of the day:

```sql
with call as
(
select ca.hadm_id, ie.icustay_id, ie.outtime
-- group by the hour of ICU discharge
, EXTRACT(HOUR FROM cast(ie.outtime as timestamp)) as bucket_outtime
-- group by the callout time
, EXTRACT(HOUR FROM cast(ca.createtime as timestamp)) as bucket_callout
from ca
inner join mimic2v30.icustayevents ie
  on ca.hadm_id = ie.hadm_id
where ca.CREATETIME is not null
and ca.hadm_id in
(select hadm_id from mimic2v30.icustayevents group by hadm_id having count(*)<2)
)
, createhist as
(
select bucket_callout as HH, count(*) as ct from call
group by bucket_callout
)
, callhist as
(
select bucket_outtime as HH, count(*) as ct from call
group by bucket_outtime
)
select callhist.HH
, createhist.ct as CalledOutTime
, callhist.ct as CalledOutDischTime
from callhist
left join createhist on callhist.HH = createhist.HH
order by HH;
```

Hour | Number called out | Number discharged
---- | ---- | ----
00:00 | 6 | 501
01:00 | 6 | 349
02:00 | 5 | 168
03:00 | 3 | 106
04:00 | 8 | 50
05:00 | 19 | 66
06:00 | 60 | 65
07:00 | 1663 | 46
08:00 | 4034 | 48
09:00 | 4816 | 147
10:00 | 5183 | 503
11:00 | 4360 | 1102
12:00 | 2730 | 1292
13:00 | 1586 | 1530
14:00 | 1659 | 2216
15:00 | 1108 | 2546
16:00 | 859 | 3504
17:00 | 675 | 4270
18:00 | 446 | 4036
19:00 | 199 | 1222
20:00 | 120 | 1804
21:00 | 82 | 2157
22:00 | 58 | 1406
23:00 | 6 | 557

Here we can see most call outs happen between 07:00 and 13:00 and most discharges happen between 14:00 and 20:00. This lines up with intuition: call outs occur during rounds, and most discharges occur when a bed has been freed in the ward (say after a patient has been discharged at the end of the day).

# Defining the base cohort

Now that we have done plenty of investigation into the CALLOUT table, we can go ahead and define our base cohort.

## All patients

First, we see how many unique `ICUSTAY_ID` we have.

```sql
select
count(ie.icustay_id) as NumIID
from mimic2v30.ICUSTAYEVENTS ie;
```

Returns 61532. Note ICUSTAYEVENTS has one unique `ICUSTAY_ID` per row.
We will need more information (e.g. date of birth, hospital admission date) for these patients, so we join to the other patient information tables:

```sql
select
    count(ie.icustay_id) as NumIID
from mimic2v30.icustayevents ie

-- get more information regarding each ICU stay
inner join mimic2v30.patients pat
  on ie.subject_id = pat.subject_id
inner join mimic2v30.ADMISSIONS adm
  on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id;
```

Returns 61532. Unsurprisingly, joining to these tables does not duplicate rows.

## Filter out neonates

We are not interested in neonatal patients for this study.

```sql
select
count(ie.icustay_id) as NumIID
from mimic2v30.icustayevents ie

-- get more information regarding each ICU stay
inner join mimic2v30.patients pat
  on ie.subject_id = pat.subject_id
inner join mimic2v30.ADMISSIONS adm
  on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

-- only adults
where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1;
```

Returns 53432. Next up, we know that CALLOUT data began data collection sometime during the archiving of the database, so we filter to only these patients.

```sql
select
count(ie.icustay_id) as NumIID
from mimic2v30.icustayevents ie

-- get more information regarding each ICU stay
inner join mimic2v30.patients pat
  on ie.subject_id = pat.subject_id
inner join mimic2v30.ADMISSIONS adm
  on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

-- only adults
where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1

-- filter to only patients admitted after call out data collection began
and ie.hadm_id in
(
select hadm_id from mimic2v30_phi_release.admissions
where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
);
```

Returns 38164.
Now, we filter to only the first ICU stay for each hospital admission (we rearrange the query to use a temporary with to facilitate this).

```sql
with co as
(
  select
    ie.*
      -- generate an integer which is 1 for the first ICU stay
      , ROW_NUMBER() over (partition by ie.hadm_id order by ie.intime) as ICU_STAY

  from mimic2v30.icustayevents ie

  -- get more information regarding each ICU stay
  inner join mimic2v30.patients pat
    on ie.subject_id = pat.subject_id
  inner join mimic2v30.ADMISSIONS adm
    on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

  -- only adults
  where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1

  -- filter to only patients admitted after call out data collection began
  and ie.hadm_id in
  (
    select hadm_id from mimic2v30_phi_release.admissions
    where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
)
select
count(icustay_id) as NumIID
from co
where HOSP_STAY = 1;
```

This returns 35494. Next we filter to only the first hospital stay for each patient.

```sql
with co as
(
  select
    ie.*
  -- generate an integer which is 1 for the first hospital stay
  , ROW_NUMBER() over (partition by adm.subject_id order by adm.admittime, ie.intime) as HOSP_STAY

  -- generate an integer which is 1 for the first ICU stay
  , ROW_NUMBER() over (partition by ie.hadm_id order by ie.intime) as ICU_STAY
  from mimic2v30.icustayevents ie

  -- get more information regarding each ICU stay
  inner join mimic2v30.patients pat
    on ie.subject_id = pat.subject_id
  inner join mimic2v30.ADMISSIONS adm
    on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

  -- only adults
  where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1

  -- filter to only patients admitted after call out data collection began
  and ie.hadm_id in
  (
    select hadm_id from mimic2v30_phi_release.admissions
    where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
)
select
count(icustay_id) as NumIID
from co
where HOSP_STAY = 1
and ICU_STAY = 1;
```

This returns 27800. A little thought will allow you to conclude that, as the code is written, the filter for the first hospital admission also filters the first ICU admission. So we can remove the `ICU_STAY` column as it is redundant.
 Now, we join this to the actual CALLOUT table to get information regarding patient discharge planning.

```sql
with co as
(
  select

  -- ICU information
  ie.*

  -- we may need hospital admission/discharge times later
  , adm.admittime, adm.dischtime

  -- generate an integer which is 1 for the first ICU admission in the first hospital admission
  , ROW_NUMBER() over (partition by adm.subject_id order by adm.admittime, ie.intime) as HOSP_STAY


  from mimic2v30.icustayevents ie

  -- get more information regarding each ICU stay
  inner join mimic2v30.patients pat
    on ie.subject_id = pat.subject_id
  inner join mimic2v30.ADMISSIONS adm
    on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

  -- only adults
  where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1

  -- filter to only patients admitted after call out data collection began
  and ie.hadm_id in
  (
    select hadm_id from mimic2v30_phi_release.admissions
    where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
)
select
count(icustay_id) as NumIID
, count(distinct icustay_id) as NumIID_unique
, count(ca.hadm_id) as NumCallout
, count(distinct ca.hadm_id) as NumCallout_unique
from co
-- join to callout table using hospital admission identifier and times of ICU admit/discharge
left join mimic2v30.callout ca
  on co.hadm_id = ca.hadm_id and ca.createtime between co.intime and co.outtime
where HOSP_STAY = 1;
```

Note that we couldn't directly use `ICUSTAY_ID` to identify call outs because the hospital database that records call out events does not record a equivalent identifier to `ICUSTAY_ID`.
We also have added in a check check if we are not duplicating rows.
The query returns 30529	for NumIID, and 27800 for NumIID_unique, indicating that there are multiple call out events for each `ICUSTAY_ID`, as could be predicted.
It also returns 25061 for NumCallout and 22332 for NumCallout_unique, implying that not all of the ICU stays have a call out event. Our next step is to remove cancelled callouts.

```sql
with co as
(
  select

  -- ICU information
  ie.*

  -- we may need hospital admission/discharge times later
  , adm.admittime, adm.dischtime

  -- generate an integer which is 1 for the first ICU admission in the first hospital admission
  , ROW_NUMBER() over (partition by adm.subject_id order by adm.admittime, ie.intime) as HOSP_STAY


  from mimic2v30.icustayevents ie

  -- get more information regarding each ICU stay
  inner join mimic2v30.patients pat
    on ie.subject_id = pat.subject_id
  inner join mimic2v30.ADMISSIONS adm
    on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

  -- only adults
  where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1

  -- filter to only patients admitted after call out data collection began
  and ie.hadm_id in
  (
    select hadm_id from mimic2v30_phi_release.admissions
    where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
)
select
count(icustay_id) as NumIID
, count(distinct icustay_id) as NumIID_unique
, count(ca.hadm_id) as NumCallout
, count(distinct ca.hadm_id) as NumCallout_unique
from co
-- join to callout table using hospital admission identifier and times of ICU admit/discharge
left join mimic2v30.callout ca
  on co.hadm_id = ca.hadm_id and ca.createtime between co.intime and co.outtime

  -- do not join to cancelled callout events
  and ca.callout_outcome != 'Cancelled'

where HOSP_STAY = 1;
```

NumIID has been reduced to 28187, and NumIID_unique remains unchanged at 27800.
NumCallout has been reduced to 21897, and NumCallout_unique has dropped to 21510 (a reduction of 822).
The next step is to only include the first call out event for patients with multiple call outs during the same ICUSTAY_ID.
This has the effect of removing unexpected readmissions within 24 hours after a patient's discharge.

```sql
with co as
(
  select

  -- ICU information
  ie.*

  -- we may need hospital admission/discharge times later
  , adm.admittime, adm.dischtime

  -- generate an integer which is 1 for the first ICU admission in the first hospital admission
  , ROW_NUMBER() over (partition by adm.subject_id order by adm.admittime, ie.intime) as HOSP_STAY


  from mimic2v30.icustayevents ie

  -- get more information regarding each ICU stay
  inner join mimic2v30.patients pat
    on ie.subject_id = pat.subject_id
  inner join mimic2v30.ADMISSIONS adm
    on ie.subject_id = pat.subject_id and ie.hadm_id = adm.hadm_id

  -- only adults
  where extract(YEAR from ie.intime) - extract(YEAR from pat.dob) > 1

  -- filter to only patients admitted after call out data collection began
  and ie.hadm_id in
  (
    select hadm_id from mimic2v30_phi_release.admissions
    where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
)
, c2 as
(
select
co.icustay_id, co.intime, co.outtime
, co.admittime, co.dischtime
, ca.*

-- generate an integer which is 1 for the first callout event
, ROW_NUMBER() over (partition by co.icustay_id order by ca.createtime) as CALLOUT_NUM

from co
-- join to callout table using hospital admission identifier and times of ICU admit/discharge
left join mimic2v30.callout ca
  on co.hadm_id = ca.hadm_id and ca.createtime between co.intime and co.outtime

  -- do not join to cancelled callout events
  and ca.callout_outcome != 'Cancelled'

where HOSP_STAY = 1
)
select
count(icustay_id) as NumIID
, count(distinct icustay_id) as NumIID_unique
-- HADM_ID is sourced from the callout table in the above subquery
, count(hadm_id) as NumCallout
, count(distinct hadm_id) as NumCallout_unique
from c2
where CALLOUT_NUM = 1;
```

Now NumIID and NumIID_unique are identical at 27800. NumCallout and NumCallout_unique are identical at 21510.
The ICU stays without callout likely occur due to in ICU death.
The next step is to remove these patients.




 and (ii) any call outs subsequent to the first call out.




Now that we have defined our base cohort, let's put it into a temporary view so that we can conveniently access it in subsequent queries.

```sql
with ca as
(
select
  adm.SUBJECT_ID, adm.HADM_ID
  -- callout variables
  , call.createtime

  -- this is when a coordinator acknowledged the call out request
  , call.acknowledge_status, call.acknowledgetime

  -- this is the status of the call out
  , call.callout_status

  -- any updates done to the call out...
  , call.updatetime

  -- the final outcome (discharged or cancelled) for the call out
  , call.callout_outcome, call.outcometime
  from mimic2v30.admissions adm
  inner join mimic2v30.patients pat
    on adm.subject_id = pat.subject_id
  left join  mimic2v30.callout call
    on adm.subject_id = call.subject_id and adm.hadm_id = call.hadm_id
  where adm.hadm_id in
  (
  select hadm_id from mimic2v30_phi_release.admissions
  where admittime > (select min(createtime) from mimic2v30_phi_release.callout)
  )
  and months_between(adm.admittime,pat.dob) > 1
)
select * from ca;
```

This query defines our temporary table, ca, which will be referenced in all the subsequent queries.

## Missing callout data

```sql
select *
from ca
where ca.createtime is null
order by hadm_id;
```

Let's pick one of the `HADM_ID` to investigate..



## Acknowledge status

Here we investigate ACKNOWLEDGE_STATUS:

```sql
select ca.acknowledge_status, count(*)
from ca
group by acknowledge_status;
```

ACKNOWLEDGE_STATUS | COUNT
---- | ----
Acknowledged | 32671
 | 7445
Unacknowledged | 1079
Revised | 649
Reactivated	| 52

There's a lot of NULL values (7445) - these are `HADM_ID` with no data in the CALLOUT table.

##


<!--
When ACKNOWLEDGE_STATUS = 'Revised', ACKNOWLEDGETIME is always null.
-->


<!--
UNSOLVED QUESTIONS:

There are 10,140 rows with all NULL data. Why do these occur in a table of only ~44000 rows?

-->
