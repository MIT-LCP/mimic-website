+++
date = "2015-09-01T14:02:13-04:00"
title = "Intro to MIMIC-III"
draft = false
linktitle = "Intro to MIMIC-III"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++

# Introduction to MIMIC-III

## 1. Overview 

This tutorial provides an introduction to the database structure and content. It also provides an idea of the types of information which can be extracted and the complexity of the data contained. By the end of this tutorial you will be able to: 

* Obtain meta-data from the various database objects (Tables, views, etc). 
* Perform basic queries on a single table. This includes counting the number of rows, and restricting the query to a subset of rows. 
* Perform basic 'joins' to combine tables and extract useful information. 
* Use database 'views' to extract high-level information. 

## 2. Database meta-data 

The meta-data for a particular table can be obtained by clicking on an entry on the left hand side of the screen. Select the patients table to see how the metadata is displayed in the panels on the right hand side of the screen. The columns found in the patients table are displayed, along with the types of data they contained, and various other parameters. Also provided are comments which describe the data contained in the columns. 

Try selecting some other tables and look at the metadata. You can close a tab by clicking on the 'X' on the metadata tabs. When you have finished, close all of the metadata tabs and go to No.3

## 3. Patient Numbers 

Ensure that the 'Query...' tab at the top of the screen is selected. SQL queries can be entered in the top panel and the results will be displayed at the bottom when the 'Execute query' button is pressed. Enter the following SQL in the box and press the 'Execute query' button. 

``` sql
SELECT * 
FROM patients
```

At the bottom of the screen you will see three columns: subject_id, gender, and date of birth. 50 records are retrieved at a time and you can page through the results using the controls at the bottom of the screen. 

Obtain the number of patients by performing the following query: 

``` sql
SELECT COUNT(*)
FROM patients
```

The 'gender' column identifies the gender of the patient. We can obtain the values used to indicate patient genders using the following query: 

``` sql
SELECT gender 
FROM patients
```

We can see that 'M' and 'F' are the two characters used to indicate patient gender. We can use this information to obtain the number of female patients by restricting the query to retrieve results which have 'F' in the 'gender' column: 

``` sql
SELECT COUNT(*) 
FROM patients
WHERE gender = 'F'
```

And the numbers of male and female patients can be obtained using this query which counts how many female and male patients are in the patients table. 

``` sql
SELECT gender, COUNT(*)
FROM patients
GROUP BY gender
```

## 4. Mortality and Admissions 

A flag which records whether or not a patient died in the hospital is stored in the patients table. Count the number of patients who died using the following query: 

``` sql
SELECT hospital_expire_flag, COUNT(*)
FROM patients
GROUP BY hospital_expire_flag
```

The database also contains date of death for patients who died inside the hospital in the column 'dod_hosp' and the date of death found in social security death records in 'dod_ssn'. This information from both columns is merged in the 'dod' column with priority given to 'dod_hosp'. Please note that this database contains adult and neonatal patients which will affect the mortality statistics. Categorizing patients into different age groups is carried out in the next section. 

## 5. Patient age and Mortality 

To determine the adult mortality rate, we must first determine adult patients. We define adults as those patients who are 15 or more years old at the date of their first admission. To perform this query, we must first combine the patients and admissions tables to find patient admission dates, and their date of birth. Please note that the table naming in the query below. We have denoted 'admissions' with the alias 'a' and 'patients' with alias 'p': 

``` sql
SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.hospital_expire_flag 
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id
```

Next, we find the minimum(earliest) admission date for each patient. This requires the use of the new functions, the 'MIN' function, which obtains the minimum value, and the 'PARTITION BY' function which determines the groups over which the minimum value is obtained, in this case, we determine the minimum time of admission for each patient: 

``` sql
SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.hospital_expire_flag, 
MIN (a.admittime)
OVER (PARTITION BY p.subject_id)
AS first_admittime
FROM admissions a 
INNER JOIN patients p 
ON p.subject_id = a.subject_id 
ORDER BY a.hadm_id, p.subject_id 
```

A patient's age is given by the difference between their date of birth and the date of their first admission. We can obtain this by combining the above query with another query to provide the ages. Furthermore, we assign categories to different ages: >= 15 years old are adults and the rest are assigned to the 'other' category. The queries are combined using the 'WITH' keyword: 

