
import csv
import os

class csvfiling():
    '''A class for handling CSV files as database'''
    def __init__(self,database):
        '''initializing the class'''
        self.database=database
        self.inv_headers=['Name','Category','Quantity','Price','Barcode','Expiry_Date']
#____________________________________________________________________________________________________________       
    ##creating a CSV file
    def create(self):
      try:
        if not os.path.exists(self.database):      #if a csv file with name given by user in Week4.app.greet() does not exist in machine then create a new file    
          with open(self.database,"w",newline="") as inv:
             writer=csv.DictWriter(inv,fieldnames=self.inv_headers)
             writer.writeheader()
             return 0
             # No need to call csvfile.close() explicitly as the `with` statement handles it

        elif os.path.exists(self.database):      #if a csv file with name given by user in Week4.app.greet() exists in machine then create a new file    
            with open(self.database,"a",newline="") as inv:
              writer=csv.DictWriter(inv,fieldnames=self.inv_headers)
              return 1
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

#______________________________________________________________________________________________________________
    #updating csv file after adding,deleting,editing the items
    def update(self,inv_content: list):
      try:
        with open(self.database,"w",newline="") as inv:
          writer=csv.DictWriter(inv,fieldnames=self.inv_headers)
          for row in inv_content:
            writer.writerow(row)
             
      except FileNotFoundError:
        print("Error: File 'inventory.csv' not found. Creating a new file.")
        # Optionally create a new file here

      except PermissionError:
        print("Error: Insufficient permissions to write to 'inventory.csv'.")
        # Handle permission issues (e.g., change permissions or choose a writable location)

      except OSError as e:
        print(f"An unexpected error occurred: {e}")
        # Handle general OS errors
#_________________________________________________________________________________________________________________
#reading csv file after adding,deleting,editing the items
    def reading_file(self):
      try:
        with open(self.database,"r",newline="") as inv:
             reader=csv.DictReader(inv)
             data=list(reader)
        return data 
             
      except FileNotFoundError:
        print("Error: File 'inventory.csv' not found. Creating a new file.")
        # Optionally create a new file here

      except PermissionError:
        print("Error: Insufficient permissions to write to 'inventory.csv'.")
        # Handle permission issues (e.g., change permissions or choose a writable location)

      except OSError as e:
        print(f"An unexpected error occurred: {e}")
        # Handle general OS errors        
#____________________________________________________________________________________________________________________
# ex=csvfiling("MCB bank.csv")
# ex.create()
# ex.adding_to_file([{'Name':'Dalda' , 'Category':"Cooking Essentials" ,'Quantity':6 ,'Price':123.90,'Barcode':"09876543212" ,'Expiry_Date': "2024-11-13"}])
# a=ex.reading_file()
# print(a)