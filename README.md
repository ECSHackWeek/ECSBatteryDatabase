[![Build Status](https://travis-ci.org/ECSHackWeek/ECSBatteryDatabase.svg?branch=master)](https://travis-ci.org/ECSHackWeek/ECSBatteryDatabase)
[![Coverage Status](https://coveralls.io/repos/github/ECSHackWeek/ECSBatteryDatabase/badge.svg?branch=master)](https://coveralls.io/github/ECSHackWeek/ECSBatteryDatabase?branch=master)

# ECSBatteryDatabase

## ECSBatDBM
Electrochemical Society Battery Database Model (ecsbatdbm) is a relational
data model, reference implementation of the model and associated API and
data management toolchain for battery related experimental data.  The
prototype implementation was first developed at ECS Data Science Sprint at
the ECS 236th Meeting in Atlanta.

## frontend
The frontend aims to provide a web interface to the database. It consists of a
minimal flask server and a React interface. Initial prototypes will focus on
adding metadata options (electrolytes/electrodes/separators) and uploading data.
Additional features for viewing data, searching by metadata, etc. will follow.
Instructions on how to install and run the frontend can be found in
frontend/README.md.

## metadata
The metadata repo includes: 
cell_metadata.xslx - A downloadable, easy-to-use method to allow users to upload batches of experimental metadata at one time. The column headings reflect the current metadata parameters considered in the database schema. 
xlsx_template.ipynb - The Jupyter notebook that builds the .xslx file.
