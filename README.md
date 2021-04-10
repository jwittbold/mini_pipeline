# mini_pipeline
Python program to create a PostgreSQL database and populate it with .csv values. 

A number of SQL queries are then performed.

## Usage
This Python script will create a PostgreSQL database and populate it with data found within the included .csv file.

## Prerequsites
Users will first need to have a recent version of Python installed as well as PostgreSQL database.

Additionally, users will need to install SQLAlchemy and psycopg2

```pip install -r requirements.txt```

After installing the requirements, users must input their personal settings in the config file:

```config.yaml```

## Results
The results from the SQL queries are saved to a file created in the same directory that the script is run from.

The file is:
```stdout_results.txt```
