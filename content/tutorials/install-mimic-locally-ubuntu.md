+++
date = "2015-09-01T14:02:13-04:00"
title = "Install MIMIC-III - Ubuntu/Mac OS X"
linktitle = "Install MIMIC-III - Ubuntu/Mac OS X"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"
+++

# Installing MIMIC-III in a local Postgres database

Prerequisites: *This tutorial assumes that you have already completed the [steps required to gain access](/gettingstarted/access) to the MIMIC dataset on PhysioNet.*

Note that this install was written and tested using Mac OS X and Ubuntu 15.04.

## 1. Install Postgres

Postgres (also known as PostgreSQL) is a database management system. To create an instance of MIMIC-III on your local machine, you'll first need to make sure that Postgres is installed. For installation, please refer to: http://www.postgresql.org/download/

On Mac OSX with the [Homebrew package manager](http://brew.sh/), simply type ```brew install postgres```. On Ubuntu Linux, try ```sudo apt-get install postgresql-9.4```.

## 2. Place the CSV data files in a local directory

Assuming that you have completed the [steps required to gain access](/gettingstarted/access) to the MIMIC dataset, you should be able to access the CSV data files on PhysioNet at: https://physionet.org/works/MIMICIIIClinicalDatabase/files/.

Download these files to a local folder and decompress them if necessary (from the command line, run ```gzip -d *.gz``` in the directory containing the files).

## 3. Connect to the database with psql

Now that Postgres is running, you should be able to connect to the system using the ```psql``` command line tool. With new installations, the default database name is 'postgres', so try connecting with:

``` bash
# connect to the default database
psql postgres
```

## 4. Create an empty database containing a MIMIC-III schema

From this point onwards we will be referring to scripts in the '[buildmimic](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic)' directory of the [MIMIC code repository](https://github.com/MIT-LCP/mimic-code/).

After connecting with psql, create a new user called "mimic", with temporary superuser privileges. Next, create a new database called "mimic":

``` psql
CREATE USER mimic;
ALTER USER mimic superuser;
CREATE DATABASE mimic OWNER mimic;
```

## 5. Create a set of empty tables on a mimiciii schema, ready to populate with the data

Refer to the '[postgres_create_tables](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic/postgres)' script in the MIMIC code repository to create the mimiciii schema and then build a set of empty tables. Each table is created by running a ```CREATE TABLE``` command in psql.

First, exit from psql with "\q" which should bring you back to the shell command prompt. Now run the "[postgres\_create\_tables.sql](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_create_tables.sql)" script as follows:

``` bash
# Run the following command to create the mimiciii schema and tables
# postgres_create_tables.sql must be in your local directory
psql -f postgres_create_tables.sql -U mimic
```

If the script runs successfully, you should see the following output:

``` bash
CREATE SCHEMA
SET
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
... etc
```

## 6. Import the CSV data files into the empty tables

Using the [Postgres ```COPY``` or ```\COPY``` commands](https://wiki.postgresql.org/wiki/COPY), you should now be able to import the CSV data into the empty set of tables. You can run the "[postgres\_load\_data.sql](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_load_data.sql)" script from the command prompt using:

``` sql
# Load the data into the mimic database
# Replace <path_to_data> with the directory containing the MIMIC-III CSV files
psql -f postgres_load_data.sql -U mimic -v mimic_data_dir='<path_to_data>'
```

If the script runs successfully, you should see the following output:

``` bash
SET
COPY 58976
COPY 34499
COPY 7567
... etc
```

*Importing the data can be slow, particularly for larger tables like CHARTEVENTS which may take several hours.*

## 7. Add indexes to improve performance

Indexes provide additional structure for the database that can help to improve the speed of queries. The MIMIC code repository [includes a script with a set of suggested indexes](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_add_indexes.sql). As before, you can run this script from the command line:

``` bash
# create indexes
psql -f postgres_add_indexes.sql -U mimic
```

## 8. MIMIC-III is ready for analysis

You should now have a working copy of MIMIC-III ready to query with the psql command line tool. First start the PSQL client from the command line:

``` bash
psql -U mimic
```

Now connect to the MIMIC database:

``` sql
-- connect to the mimic database
\c mimic
```

Before going further, you should revoke the superuser privileges from the mimic user:

``` sql
alter user mimic nosuperuser;
```

Now try, for example, counting the number of patients in the database:

``` sql
select count(subject_id)
from mimiciii.patients;
-- returns x rows
```

## 9. Install PgAdminIII (optional)

PgAdmin is a graphical user interface ('GUI') tool for administering Postgres databases. For installation guidelines see: http://www.pgadmin.org/download/

On Mac OSX with the [Homebrew package manager](http://brew.sh/), install PgAdminIII with ```brew install cask pgadmin3``` ('brew cask' is a tool for installing non-command-line packages). On Ubuntu Linux, try ```sudo apt-get install pgadmin3```.

Once PgAdminIII is installed, it can be connected to your local MIMIC instance. The tool offers a simple point and click interface for exploring the data and running queries.

![PgAdminIII screenshot](/img/tutorial_pgadminIII.png)
