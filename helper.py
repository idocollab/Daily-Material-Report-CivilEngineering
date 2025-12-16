
def log_setup(): 
 """
 This function helps creating a look.log file in current directory and a basic template 
 of log structure.
 Note : You must have to import logging in main file.
 """    
 file=get_input("Enter Log Filename[Eg:look.log] : ",error="Invalid Filename...").strip().lower()
 import logging
 logging.basicConfig(filename=file if file.endswith(".log") else "look.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")


def get_input(command,data_type=str,error="Wrong Data...",num_check=False):
    """
      This function helps taking input with data type mentioned in parameters with handeling all error
       and allow reinput of data.
    """ 
    
    while True:
     try :
      data=data_type(input(command))
      if num_check==True and data_type!=str:
        if data>=0:
            return data
        else :
            print("Data must be postive number...")  
            continue  
      else:
        return data
     except ValueError:
        print("ValueError...")
     except Exception as e:
        print(e) 

def clean():
   import os
   if os.name == "nt":   # Windows
     os.system("cls")
   else:                 # macOS and Linux
     os.system("clear")
