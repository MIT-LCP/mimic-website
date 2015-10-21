+++
date = "2015-09-01T14:02:13-04:00"
title = "Install MIMIC locally"
linktitle = "Install MIMIC locally"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"
+++

# How to install MIMIC-III in a local Postgres database

Prerequisites: *This tutorial assumes that you have already completed the [steps required to gain access](/gettingstarted/access) to the MIMIC dataset on PhysioNet.*

## 1. Install Postgres

Postgres (also known as PostgreSQL) is a database management system. To create an instance of MIMIC-III on your local machine, you'll first need to make sure that Postgres is installed. For installation, please refer to: http://www.postgresql.org/download/

On Mac OSX with the [Homebrew package manager](http://brew.sh/), simply type ```brew install postgres```. On Ubuntu Linux, try ```sudo apt-get install postgresql-9.4```.

## 2. Place the CSV data files in a local directory

Assuming that you have completed the [steps required to gain access](/gettingstarted/access) to the MIMIC dataset, you should be able to access the CSV data files on PhysioNet at: https://physionet.org/works/MIMICIIIClinicalDatabase/files/. Download these files to a local folder and decompress them if necessary.

## 3. Connect to the database with psql

Now that Postgres is running, you should be able to connect to the system using the ```psql``` command line tool. With new installations, the default database name is 'postgres', so try connecting with:

``` bash
# connect to the default database
psql postgres 
```

## 4. Create an empty database containing a MIMIC-III schema

From this point onwards we will be referring to scripts in the '[buildmimic](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic)' directory of the [MIMIC code repository](https://github.com/MIT-LCP/mimic-code/).

After connecting with psql, create a new user. Next, create a MIMIC database with a schema for MIMIC-III:

``` bash
CREATE USER MIMIC;
CREATE DATABASE MIMIC OWNER MIMIC;
# connect to the database
\c MIMIC
CREATE SCHEMA MIMICIII;
```

## 5. Create a set of empty tables, ready to populate with the data

Refer to the '[postgres_create_tables](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic/postgres)' script in the MIMIC code repository to build a set of empty tables. Each table is created by running a ```CREATE TABLE``` command in psql. For example, the caregivers table is created with:

``` psql
-- drop the table if it already exists
DROP TABLE MIMICIII.CAREGIVERS;

-- create the table
CREATE TABLE MIMICIII.CAREGIVERS
    (    ROW_ID INT NOT NULL, 
    CGID INT NOT NULL, 
    LABEL VARCHAR(15), 
    DESCRIPTION VARCHAR(30),
    CONSTRAINT cg_rowid_pk  PRIMARY KEY (ROW_ID),
    CONSTRAINT cg_cgid_unique UNIQUE (CGID)
    );
```

## 6. Import the CSV data files into the empty tables

Using the [Postgres ```COPY``` or ```\COPY``` commands](https://wiki.postgresql.org/wiki/COPY), you should now be able to import the CSV data into the empty set of tables. If the CSV files are contained in your current working directory, then either of the following commands should import the caregivers table:

Option 1: import with ```\COPY```

``` sql
\COPY mimiciii.caregivers from 'CAREGIVERS_DATA_TABLE.csv' with DELIMITER ',' CSV HEADER
```

Option 2: import with ```COPY```

``` sql
COPY MIMICIII.CAREGIVERS 
    FROM '/path/to/file/CAREGIVERS_DATA_TABLE.csv' 
    DELIMITER ',' 
    CSV HEADER;
```

*Importing the data can be slow, particularly for larger tables like CHARTEVENTS which may take several hours.*

## 7. Add indexes to improve performance

Indexes provide additional structure for the database that can help to improve the speed of queries. The MIMIC code repository [includes a script with a set of suggested indexes](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_add_indexes.sql). For example, an index on subject_id and hadm_id can be created for the ADMISSIONS table with the following command:

``` sql
-- drop the existing index if it exists
drop index MIMICIII.ADMISSIONS_idx01;

-- create the index
CREATE INDEX ADMISSIONS_IDX01 
  ON MIMICIII.ADMISSIONS (SUBJECT_ID,HADM_ID);
``` 

## 8. MIMIC-III is ready for analysis

You should now have a working copy of MIMIC-III ready to query with the psql command line tool. Try, for example, counting the number of patients in the database:

``` sql
select count(subject_id)
from MIMICIII.PATIENTS;
-- returns x rows
```

## 9. Install PgAdminIII (optional) 

PgAdmin is a graphical user interface ('GUI') tool for administering Postgres databases. For installation guidelines see: http://www.pgadmin.org/download/

On Mac OSX with the [Homebrew package manager](http://brew.sh/), install PgAdminIII with ```brew install cask pgadmin3``` ('brew cask' is a tool for installing non-command-line packages). On Ubuntu Linux, try ```sudo apt-get install pgadmin3```.

Once PgAdminIII is installed, it can be connected to your local MIMIC instance. The tool offers a simple point and click interface for exploring the data and running queries.

![PgAdminIII screenshot](/img/tutorial_pgadminIII.png)






