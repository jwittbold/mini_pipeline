# mini_pipeline
Python program to create a PostgreSQL database and populate it with .csv values. 

A number of SQL queries are then performed with results saved to .txt file.

## Prerequsites
Users will first need to have a recent version of Python installed as well as PostgreSQL.

Additionally, users will need to install SQLAlchemy and psycopg2

```pip install -r requirements.txt```

After installing the requirements, users must input their personal settings in the config file:

```config.yaml```

## Usage
To run the program from within your terminal, navigate to where the directory in which the file is saved and and enter:

```python3 mini_pipeline.py```

## Results
The results from the SQL queries are saved to a file created in the same directory that the script is run from.

The file is:
```stdout_results.txt```
