import csv
import pandas as pd
prod_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\products.csv"
couriers_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\couriers.csv"
orders_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\orders.csv"

new_products = []
updated_products = []


class product:

    def load_data_prod(prod_file_path):
    #read from the file
        try:
            data = pd.read_csv(prod_file_path)
        except FileNotFoundError as fnf_error:
            print(fnf_error) 
            return fnf_error
            exit
        else:   
            df = pd.DataFrame(data)
            print(df)
            return df
            
    def create_data_prod():
            option = 1
            new_product = input('Enter product name :')
            new_prod_price = input('Enter product Price :')
            new_data = {"Name":new_product, "Price" :new_prod_price}
            #APPEND product dictionary to products list
            new_products.append(new_data)
            product.load_data_dict_prod(new_products,option,0)

    def update_data_prod():
            option=2
            product.load_data_prod(prod_file_path)
            itemindex=int(input("Enter Product Index Value to update : ")) 
            if(itemindex<0):
                print('Incorrect index value')
                exit() 
            try:    
                updatedproduct = input("Enter New Product Name : ")
                new_price = input("Enter New Price : ")  
                updated_data = {"Name":updatedproduct, "Price" :new_price}
                product.load_data_dict_prod(updated_data,option,itemindex)
            except Exception as e:
                print(f"An error occurred: {e}")        

    def delete_data_prod():
            df = product.load_data_prod(prod_file_path)
            itemindex=int(input("Enter Product Index Value to Delete : ")) 
            #data = pd.read_csv(prod_file_path)
            #df = pd.DataFrame(data) 
            if(itemindex<-1):
                print('Incorrect index value')
                exit() 
            try:    
                df.drop(itemindex,axis=0,inplace=True)
                df.to_csv(prod_file_path,index=False)
                print("\nProduct Deleted Successfully\n")
                product.load_data_prod(prod_file_path)   
            except Exception as e:
                print(f"An error occurred: {e}")   
                
    def save_data_prod(new_products,option,itemindex):
        option=option
        if(option==0):
            product.load_data_prod(prod_file_path)
        if(option==1):#create data
            for data in new_products:
                if data['Name'] == '' or data['Price'] == '':
                   print("Data is empty, Data is not saved") 
                else:
                  filedata = pd.read_csv(prod_file_path)    
                  if(filedata.empty): #if file is not empty each time it adds new line with 'a' mode
                    df = pd.DataFrame(new_products)   
                    df.to_csv(prod_file_path,index=False)
                  else:
                    df = pd.DataFrame(new_products)   
                    df.to_csv(prod_file_path,mode='a',index=False,header=False)
                print("Product is added successfully")   
                product.load_data_prod(prod_file_path) 

        if(option==2):#update data
            data = pd.read_csv(prod_file_path)
            df = pd.DataFrame(data)
            df.loc[itemindex] = new_products
            df.to_csv(prod_file_path,index=False)
            print("Product is Updated successfully")   
            product.load_data_prod(prod_file_path) 
        
    def load_data_dict_prod(new_products,option,itemindex):
            if(option==1):
                product.save_data_prod(new_products,option,itemindex)
            if(option==2):
                product.save_data_prod(new_products,option,itemindex)

           