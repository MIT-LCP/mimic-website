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

* Obtain metadata from the various database objects (tables, views, etc). 
* Perform basic queries on a single table. This includes counting the number of rows, and restricting the query to a subset of rows. 
* Perform basic 'joins' to combine tables and extract useful information. 
* Use database 'views' to extract high-level information. 

Tutorial coming soon...

<!-- 

Commence the tutorial by opening the [QueryBuilder](https://mimic2app.csail.mit.edu/querybuilder/) application. 

## 2. Database metadata 

The metadata for a particular table can be obtained by clicking on an entry on the left hand side of the screen. Select the patients table to see how the metadata is displayed in the panels on the right hand side of the screen. The columns found in the patients table are displayed, along with the types of data they contained, and various other parameters. Also provided are comments which describe the data contained in the columns. 

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
SELECT DISTINCT gender 
FROM patients
```

We can see that 'M' and 'F' are the two characters used to indicate patient gender. We can use this information to obtain the number of female patients by restricting the query to retrieve results which have 'F' in the 'gender' column: 

``` sql
SELECT COUNT(*) 
FROM patients
WHERE gender = 'F'
```

And the numbers of male and female patients can be obtained using this query: 

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

The database also contains date of death for patients FIX FIX FIX who died outside the hospital, based on social security death records FIX FIX FIX. This information is contained in the 'dod' column. Please note that this database contains adult, pediatric, and neonatal patients which will affect the mortality statistics. Categorizing patients into different age groups is carried out in the next section. 

## 5. Patient age and Mortality 

To determine the adult mortality rate, we must first determine adult patients. We define adults as those patients who are 15 or more years old at the date of their first admission. To perform this query, we must first combine the patients and admissions tables to find patient admission dates, and their date of birth. Please note that the table naming in the query below. We have denoted 'admissions' with 'a' and 'patients' with 'p': 

``` sql
SELECT p.subject_id, p.dob, a.hadm_id, a.admittime, p.hospital_expire_flag 
FROM admissions a
INNER JOIN patients p
ON p.subject_id = a.subject_id
```

Next, we find the minimum(earliest) admission date for each patient. This requires the use of the new functions, the 'MIN' function, which obtains the minimum value, and the 'PARTITION BY' function which determines the groups over which the minimum value is obtained, in this case, we determine the minimum time of admission for each patient: 

``` sql
SELECT DISTINCT p.subject_id, p.dob, a.hadm_id, a.admittime, p.hospital_expire_flag, 
MIN (a.admittime)
OVER (PARTITION BY p.subject_id)
AS first_admitdate
FROM admissions a 
INNER JOIN patients p 
ON p.subject_id = a.subject_id 
AND p.dob IS NOT NULL 
ORDER BY a.hadm_id, p.subject_id 
```

A patient's age is given by the difference between their date of birth and the date of their first admission. We can obtain this by combining the above query with another query to provide the ages. Furthermore, we assign categories to different ages: >= 15 years old are adults and the rest are assigned to the 'other' category. The queries are combined using the 'WITH' keyword: 

``` sql 
WITH first_admission_date AS(
SELECT DISTINCT p.subject_id, p.dob, p.gender, a.hadm_id, a.admittime,
MIN (a.admittime)
OVER (PARTITION BY a.hadm_id, p.subject_id)
AS first_admitdate
FROM admissions a 
INNER JOIN patients p 
ON p.subject_id = a.subject_id
AND p.dob IS NOT NULL 
ORDER BY a.hadm_id, p.subject_id
), 
age AS (
SELECT subject_id, hadm_id, dob, gender, first_admitdate, 
ROUND(months_between(first_admitdate, dob) /12,2) first_admit_age,
CASE 
WHEN (months_between(first_admitdate,dob) /12) >= 15
THEN 'adult'
WHEN months_between(first_admitdate,dob) <=1
THEN 'neonate'
ELSE 'middle'
END AS age_group
FROM first_admission_date
ORDER BY subject_id,hadm_id
)
SELECT * FROM age
```

The above query can now be combined with the **WHERE** and **COUNT** functions described earlier to determine the number of adult patients, whether or not they died, and therefore, their mortality rate.

-->

