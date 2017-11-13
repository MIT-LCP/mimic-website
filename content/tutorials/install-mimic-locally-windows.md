+++
date = "2016-02-06T07:30:21-04:00"
title = "Install MIMIC (Windows)"
linktitle = "Install MIMIC (Windows)"
weight = 2
toc = "true"

[menu]
  [menu.main]
    parent = "Tutorials"
+++

# Installing MIMIC-III in a local Postgres database on Windows

These are relatively brief instructions provided to ease installation of PostgreSQL with MIMIC on a Windows machine. If you feel there are key details missing, please [raise an issue](https://github.com/MIT-LCP/mimic-website/issues) with your suggested improvements - we would love to incorporate them!

Note that before proceeding with this guide you will need to:

1. Download the MIMIC-III Clinical Database (see [here](/gettingstarted/access/) for details on gaining access).
2. Extract the MIMIC-III Clinical Database as .csv files somewhere on your local computer.
3. Download the PostgreSQL scripts from [here](https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic/postgres) - only the files which end in `.sql` are required.

## Install PostgreSQL

Install PostgreSQL using the installer linked to here:
http://www.postgresql.org/download/windows/

Run through the entire install process - remember your postgres user password as you will need it later.

## Run SQL Shell (psql)

Open up the SQL shell program. Log-in as user postgres (and use the password you specified during the install process).

### Create the database to hold the data

Run the following commands:

```sql
DROP DATABASE IF EXISTS mimic;
CREATE DATABASE mimic OWNER postgres;
```

This creates the database `mimic`, owned by user `postgres`. Of course you are welcome to change these values if you like - just note that any changes here will require further changes in the subsequent steps.

Next, connect to the `mimic` database.

```sql
\c mimic;
```


### Create the tables on the database

Note that postgres uses the `public` schema by default. While it is personal preference, we recommend creating an independent schema to host the data. To do this, create the mimiciii schema:

```
CREATE SCHEMA mimiciii;
```

Then, inform postgres that it should by default use the `mimiciii` schema. **You will need to do this every time you launch psql**.

```
set search_path to mimiciii;
```

Now run the create tables script (note: this assumes that the create table script is in the current directory - if it is not, see below).

```sql
\i postgres_create_tables.sql
```

If you get the error `postgres_create_tables.sql: No such file or directory` that means that the file `postgres_create_tables.sql` is not in your current directory. Specify the path to the file. In my case, I wrote:

```sql
\i D:/work/mimic-code/buildmimic/postgres/postgres_create_tables.sql
```

If you see a lot of "NOTICE: table does not exist" don't worry, that's normal. The script tries to delete the table before it creates it.

### Import the data into the tables

Run the following command import the data into these tables:

```sql
\set ON_ERROR_STOP 1
\set mimic_data_dir 'D:/mimic/v1_4'
\i D:/work/mimic-code/buildmimic/postgres/postgres_load_data.sql
```

Note I have specified a folder, `'D:/mimic/v1_4'`. This folder contains all the CSV files which store MIMIC. This should begin the load process, which takes some time.

### Add indexes

After the load finishes, it is recommended to install indexes to improve the speed of queries on the database.
These can be installed by running the following:

```sql
\i D:/work/mimic-code/buildmimic/postgres/postgres_add_indexes.sql
```

While you have the option of building constraints (using `postgres_add_constraints.sql`) these are mainly used for data integrity checking during the creation of the data - it is not necessary to run this file on your local installation.

### Test your build

You should now be able to query MIMIC-III! Try the following simple query:

```sql
select
  icustay_id, intime, outtime
from icustays
limit 10;
```

If you'd like to verify everything loaded correctly, you can run the check script:

```sql
\i D:/work/mimic-code/buildmimic/postgres/postgres_checks.sql
```

### (Optional) Add comments

We have provided a script to add comments to all the tables/columns in MIMIC-III. Run the following to add these comments:


```sql
\i D:/work/mimic-code/buildmimic/postgres/postgres_add_comments.sql
```

You may also find the [introduction to MIMIC-III](/tutorials/intro-to-mimic-iii/) guide useful. Good luck in your research!
