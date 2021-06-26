---
title: "Core"
linkTitle: "Core"
date: 2020-08-10
weight: 10
description: >
  The Core module contains patient tracking data. Demographics, hospital admissions, and in-hospital ward transfers are described here.
---

The Core module contains three tables: patients, admissions, and transfers. These tables provide demographics for the patient, a record for each hospitalization, and a record for each ward stay within a hospitalization.

Notably, the patients table provides timing information for each patient through the anchor_year and anchor_year_group columns. The anchor_year is a deidentified year occurring sometime between 2100 - 2200, and the anchor_year_group is a three year long date ranges between 2008 - 2019. These pieces of information allow researchers to infer the approximate year a patient received care. For example, if a patient's anchor_year is 2158, and their anchor_year_group is 2011 - 2013, then any hospitalizations for the patient occurring in the year 2158 actually occurred sometime between 2011 - 2013. Finally, the anchor_age provides the patient age in the given anchor_year. If the patient was over 89 in the anchor_year, this anchor_age has been set to 91 (i.e. all patients over 89 have been grouped together into a single group with value 91, regardless of what their real age was).
