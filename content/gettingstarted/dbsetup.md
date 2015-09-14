+++
date = "2015-09-01T14:02:13-04:00"
title = "Database set up"
linktitle = "Database set up"
weight = 2
toc = "true"

[menu]
  [menu.main]
    parent = "Getting started"

+++

# Using the data

MIMIC is provided in flat, comma delimited files with quotes surrounding text fields where appropriate. While this format is amenable to most software packages, you may find it most convenient to work with the data using structured query language (SQL). SQL is most frequently used with relative data as it allows for fast retrieval of information when appropriately configured. Of course, other programming languages, such as Python, are equally able to handle the data, albeit in a different format. When available, we have provided information here to help users import the data into a format which they can easily utilize. Documentation is currently available for MySQL, Postgres SQL and Oracle.

Note that while we aim to facilitate users in accessing and using the database, we unfortunately cannot support all the various software which could feasibly be used to analyze MIMIC. If users are successful in importing the database in a given software package, we welcome contribution of their code and methods used to accomplish this task, and we will update this page providing and provide the appropriate acknowledgements.

# Oracle

Scripts for importing the data into Postgres SQL are provided in the GitHub repository.

# Postgres SQL

Scripts for importing the data into Postgres SQL are provided in the GitHub repository.

# MySQL

Scripts for importing the data into Postgres SQL are provided in the GitHub repository.