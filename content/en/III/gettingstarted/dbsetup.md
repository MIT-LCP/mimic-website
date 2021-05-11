+++
date = "2015-09-01T14:02:13-04:00"
title = "Downloading the MIMIC-III database"
linktitle = "Downloading the database"
weight = 4
toc = "false"

+++

## PhysioNet  

Once your [application to access MIMIC](/iii/gettingstarted/) has been approved, you will be granted access to the 'MIMIC-III Clinical Database' project page on PhysioNet:  
https://physionet.org/content/mimiciii/

## Data and build scripts

MIMIC is provided as a collection of comma-separated (CSV) files, along with scripts to help users import the data into popular database systems. Scripts are available in the [MIMIC code repository](https://github.com/MIT-LCP/mimic-code) for Postgres, MySQL, and Oracle:  
https://github.com/MIT-LCP/mimic-code/tree/master/buildmimic

If you are familiar with Make, then you can directly clone the above repository and run `make` in order to build MIMIC on a PostgreSQL instance. Otherwise, see the tutorials below.

## Tutorial  

Tutorials for installing MIMIC in a local Postgres database are provided for Mac OSX, Unix, and MS Windows systems. For more detail, select the 'Tutorial' item in the left menu.

