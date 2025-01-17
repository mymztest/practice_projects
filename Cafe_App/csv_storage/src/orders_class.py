
import pandas as pd
from prod_class import product
from courier_class import courier

prod_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\products.csv"
couriers_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\couriers.csv"
orders_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\orders.csv"

new_couriers = []
new_orders = []
order_status = {}

###################################################################################

class orders:

    def load_data_orders(orders_file_path):
    #read from the file
        try:
            data = pd.read_csv(orders_file_path)
        except FileNotFoundError as fnf_error:
            print(fnf_error) 
            return fnf_error
        else:   
            df = pd.DataFrame(data)
            print(df)

    def save_data_orders(new_orders,option,itemindex):
        option=option
        if(option==1):
            orders.load_data_orders(orders_file_path)
        if(option==2):#create data
            #print(new_orders)
            for data in new_orders:
             if(data['customer_name'] == '' or data['customer_address'] == '' or data['customer_phone'] == '' or data['courierindex'] == '' or data['status'] == '' or data['items']== ''):
                print("Data is empty, Data is not saved") 
             else:
                filedata = pd.read_csv(orders_file_path)    
                if(filedata.empty): #if file is not empty each time it adds new line with 'a' mode
                    df = pd.DataFrame(new_orders)   
                    df.to_csv(orders_file_path,index=False)
                else:
                    df = pd.DataFrame(new_orders)   
                    df.to_csv(orders_file_path,mode='a',index=False,header=False)
                print("Order is added successfully")   
                orders.load_data_orders(orders_file_path)

        if(option==3):#update order status
            data = pd.read_csv(orders_file_path)
            df = pd.DataFrame(data)
            df.loc[itemindex,'status'] = new_orders['status']  
            df.to_csv(orders_file_path,index=False)
            print("Order Status is Updated successfully")   
            orders.load_data_orders(orders_file_path)

        if(option==4):#update order
            data = pd.read_csv(orders_file_path)
            df = pd.DataFrame(data)
            df.loc[itemindex] = new_orders
            df.to_csv(orders_file_path,index=False)
            print("Order is Updated successfully")   
            orders.load_data_orders(orders_file_path) 

    def load_data_dict_orders(new_orders,option,itemindex):
        if(option==1):
            orders.save_data_orders(new_orders,option,itemindex)
        if(option==2):
            orders.save_data_orders(new_orders,option,itemindex)
        if(option==3):
            orders.save_data_orders(new_orders,option,itemindex)
        if(option==4):
            orders.save_data_orders(new_orders,option,itemindex)  

    def create_data_orders():
        option = 2
        cust_name = input('Enter Customer name :')
        cust_address = input('Enter Customer address :')
        cust_ph_no = input('Enter Customer Phone number :')
        #PRINT products list with index value
        print('Product Available to order Are \n ')
        product.load_data_prod(prod_file_path)
        #GET user inputs for comma-separated list of product index values
        #CONVERT above user input to a string e.g. "2,1,3"
        prod_index_values = input("Enter comma-separated index of products : example 2,1,3 : \n")
        #PRINT couriers list with index value for each courier
        courier.load_data_couriers(couriers_file_path)
        cust_courier_index = int(input("Enter Couriers index : "))
        order_status = "Preparing"
        new_data = {"customer_name":str(cust_name), "customer_address": str(cust_address), "customer_phone" :('{} {} {}'.format('+44',cust_ph_no[1:5],cust_ph_no[5:])), "courierindex":cust_courier_index, "status":str(order_status), "items": prod_index_values}
        #APPEND order dictionary to orders list
        new_orders.append(new_data)
        orders.load_data_dict_orders(new_orders,option,0)

    def update_existing_orders_status():
        option=3
        orders.load_data_orders(orders_file_path)
        orderindex=int(input("Enter Order Index to update Status: ")) 
        if(orderindex<-1):
            print('Incorrect index value')
            exit() 
        updatedstatus=input("Enter Order status to update : ")
        updated_data = {"status":updatedstatus}
        orders.load_data_dict_orders(updated_data,option,orderindex)

    def update_data_orders():
        option=4
        orders.load_data_orders(orders_file_path)
        itemindex=int(input("Enter Order Index Value to update : ")) 
        if(itemindex<-1):
            print('Incorrect index value')
            exit() 
        newcust_name = input('Enter Customer name :')
        newcust_address = input('Enter Customer address :')
        newcust_ph_no = input('Enter Customer Phone number :')
        newcust_courier_index = int(input("Enter Couriers index : "))
        newprod_index_values = input("Enter comma-separated index of products : example 2,1,3 : ")
        order_status = "Preparing"
        updated_data = {"customer_name":str(newcust_name), "customer_address": str(newcust_address), "customer_phone" :('{} {} {}'.format('+44',newcust_ph_no[1:5],newcust_ph_no[5:])), "courierindex": newcust_courier_index, "status":str(order_status), "items": newprod_index_values}
        orders.load_data_dict_orders(updated_data,option,itemindex) 

    def delete_data_orders():
        orders.load_data_orders(orders_file_path)
        itemindex=int(input("Enter Courier Index Value to Delete : ")) 
        data = pd.read_csv(orders_file_path)
        df = pd.DataFrame(data) 
        if(itemindex<-1):
            print('Incorrect index value')
            exit()
        try:  
            df.drop(itemindex,axis=0,inplace=True)
            df.to_csv(orders_file_path,index=False)
            print("\n Order Deleted Successfully\n")
            orders.load_data_orders(orders_file_path)
        except Exception as e:
            print(f"An error occurred: {e}") 