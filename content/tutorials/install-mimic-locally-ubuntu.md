+++
date = "2015-09-01T14:02:13-04:00"
title = "Install MIMIC (Unix/Mac)"
linktitle = "Install MIMIC (Unix/Mac)"
weight = 1
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"
+++

# Installing MIMIC-III in a local Postgres database

Prerequisites: *This tutorial assumes that you have already completed the [steps required to gain access](/gettingstarted/access) to the MIMIC dataset on PhysioNet.*

Note that this install was written and tested using Mac OS X and Ubuntu 15.04. If you feel there are key details missing, please [raise an issue](https://github.com/MIT-LCP/mimic-website/issues) with your suggested improvements - we would love to incorporate them!

There are two options for installing MIMIC-III locally in a PostgreSQL database:

1. Manually, by following the tutorial below
2. Automatically, using the make files available in the [mimic-code repository](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic/postgres)

These steps are roughly equivalent, though you may learn more about the database configuration by installing the data manually.

## 0. Prepare

Note that before proceeding with this tutorial you will need to:

1. Download the MIMIC-III Clinical Database (see [here](/gettingstarted/access/) for details on gaining access).
2. Place the MIMIC-III Clinical Database as either .csv or .csv.gz files somewhere on your local computer.
3. Download the PostgreSQL scripts from [here](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic/postgres) - only the files which end in `.sql` are required.

It's easiest to move all the MIMIC data files and the scripts to load the data into a single folder (usually called the working directory). Most of the commands below will assume that files are located in the current folder.

## 1. Install Postgres

Postgres (also known as PostgreSQL) is a database management system. To create an instance of MIMIC-III on your local machine, you'll first need to make sure that Postgres is installed. For installation, please refer to: http://www.postgresql.org/download/

On Mac OSX with the [Homebrew package manager](http://brew.sh/), simply type ```brew install postgres```. On Ubuntu Linux, try ```sudo apt-get install postgresql```.

## 2. Place the CSV data files in a local directory

Assuming that you have completed the [steps required to gain access](/gettingstarted/access) to the MIMIC dataset, you should be able to access the CSV data files on PhysioNet at: https://physionet.org/works/MIMICIIIClinicalDatabase/files/.

Download these files to a local folder and decompress them if desired (it is possible to load the data directly into a database from compressed data files). The program `gzip` can be used to decompress the data (e.g. ```gzip -d *.gz```).


## 3. Create a user to access the data

It's bad practice to use a superuser account for day to day querying as you may accidentally drop raw data or something similar which would take effort to rectify.

To avoid this issue, we will create a user account on the database with the same username as the operating system user. To find out the local operating system username, type the following in the terminal:

```bash
whoami
```

That should return a username. For the rest of this tutorial, we will use `mimicuser`, but it's recommended to replace this with your local username. If you do, you can use operating system authentication and avoid having to password protect the user for the database. We can use a terminal command to create the user:

```bash
createuser -P -s -e -d mimicuser
```

This user is a superuser - we will remove this privilege later.

## 4. Connect to the database with psql

Now that Postgres is running, you should be able to connect to the system using the ```psql``` command line tool. With new installations, the default database name is 'postgres', so try connecting with:

``` bash
# connect to the default database 'postgres'
psql -U username -d postgres
```

## 5. Create an empty database containing a MIMIC-III schema

From this point onwards we will be referring to scripts in the '[buildmimic](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic)' directory of the [MIMIC code repository](https://github.com/MIT-LCP/mimic-code/).
You should have already downloaded the SQL scripts to your working directory.

After connecting with psql, create a new database called "mimic":

``` psql
CREATE DATABASE mimic OWNER mimicuser;
```

## 6. (Optional, recommended) Create a schema to hold the data

Note that postgres uses the `public` schema by default. We recommend creating an independent schema to host the data. To do this, create the mimiciii schema:

```
\c mimic;
CREATE SCHEMA mimiciii;
```

In the future, you will need to inform postgres that it should use the `mimiciii` schema.

```
set search_path to mimiciii;
```

**You will need to run the above every time you launch psql**.

## 7. Create a set of empty tables on a mimiciii schema, ready to populate with the data

Refer to the '[postgres_create_tables](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic/postgres)' script in the MIMIC code repository to create the mimiciii schema and then build a set of empty tables. Each table is created by running a ```CREATE TABLE``` command in psql.

First, exit from psql with `\q` which should bring you back to the shell command prompt. Now run the "[postgres\_create\_tables.sql](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_create_tables.sql)" script as follows:

``` bash
# Run the following command to create tables on the mimiciii schema
# postgres_create_tables.sql must be in your local directory
psql 'dbname=mimic user=mimicuser options=--search_path=mimiciii' -f postgres_create_tables.sql
```

If the script runs successfully, you should see the following output:

``` bash
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
... etc
```


If you get the error `postgres_create_tables.sql: No such file or directory` that means that the file `postgres_create_tables.sql` is not in your current directory. Either download the file to the local directory, or specify the directory in the above command.

If you see warnings about being unable to drop tables, don't worry, this is expected (see [#224](https://github.com/MIT-LCP/mimic-code/issues/224)).

## 8. Import the CSV data files into the empty tables

Using the [Postgres ```COPY``` or ```\COPY``` commands](https://wiki.postgresql.org/wiki/COPY), you should now be able to import the CSV data into the empty set of tables. You can run the "[postgres\_load\_data.sql](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_load_data.sql)" script from the command prompt using:

``` sql
# Load the data into the mimic database
# Replace <path_to_data> with the directory containing the MIMIC-III CSV files
psql 'dbname=mimic user=mimicuser options=--search_path=mimiciii' -f postgres_load_data.sql -v mimic_data_dir='<path_to_data>'
```

If the script runs successfully, you should see the following output:

``` bash
COPY 58976
COPY 34499
COPY 7567
COPY 0
... etc
```

*Importing the data can be slow, particularly for larger tables like CHARTEVENTS which may take several hours.*

Note also that above, we have included a line which states `COPY 0`. This is expected: CHARTEVENTS acts as a "mapping" table to multiple sub-tables, and no data is actually stored within it, so postgres reports that 0 rows were inserted. **This is expected behaviour for CHARTEVENTS.**

## 9. Add indexes to improve performance

Indexes provide additional structure for the database that can help to improve the speed of queries. The MIMIC code repository [includes a script with a set of suggested indexes](https://github.com/MIT-LCP/mimic-code/blob/master/buildmimic/postgres/postgres_add_indexes.sql). As before, you can run this script from the command line:

``` bash
# create indexes
psql 'dbname=mimic user=mimicuser options=--search_path=mimiciii' -f postgres_add_indexes.sql
```

## 10. Run checks

We have included a script which verifies all rows have been loaded in. Run those checks now:

```bash
# create indexes
psql 'dbname=mimic user=mimicuser options=--search_path=mimiciii' -f postgres_checks.sql
```

If all tables have the expected number of rows, you should see the phrase 'PASSED' for every table.

## 11. MIMIC-III is ready for analysis

You should now have a working copy of MIMIC-III ready to query with the psql command line tool. First start the PSQL client from the command line:

``` bash
psql 'dbname=mimic user=mimicuser options=--search_path=mimiciii'
```

Before going further, you should grant all privileges needed to the mimic user, then revoke the superuser privilege:

``` sql
grant select on all tables in schema mimiciii to mimicuser;
grant usage on schema mimiciii to mimicuser;
grant connect on database mimic to mimicuser;
alter user mimicuser nosuperuser;
```

Now try, for example, counting the number of patients in the database:

``` sql
select count(subject_id)
from mimiciii.patients;
```

Note that, because we specified the search_path in the connection string above (`--search_path=mimiciii`), we can omit it in the query:


``` sql
select count(subject_id)
from patients;
```

## 12. Install a graphical user interface (optional)

It is sometimes convenient to use a graphical user interface (GUI) for working with the database. There are a few options here:

* pgadmin - http://www.pgadmin.org/download/
* dbeaver - https://dbeaver.jkiss.org/
* valentina - https://www.valentina-db.com/en/

<!--
On Mac OSX with the [Homebrew package manager](http://brew.sh/), install PgAdminIII with ```brew install cask pgadmin3``` ('brew cask' is a tool for installing non-command-line packages). On Ubuntu Linux, try ```sudo apt-get install pgadmin3```.

Once PgAdminIII is installed, it can be connected to your local MIMIC instance. The tool offers a simple point and click interface for exploring the data and running queries.

![PgAdminIII screenshot](/img/tutorial_pgadminIII.png)
-->
