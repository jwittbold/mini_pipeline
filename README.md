# mini_pipeline
Python program to create database and populate with .csv values. 

A number of SQL queries are then performed.

## Usage
This Python script will create a PostgreSQL database and populate it with data found within the included .csv file.

## Prerequsites
Users will first need to have a recent version of Python installed as well as PostgreSQL database.

Additionally, users will need to install SQLAlchemy and psycopg2

```pip install -r requirements.txt```

## Results
The results from the SQL queries are saved to a file created in the same directory that the script is run from.

The file is:
```stdout_results.txt```
