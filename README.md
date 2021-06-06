# mini_pipeline
A Python program to create a PostgreSQL database and populate it with .csv values. 

A number of SQL queries are then performed with results saved to a .txt file.

## Prerequsites
Users will first need to have a recent version of Python installed as well as PostgreSQL.

Additionally, users will need to install SQLAlchemy and psycopg2:

```pip install -r requirements.txt```

After installing the requirements, users must input their personal settings in the config file:

```config.yaml```

## Usage
To run the program from within your terminal, navigate to the directory in which the file is saved and enter:

```python3 mini_pipeline.py```

## Results
The results from the SQL queries are saved to a file created in the same directory that the script is run from.

The file is:
```stdout_results.txt```

Contents of ```stdout_results.txt``` will be:

The greatest number of tickets sold for a particular event was 1024 \
The ticket prices in descending order are: 89.95, 89.95, 59.34, 43.0, 35.0, 35.0 \
Events were held in these distinct locations: Michigan, Carlisle, New York, Washington DC \
The highest spending customer, Customer 3, spent $124.95 in total. 
