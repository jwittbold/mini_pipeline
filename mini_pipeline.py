
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine.url import URL
import pandas as pd
import sys
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

db_url = config['db_settings']

FILE_PATH = config['FILE_PATH']
col_names = ('ticket_id', 'trans_date', 'event_id', 'event_name', 'event_date', 'event_type', 'event_city', 'num_tickets', 'price', 'customer_id', 'event_addr')
df = pd.read_csv(FILE_PATH, sep=',', names=col_names, index_col=False)


def main():
    """Establishes database connection and excecutes functions (SQL queries) contained within"""
    try:
        engine = create_engine(URL(**db_url))

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(type(e))

    Session = sessionmaker(bind=engine)
    session = Session()

    def csv_to_table():
        """Creates table from 'df' variable using parameters specified within 'df' variable creation"""
        
        try:
            table_name = 'ticket_sales'
            df.to_sql(
                table_name,
                engine,
                if_exists='replace',
                index=False,
                chunksize=500
                )
            csv_to_table()

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(type(e))
            

    def max_attendance():
        """Returns number of attendees for the event with maximum attendance"""
        
        try:
            max_attendance = pd.read_sql("""
                SELECT MAX(num_tickets)
                FROM ticket_sales
                """,
            con=engine)
            
            result = int(max_attendance.iloc[0])
            print(f'The greatest number of tickets sold for a particular event was {result}')

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(type(e))

    max_attendance()

    def query_price():
        """Queries ticket prices and returns prices in descending order"""

        try:
            ticket_prices = pd.read_sql("""
                SELECT price 
                FROM ticket_sales
                ORDER BY price DESC;
                """,
            con=engine)

            # removes enclosing brackets of dataframe elements using list slicing and translation mapping 
            stripped = ticket_prices['price'] = ticket_prices['price'].apply(lambda x: str(x).strip('[]'))
            result = str(stripped.values.tolist())[1:-1]
            translation = {39:None}
            print(f'The ticket prices in descending order are:', result.translate(translation))

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(type(e))

    query_price()


    def query_city():
        """Queries for cities in which events were held, only returns distinct values for those cities"""

        try:    
            locations = pd.read_sql("""
                SELECT DISTINCT(event_city)
                FROM ticket_sales;
            """,
            con=engine)
            
            # removes enclosing brackets of dataframe elements using list slicing and translation mapping 
            stripped = locations['event_city'] = locations['event_city'].apply(lambda x: str(x).strip('[]'))
            result = str(stripped.values.tolist())[1:-1]
            translation = {39:None}
            print(f'Events were held in these distinct locations:', result.translate(translation))

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(type(e))  

    query_city()


    def top_customer():
        """Sums ticket prices based on customer_id, returns id of highest spending customer and total amount spent"""

        try:    
            top_customer = pd.read_sql("""
                SELECT SUM(price), customer_id
                FROM ticket_sales
                GROUP BY customer_id
                ORDER BY SUM(price) DESC
                LIMIT 1;
            """,
            con=engine)
            print(f'The highest spending customer, Customer {int(top_customer.iloc[0][1])}, spent ${top_customer.iloc[0][0]} in total.')

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(type(e))        

    top_customer()

    session.commit()
    session.close()

if __name__ == '__main__':   

    # writes the results from stdout to a text file contained within the same directory
    original_stdout = sys.stdout
    with open('stdout_results.txt', 'w') as f:
        sys.stdout = f 
        main()
        sys.stdout = original_stdout
