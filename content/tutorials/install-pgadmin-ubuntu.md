+++
date = "2015-09-01T14:02:13-04:00"
title = "Intro to MIMIC-III"
draft = true
linktitle = "Intro to MIMIC-III"
weight = 1
toc = "true"

+++

# Quick guide on installing PostgreSQL on Ubuntu

```sh
lsb_release -a:
```

No LSB modules are available.

Distributor ID: Ubuntu

Description:    Ubuntu 15.04

Release:        15.04

Codename:       vivid

## Check what versions are available

It's a good first step to check you are installing the latest version. You can search for package versions as follows:

```sh
sudo apt-cache search postgres
```

For me, I saw:

```
pgadmin3
...
postgresql-9.4-asn1oid - ASN.1 OID data type for PostgreSQL
postgresql-9.4-debversion - Debian version number type for PostgreSQL
...
postgresql-9.4-slony1-2 - replication system for PostgreSQL: PostgreSQL 9.4 server plug-in
```

## Install PostgreSQL (aka Postgres)

### Install command

```sh
sudo apt-get install postgresql-9.4
```

### Login to psql and update the postgres user password

```sh
sudo -u postgres psql
```

```psql
ALTER USER postgres PASSWORD 'mimic';
```

### Exit psql

```psql
\q;
```

Note commands in psql begin with '\'.

### Run psql later on

```sh
psql -U postgres -h localhost
```

## pgadmin

### Installation

This is an optional step to get a user interface.

```
sudo apt-get install pgadmin3
```

### Running pgadmin

```sh
pgadmin
```
