# Udacity Data Engineering Nanodegree - Capstone Project

### About the project
The goal of the project is to build data pipeline to be able to analyse immigration/travel trends in the U.S.
Full details and implementation are in **Capstone Project Template.ipynb**


### Project files
`config.cfg` stores configuration parameters for AWS.
`Capstone Project Template.ipynb` is the main project file, where all data cleaning and modelling is done.
`create_tables.py` creates tables in Redshift.
`create_tables_queries.py` contains sql queries for creating tables in Redshift.
`README.md` provides description of the project.
`US-Immigration-ER-Diagram.png` contains data model diagram.
All other files are data files.

### How to run the project
1. Create three S3 buckets: for ingesting raw data, for cleaned data, for application data (data that will be loaded into Redshift)
2. Create Redshift cluster and put the parameters in `config.cfg` file in \[CLUSTER\] section.
3. Edit `config.cfg` and fill in the required parameters.
4. Run `create_tables.py` script to create tables in Redshift.
5. Run `Capstone Project Template.ipynb` notebook.