``` sql 
WITH first_admission_time AS(
SELECT p.subject_id, p.dob, p.gender, a.hadm_id, a.admittime,
MIN (a.admittime)
OVER (PARTITION BY a.hadm_id, p.subject_id)
AS first_admittime
FROM admissions a 
INNER JOIN patients p 
ON p.subject_id = a.subject_id
ORDER BY a.hadm_id, p.subject_id
), 
age AS (
SELECT subject_id, hadm_id, dob, gender, first_admittime, 
ROUND(months_between(first_admittime, dob) /12,2) first_admit_age,
CASE 
WHEN (months_between(first_admittime,dob) /12) >= 15
THEN 'adult'
WHEN months_between(first_admittime,dob) <=1
THEN 'neonate'
ELSE 'middle'
END AS age_group
FROM first_admission_time
ORDER BY subject_id,hadm_id
)
SELECT * FROM age
```

The above query can now be combined with the **WHERE** and **COUNT** functions described earlier to determine the number of adult patients, whether or not they died, and therefore, their mortality rate. 


## 6. ICU Stays 

In the MIMIC-III database, we define an ICU stay to be continuous if a patient is returned to an ICU room within 24 hours of being moved to a ward. Patient ICU movements are recorded in the transfers table: 

``` sql 
SELECT * FROM transfers
```

The columns should be fairly self explanatory, click on the transfers table on the left hand side if you need more information about the columns and the data they contain. The 'prev_careunit' and 'curr_careunit' contain the names of the previous and current careunit respectively. The transfers table also contains columns 'prev_wardid' and 'curr_wardid' which contain the IDs of the previous and current careunit respectively. Ward IDs which specify the room within a ward have no corresponding key in order to protect patient health information. 

The transfers table may have multiple entries per patient to provide information of all movement between various careunits of the hospital. The first entry in the transfers table for a patient who comes into the ICU will have nothing in the 'prev_careunit' column and similarly, the last entry for a patient will have nothing in the 'curr_careunit'. Patient entries that have nothing in both previous and current careunit columns signifies that patients have been transfered between units that do not fall under any of the ICUs. An example query for one patient and result from the transfers table is shown below. Note that columns 'intime', 'outtime', and 'los' have been truncated. 

```sql

SELECT * FROM mimicIII.transfers where HADM_ID = 112213;

```

row_id| subject_id | hadm_id | icustay_id | dbsource | eventtype | prev_careunit | curr_careunit | prev_wardid | curr_wardid
-------- | ------------ | --------- | ------------ | ----------- | ----------- | --------------- | --------------- | ------------- | -------------
   54 |         12 |  112213 |            | carevue    | admit     |               |               |             |          27
   55 |         12 |  112213 |            | carevue    | transfer  |               |               |          27 |           2 
   56 |         12 |  112213 |     232669 | carevue    | transfer  |               | SICU          |           2 |          23 
   57 |         12 |  112213 |            | carevue    | transfer  | SICU          |               |          23 |          49 
   58 |         12 |  112213 |     232669 | carevue    | transfer  |               | SICU          |          49 |          23 
   59 |         12 |  112213 |            | carevue    | transfer  | SICU          |               |          23 |          36 
   60 |         12 |  112213 |            | carevue    | discharge |               |               |          36 |            

<!-- talk about services --> 
## 7. Services 
Services is a newly added table in MIMIC-III which contains information about the transfers from being under one service to another during a patient's stay. The services table contains columns including 'prev_service' and 'curr_service' which contain the names of previous and current services respectively. 'transfertime' is the time at which the patient was moved from 'prev_service' to 'curr_service'. 

## 8. Tutorial Problem 
​
How would gather useful information about patients admitted to the ICU? 

The problem is problem is broken down into serveral parts and we recommend viewing the solution, which can be found below, after several attempts. 

# Step 1 
First start with retrieving 'subject_id', 'hadm_id', 'icustay_id', 'intime', and 'outtime' from the 'mimicIII' database 'icustayevents' table. 

# Step 2 
In addition to step 1, retrieve the caulcated age of patients by also using the patients table. 

# Step 3 
Now separate neonates from adult patients. 

# Step 4 
By incorporating the admissions table, find how long each stay was **BEFORE** the patients were admitted to the ICU 

# Step 5 
Next find the date of the patient's death if applicable. 

# Step 6 
Then find those deaths that occured while the patients were in the hospital 

