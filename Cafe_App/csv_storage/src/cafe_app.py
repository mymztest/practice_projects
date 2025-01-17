
import pandas as pd
from prod_class import product
from courier_class import courier
from orders_class import orders

prod_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\products.csv"
couriers_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\couriers.csv"
orders_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\orders.csv"


def main_menu_options():
    main_menu_options = '''
    ------------------------------------------------------
    You are in Main Menu options Please select following :
    
    Press 1. To PRINT products menu options
    Press 2. To PRINT couriers menu options
    Press 3. To PRINT orders menu options
    Press 0. To Save data to CSV and exit
    ------------------------------------------------------
    '''
    choice = int(input(main_menu_options))   
    return choice

def products_menu_options():
    prod_mnu_option = ''' 
    Products Menu Options:
    ------------------------------------------------------
      1. To PRINT products list
      2. To CREATE new product
      3. To UPDATE existing product
      4. To DELETE product
      
      0. To RETURN to main menu
    ------------------------------------------------------

      '''
    prod_menu_choice = int(input(prod_mnu_option))   
    return prod_menu_choice

def couriers_menu_options():
    courier_mnu_option = ''' 
    Couriers Menu options:
    ------------------------------------------------------   
      1. Get list of all the couriers. 
      2. Add new courier in the list. 
      3. Update an courier item in the list. 
      4. Delete a courier from the list. 
      0. Return to main menu. 
    ------------------------------------------------------  
      '''
    courier_menu_choice = int(input(courier_mnu_option))   
    return courier_menu_choice

def orders_menu_options():
      orders_mnu_option = ''' 
      Orders Menu options:
    ------------------------------------------------------              
        1. Get list of all the Orders.
        2. Add new Order in the list.
        3. Update an Order status.
        4. Update an Order item in the list.
        5. Delete a Order from the list.
        0. Return to main menu.
    ------------------------------------------------------        
      '''   
      orders_menu_choice = int(input(orders_mnu_option))   
      return orders_menu_choice

choice = main_menu_options()
if(choice==0):
  print("You have Exited the App")
elif(choice==1): 
  prod_menu_choice = products_menu_options()
  if(prod_menu_choice==0):
    main_menu_options()
  elif(prod_menu_choice==1):
    product.load_data_prod(prod_file_path)         
  elif(prod_menu_choice==2):
    product.create_data_prod()
  elif(prod_menu_choice==3):
    product.update_data_prod()
  elif(prod_menu_choice==4):
    product.delete_data_prod()  
  elif():
    print("This Menu Option is not available") 
elif(choice==2):
    couriers_menu_choice = couriers_menu_options()
    if(couriers_menu_choice==0):
        main_menu_options()
    elif(couriers_menu_choice==1):
        courier.load_data_couriers(couriers_file_path) 
    elif(couriers_menu_choice==2):
        courier.create_data_couriers()
    elif(couriers_menu_choice==3):
        courier.update_data_couriers()
    elif(couriers_menu_choice==4):
        courier.delete_data_couriers()  
    elif():
        print("This Menu Option is not available")    
elif(choice==3):  
    orders_menu_choice = orders_menu_options() 
    if(orders_menu_choice==0):
          main_menu_options() 
    elif(orders_menu_choice==1):
          orders.load_data_orders(orders_file_path)         
    elif(orders_menu_choice==2):
          orders.create_data_orders() 
    elif(orders_menu_choice==3):
          orders.update_existing_orders_status() 
    elif(orders_menu_choice==4):
          orders.update_data_orders()
    elif(orders_menu_choice==5):
          orders.delete_data_orders()  
    elif():
        print("This Menu Option is not available")      
else:
      print("This Menu Option is not available")   
