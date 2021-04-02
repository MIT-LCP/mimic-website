+++
date = "2016-09-01T19:34:46-04:00"
title = "MIMIC Querybuilder"
aliases = "/gettingstarted/querybuilder/"
linktitle = "Querybuilder"
weight = 1
toc = "true"

+++

The MIMIC Querybuilder is a graphical interface for running SQL queries on the MIMIC-III database. It is intended for light exploration of the data, in particular for researchers who are new to MIMIC-III and seeking to gain an understanding of its structure. Researchers seeking to carry out research projects with MIMIC should [follow our instructions](/iii/gettingstarted/dbsetup/) for building a local version of the database. 

## Notes and limitations

Queries should be written using PostgreSQL syntax. Two key limitations have been implemented to manage server load:

- The system has been intentionally limited to return only the first 5000 rows of a query  
- All queries have a maximum running time of 15 minutes. Queries that run for over 15 minutes will time out, returning no results.  

While we will aim to provide a stable service, our laboratory has limited resources and so we cannot commit to providing continuous uptime.

## Access Querybuilder

Querybuilder is available via the following link, using the PhysioNetWorks username (email address) and password provided to you upon being [granted access](/iii/gettingstarted/access/): https://querybuilder-lcp.mit.edu/


