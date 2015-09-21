+++
date = "2015-09-01T14:02:13-04:00"
title = "Intro to MIMIC-III"
draft = true
linktitle = "Intro to MIMIC-III"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"

+++

# Introduction to MIMIC-III

## 1. Overview 

This tutorial provides an introduction to the database structure and content. It also provides an idea of the types of informatino which can be extracted and the complexity of the data contained. By the end of this tutorial you will be able to: 

* Obtain meta-data from the various database objects (Tables, views, etc). 
* Perform basic queries on a single table. This includes counting the number of rows, and restricting the query to a subset of rows. 
* Perform basic 'joins' to combine tables and extract useful information. 
* Use database 'views' to extract high-level information. 

Commence the tutorial by opening the [QueryBuilder](https://mimic2app.csail.mit.edu/querybuilder/) application. 

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
