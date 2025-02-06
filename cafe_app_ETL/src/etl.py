"""
Python Extract Transform Load Example
"""

# %%
import pandas as pd
import re
from sqlalchemy import create_engine
from datetime import datetime


columns = ['datetime', 'city', 'customer_name', 'items', 'total_price', 'payment_method', 'card_no']

def extract_csv(file_path):    
    # Read the CSV file data into a DataFrame
    df = pd.read_csv(file_path)
    df.columns = columns  
    
    # Convert the 'Items' column to string type
    df['items'] = df['items'].astype(str).fillna('')
    # Split the 'Items' column into separate rows
    items_split = df['items'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).reset_index(name='items')
    items_split['newitems'] = parse_items(items_split['items'])
    items_split[['item', 'variant', 'size', 'price']] = items_split['newitems'].apply(pd.Series)
    
    # Merge the split items back with the original data
    df = df.drop(columns=['items']).merge(items_split, left_index=True, right_on='index').drop(columns=['index'])
    
    # Drop the 'Items' column
    df = df.drop(columns=['items'])

    df['datetime'] = pd.to_datetime(df['datetime'], format='%d/%m/%Y %H:%M')
    # Reorder columns
    df = df[['datetime', 'city', 'customer_name', 'item', 'variant', 'size', 'price', 'total_price', 'payment_method','card_no']]
    
    # Save the DataFrame to a new CSV file
    df.to_csv('parsed_data.csv', index=False)
    return df

def transform(df:pd.DataFrame):   
    df = df.drop(columns=['card_no'])
    return df       

def parse_items(items):
    parsed_items = []
    regex_with_variant = r"^(?P<size>\w+)\s+(?P<item_name>[a-zA-Z\s]+)\s+-\s+(?P<variant>[a-zA-Z\s]+)\s+-\s+(?P<price>[0-9.]+)$"
    regex_without_variant = r"^(?P<size>\w+)\s+(?P<item_name>[a-zA-Z\s]+)\s+-\s+(?P<price>[0-9.]+)$"
    for i in items:
        items = i.split(",")
        for i in items:
            item = i.strip()
            print(item)
            match = re.match(regex_with_variant, item)
            if match:
                parsed_items.append({
                    "item_name": match.group("item_name").strip(),
                    "variant": match.group("variant").strip(),
                    "size": match.group("size").strip(),
                    "price": float(match.group("price").strip())
                })
                continue
            match = re.match(regex_without_variant, item)
            if match:
                parsed_items.append({
                    "item_name": match.group("item_name").strip(),
                    "variant": "None",  # No variant available
                    "size": match.group("size").strip(),
                    "price": float(match.group("price").strip())
                })
                continue
            else:
                # Log unmatched items
                print(f"Item format not matched: {item}")
    return parsed_items    


# %%

