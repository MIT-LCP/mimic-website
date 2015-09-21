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

## Overview 

This tutorial provides an introduction to the database structure and content. It also provides an idea of the types of informatino which can be extracted and the complexity of the data contained. By the end of this tutorial you will be able to: 

* Obtain meta-data from the various database objects (Tables, views, etc). 
* Perform basic queries on a single table. This includes counting the number of rows, and restricting the query to a subset of rows. 
* Perform basic 'joins' to combine tables and extract useful information. 
* Use database 'views' to extract high-level information. 

Commence the tutorial by opening the [QueryBuilder](https://mimic2app.csail.mit.edu/querybuilder/) application. 

``` sql
SELECT *
FROM noteevents
```
