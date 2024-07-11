
import csv
import os

class csvfiling():
    '''A class for handling CSV files as database'''
    def __init__(self,database):
        '''initializing the class'''
        
        self.inv_headers=[database,'Peaker']
        # Define the base path
        self.base_path=os.getcwd()   # Get current working directory

        # Define the folder name you're looking for
        self.folder_name="history"

        #potential path
        self.potential_path=f"{self.base_path}/{self.folder_name}"

        self.database=f"{self.potential_path}/{database}.csv"
#________________________________________________________________________________________________       
    ##creating a CSV file
    def create(self):
      try:
        if not os.path.exists(self.database):      #if a csv file with name given by user in Week4.app.greet() does not exist in machine then create a new file    
          with open(self.database,"w",newline="") as inv:
             writer=csv.DictWriter(inv,fieldnames=self.inv_headers)
             writer.writeheader()
             
             # No need to call csvfile.close() explicitly as the `with` statement handles it

        elif os.path.exists(self.database):      #if a csv file with name given by user in Week4.app.greet() exists in machine then create a new file    
            with open(self.database,"a",newline="") as inv:
              writer=csv.DictWriter(inv,fieldnames=self.inv_headers)
              
      except FileNotFoundError:
        print("Error: File 'inventory.csv' not found. Creating a new file.")
        # Optionally create a new file here

      except PermissionError:
        print("Error: Insufficient permissions to write to 'inventory.csv'.")
        # Handle permission issues (e.g., change permissions or choose a writable location)

      except OSError as e:
        print(f"An unexpected error occurred: {e}")
        # Handle general OS errors

#_____________________________________________________________________________________________________________       
     #adding to CSV file  
    def adding_to_file(self,inv_items: list ):
      
      try:
        with open(self.database,"a",newline="") as inv:
            
            writer=csv.DictWriter(inv,fieldnames=self.inv_headers)
            
            for items in inv_items:
               writer.writerow(items)

      except FileNotFoundError:
        print("Error: File 'inventory.csv' not found. Creating a new file.")
        # Optionally create a new file here

      except PermissionError:
        print("Error: Insufficient permissions to write to 'inventory.csv'.")
        # Handle permission issues (e.g., change permissions or choose a writable location)

      except OSError as e:
        print(f"An unexpected error occurred: {e}")
        # Handle general OS errors

