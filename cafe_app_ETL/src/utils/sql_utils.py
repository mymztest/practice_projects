from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import logging

# Configure logging
LOGGER = logging.getLogger()

def connect_to_db():
    """ Connects to a PostgreSQL database"""
    # Replace with your PostgreSQL credentials
    conn_string = 'postgresql://username:password@localhost:port/dbname'
    try:
        LOGGER.info(
            "open_sql_database_connection_and_cursor: new connection starting..."
        )
        
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        LOGGER.info("open_sql_database_connection_and_cursor: connection ready")
        return conn, cursor
    except ConnectionError as ex:
        LOGGER.info(
            f"open_sql_database_connection_and_cursor: failed to open connection: {ex}"
        )
        raise ex

def create_tables(conn, cursor):
    try:
        sql = '''CREATE TABLE product_sales (datetime TIMESTAMP, city VARCHAR(255), customer_name VARCHAR(255), item VARCHAR(255), variant VARCHAR(255), size VARCHAR(255), price FLOAT, total_price FLOAT, payment_method VARCHAR(255));'''
        cursor = conn.cursor() 
        cursor.execute(sql) 
        LOGGER.info('create_db_tables: committing changes')
        conn.commit()
        LOGGER.info('create_db_tables: done')
        return conn,cursor
    except Exception as ex:
        LOGGER.error(f'create_db_tables: failed to create tables: {ex}')
        raise ex
    
def load_data_into_db(df:pd.DataFrame, conn, cursor):
    engine = create_engine('postgresql+psycopg2://', creator=lambda: conn)
    try:
        df.to_sql('product_sales', con=engine, if_exists='replace', index=False) 
        conn.commit()
        print(f"Sucssefully loaded data into Table")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()   