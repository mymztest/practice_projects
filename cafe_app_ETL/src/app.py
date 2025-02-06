# %%
import pandas as pd
import logging
from logging.handlers import TimedRotatingFileHandler
from sqlalchemy import create_engine
from datetime import datetime
import etl
from utils import sql_utils

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"), # Log to a file
                        logging.StreamHandler()         # Log to console
                    ])

# Create a logger object
logger = logging.getLogger()
handler = TimedRotatingFileHandler('app.log', when='midnight', interval=1, backupCount=7)
columns = ['datetime', 'city', 'customer_name', 'items', 'total_price', 'payment_method', 'card_no']

def main():
    """
    The main function orchestrates the ETL process.
    """
    file_path = "D:\\DE_Projects_github\\practice_projects\\cafe_app_final\\data\\edinburgh.csv"
    logger.info("Starting ETL process...")
    try:
        raw_data = etl.extract_csv(file_path)
        transformed_data = etl.transform(raw_data)
        conn,cursor = sql_utils.connect_to_db()
        conn,cursor = sql_utils.create_tables(conn, cursor)
        sql_utils.load_data_into_db(transformed_data,conn,cursor)
        logger.info("ETL process completed successfully.")
    except Exception as e:
        logger.error(f"ETL process failed: {e}")

if __name__ == '__main__':
    main()