# Step 7 
Find how many of those deaths occured within the ICU 


## Solutions to Tutorial Problem in No. 7

# Solution to Step 1 

``` sql 
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
from mimicIII.icustayevents ie;
```

# Solution to Step 2 

``` sql 
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age
from mimicIII.icustayevents ie
inner join mimicIII.patients pat
  on ie.subject_id = pat.subject_id;
  ```
  
# Solution to Step 3

``` sql 
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age
      , case 
          when months_between(ie.intime,pat.dob) <= 1 then 'neonate'
          when months_between(ie.intime,pat.dob) > 1 and months_between(ie.intime,pat.dob) <= 15*12 then 'middle'
          else 'adult' end as ICUSTAY_AGE_GROUP
from mimicIII.icustayevents ie
inner join mimicIII.patients pat
  on ie.subject_id = pat.subject_id;
```

# Solution to Step 4
``` sql 
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age
      
      , case 
          when months_between(ie.intime,pat.dob) <= 1 then 'neonate'
          when months_between(ie.intime,pat.dob) > 1 and months_between(ie.intime,pat.dob) <= 15*12 then 'middle'
          else 'adult' end as ICUSTAY_AGE_GROUP
          
      , round( ie.intime - adm.admittime , 2 ) as preICULOS
from mimicIII.icustayevents ie
inner join mimicIII.patients pat
  on ie.subject_id = pat.subject_id
inner join mimicIII.admissions adm
  on ie.hadm_id = adm.hadm_id;
  ```  

# Solution to Step 5

``` sql 
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age
      
      , case 
          when months_between(ie.intime,pat.dob) <= 1 then 'neonate'
          when months_between(ie.intime,pat.dob) > 1 and months_between(ie.intime,pat.dob) <= 15*12 then 'middle'
          else 'adult' end as ICUSTAY_AGE_GROUP
          
      , round( ie.intime - adm.admittime , 2 ) as preICULOS
      , adm.deathtime
from mimicIII.icustayevents ie
inner join mimicIII.patients pat
  on ie.subject_id = pat.subject_id
inner join mimicIII.admissions adm
  on ie.hadm_id = adm.hadm_id;
 ```

# Solution to Step 6
``` sql
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age
      
      , case 
          when months_between(ie.intime,pat.dob) <= 1 then 'neonate'
          when months_between(ie.intime,pat.dob) > 1 and months_between(ie.intime,pat.dob) <= 15*12 then 'middle'
          else 'adult' end as ICUSTAY_AGE_GROUP
          
      , round( ie.intime - adm.admittime , 2 ) as preICULOS
      , adm.deathtime
      
      , case when adm.discharge_location = 'DEAD/EXPIRED' then 'Y' else 'N' end
          as hospital_expire_flag
          
from mimicIII.icustayevents ie
inner join mimicIII.patients pat
  on ie.subject_id = pat.subject_id
inner join mimicIII.admissions adm
  on ie.hadm_id = adm.hadm_id;
  ```
  
# Solution to Step 7
``` sql 
select ie.subject_id, ie.hadm_id, ie.icustay_id
      , ie.intime
      , ie.outtime
      , round( months_between(ie.intime,pat.dob)/12 , 2 ) as age
      
      , case 
          when months_between(ie.intime,pat.dob) <= 1 then 'neonate'
          when months_between(ie.intime,pat.dob) > 1 and months_between(ie.intime,pat.dob) <= 15*12 then 'middle'
          else 'adult' end as ICUSTAY_AGE_GROUP
          
      , round( ie.intime - adm.admittime , 2 ) as preICULOS
      , adm.deathtime
      
      , case when adm.discharge_location = 'DEAD/EXPIRED' then 'Y' else 'N' end
          as hospital_expire_flag
        , case 
            when adm.deathtime between ie.intime and ie.outtime 
              then 'Y'
            when adm.deathtime <= ie.intime -- sometimes there are typographical errors in the death date
              then 'Y'
            when adm.dischtime <= ie.outtime and adm.discharge_location = 'DEAD/EXPIRED'
              then 'Y'
            else 'N' end 
          as ICUSTAY_EXPIRE_FLAG
          
          
from mimicIII.icustayevents ie
inner join mimicIII.patients pat
  on ie.subject_id = pat.subject_id
inner join mimicIII.admissions adm
  on ie.hadm_id = adm.hadm_id;
  ```
