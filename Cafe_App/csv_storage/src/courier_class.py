import csv
import pandas as pd
prod_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\products.csv"
couriers_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\couriers.csv"
orders_file_path = "D:\\practice_projects\\Cafe_App\\csv_storage\\data\\orders.csv"

new_couriers = []
updated_couriers = []

class courier:
    def load_data_couriers(couriers_file_path):
    #read from the file
        try:
            data = pd.read_csv(couriers_file_path)
        except FileNotFoundError as fnf_error:
            print(fnf_error) 
            return fnf_error
        else:   
            df = pd.DataFrame(data)
            print(df)

    def save_data_couriers(new_couriers,option,itemindex):
        option=option
        if(option==0):
            courier.load_data_couriers(couriers_file_path)
        if(option==1):#create data
            for data in new_couriers:
                if data['courier_name'] == '' or data['ph_no'] == '':
                    print("Data is empty, Data is not saved") 
                else:
                    filedata = pd.read_csv(couriers_file_path)    
                    if(filedata.empty): #if file is not empty each time it adds new line with 'a' mode
                        df = pd.DataFrame(new_couriers)   
                        df.to_csv(couriers_file_path,index=False)
                    else:
                        df = pd.DataFrame(new_couriers)   
                        df.to_csv(couriers_file_path,mode='a',index=False,header=False)
                print("Courier is added successfully")   
                courier.load_data_couriers(couriers_file_path) 

        if(option==2):#update data
            data = pd.read_csv(couriers_file_path)
            df = pd.DataFrame(data)
            df.loc[itemindex] = new_couriers
            df.to_csv(couriers_file_path,index=False)
            print("Courier is Updated successfully")   
            courier.load_data_couriers(couriers_file_path) 
  
    def load_data_dict_couriers(new_couriers,option,itemindex):
        if(option==1):
            courier.save_data_couriers(new_couriers,option,itemindex)
        if(option==2):
            courier.save_data_couriers(new_couriers,option,itemindex)

    def create_data_couriers():
        option = 1
        new_courier = input('Enter Courier name :')
        new_courier_ph_no = input('Enter Courier Phone number :')
        new_data = {"courier_name":new_courier, "ph_no" :('{} {} {}'.format('+44',new_courier_ph_no[1:5],new_courier_ph_no[5:]))}
        #APPEND product dictionary to products list
        new_couriers.append(new_data)
        courier.load_data_dict_couriers(new_couriers,option,0)

    def update_data_couriers():
        option=2
        courier.load_data_couriers(couriers_file_path)
        itemindex=int(input("Enter Courier Index Value to update : ")) 
        if(itemindex<-1):
            print('Incorrect index value')
            exit() 
        updatedcourier=input("Enter New Courier Name : ")
        new_ph_no=input("Enter New Phone number : ")  
        updated_data = {"courier_name":updatedcourier, "ph_no" :('{} {} {}'.format('+44',new_ph_no[1:5],new_ph_no[5:]))}
        courier.load_data_dict_couriers(updated_data,option,itemindex)      

    def delete_data_couriers():
        courier.load_data_couriers(couriers_file_path)
        itemindex=int(input("Enter Courier Index Value to Delete : ")) 
        data = pd.read_csv(couriers_file_path)
        df = pd.DataFrame(data) 
        if(itemindex<-1):
            print('Incorrect index value')
            exit()
        try:  
            df.drop(itemindex,axis=0,inplace=True)
            df.to_csv(couriers_file_path,index=False)
            print("\n Couriers Deleted Successfully\n")
            courier.load_data_couriers(couriers_file_path)
        except Exception as e:
            print(f"An error occurred: {e}") 