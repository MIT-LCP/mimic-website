+++
date = "2015-10-08T07:01:22-04:00"
title = "Multiple callouts"
draft = true
linktitle = "Multiple callouts"
weight = 1
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

This query forms our base cohort.


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

So clearly we have quite a few ICU admissions who do not have an entry in the call out table: almost 20%!

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

# Base cohort

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
