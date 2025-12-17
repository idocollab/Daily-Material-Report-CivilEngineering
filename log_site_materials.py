#Import modules 
from helper import get_input,log_setup,clean
log_setup()
import logging
from datetime import datetime
from csv import writer
import os
from colorama import Fore,Style



class MaterialUsage:
    #Initialize parameters needed 
    def __init__(self,work_type,location,cement_bags,sand_m3,aggregate_m3,file,cement_cost=450,sand_cost=1800,aggregate_cost=1600):
        current=datetime.now()
        year=current.year
        month=current.month
        day=current.day
        self.date=f"{year}:{month}:{day}"
        self.cement_bags=int(cement_bags)
        self.sand_m3=round(float(sand_m3),4)
        self.aggregate_m3=round(float(aggregate_m3),4)  
        self.work_type=work_type
        self.location=location 
        self.cement_cost=cement_cost
        self.sand_cost=sand_cost
        self.aggregate_cost=aggregate_cost
        self.file=file
        logging.info("Parameters Initialized...")

    def save_data(self): #save data to daily.csv or custom.csv file 
        def  total_cost():
         total_cement_cost=round(self.cement_bags*self.cement_cost,4)
         total_sand_cost=round(self.sand_m3*self.sand_cost,4)
         total_aggregate_cost=round(self.aggregate_m3*self.aggregate_cost,4)
         total=round(total_cement_cost+total_sand_cost+total_aggregate_cost,4)
         return [total_cement_cost,total_sand_cost,total_aggregate_cost,total]
        data=[self.date,self.work_type,self.location,self.cement_bags,self.sand_m3,self.aggregate_m3]+total_cost()
        if os.path.exists(self.file):     #append if file exists
            with open(self.file,'a',newline="") as f:
                w=writer(f)
                w.writerow(data)
                logging.info("New datas get apended...")
        elif not os.path.exists(self.file):   #write if file dont exists
            with open(self.file,"w",newline="") as f:
                w=writer(f)
                header=["Date","WorkType","Location","CementBags","Sand-m3","Aggregate-m3","CementCost","SandCost","AggregateCost","TotalCost"]
                w.writerow(header)
                w.writerow(data)
                logging.info("New datas added to new file")
                   
      
class Menu: #CLI menu 

    def front(self):    # First and front menu on display
        print(Fore.WHITE+Style.BRIGHT+"_"*45)
        print(Fore.WHITE+Style.BRIGHT+" ")
        print(Fore.WHITE+Style.BRIGHT+"Daily Material".center(42))  
        print(Fore.WHITE+Style.BRIGHT+" ")
        print(Fore.CYAN+Style.BRIGHT+"Developer : Er.Shivam Yadav")
        print(Fore.WHITE+Style.BRIGHT+"_"*45)
        logging.info("Front Menu Appeared...")
    def save_data_menu(self):  #menu after saving data and ending menu
        clean()
        print(Fore.WHITE+Style.BRIGHT+"_"*45)
        print(Fore.CYAN+Style.BRIGHT+"Data saved...")
        print(Fore.WHITE+Style.BRIGHT+"_"*45)
        print("Today's data added succcessful...")
        print(Fore.WHITE+Style.BRIGHT+"_"*45)
        finish=get_input("Enter to End This App...")
        os.system("exit")
        logging.info("Save Data Menu Appeared...")

    def take_data(self):     #take data from menu
        work_type=get_input("Work Type : ",data_type=str,error="Wrong WorkType...")
        location=get_input("Location : ",error="Wrong Location...")
        cement_bags=get_input("Number Of CementBags Used : ",data_type=int,error="If its 20.5, make it 21...")
        sand_m3=get_input("Volume Of Sand Used[m3] : ",data_type=float,error="Wrong Volume Of Sand...")
        aggregate_m3=get_input("Volume Of Aggregate Used[m3] : ",data_type=float,error="Wrong Volume Of Aggregate...")
        while True:
         file=get_input("CSV Filename or Filepath : ",data_type=str,error="Wrong FileName...")
         if file.strip().lower().endswith(".csv") : 
            break 
        logging.info("Data Taken From User...")    
        return [work_type,location,cement_bags,sand_m3,aggregate_m3,file]    
      

    

def main():          #main function to control everything
    clean()
    menu_obj=Menu()
    menu_obj.front()
    data=menu_obj.take_data()
    material_obj=MaterialUsage(data[0],data[1],data[2],data[3],data[4],data[5])
    material_obj.save_data()
    menu_obj.save_data_menu()
    logging.info("Program Ended...")

if __name__=="__main__": # doesnot work if you import this file to another ,Extra Safety
    main()                    

