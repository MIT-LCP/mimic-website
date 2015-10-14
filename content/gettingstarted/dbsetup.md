+++
date = "2015-09-01T14:02:13-04:00"
title = "Setting up the database"
linktitle = "Setting up the database"
weight = 2
toc = "false"

[menu]
  [menu.main]
    parent = "Getting started"

+++

# Setting up the database

## Creating a local version of MIMIC from the CSV files

Once your [application to access MIMIC](http://mimic.physionet.org/gettingstarted/access/) has been approved, you will be granted access to the 'MIMIC-III Clinical Database' project page on PhysioNet:
https://physionet.org/works/MIMICIIIClinicalDatabase/

MIMIC is provided as a collection of comma-separated (CSV) files, along with scripts to help users import the data into popular database systems. Scripts are available in the [MIMIC code repository](https://github.com/MIT-LCP/mimic-code) for Postgres, MySQL, and Oracle:
https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic

For a tutorial on installing MIMIC in a local Postgres database, see:
http://mimic.physionet.org/tutorials/install_mimic_locally/

## Creating and connecting to a cloud version of MIMIC with Amazon Relational Database Service (RDS)

Amazon Relational Database Service allows a relational database to be created on a remote cloud server. Tutorial to follow...

## Creating a cloud version of MIMIC with Microsoft Azure

Microsoft Azure's SQL Database allows a relational database to be created on a remote cloud server. Tutorial to follow...









