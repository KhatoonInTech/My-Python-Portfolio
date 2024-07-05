#inventoryclass
from .import Mod_Filing as mf 
from .import Mod_Food_Items as mfi
from datetime import date
from tabulate import tabulate



class Inventory():
    """Manages the overall food store inventory."""
    def __init__(self,database):
     """Listing items in inventory."""
     self.items=[]
     self.file=mf.filing.csvfiling(database)
     self.header = self.file.inv_headers
     self.content = self.file.reading_file()

#_____________________________________________________________________________________________________________     
    # adding items 
    def adding(self):
       '''Taking input from user and appending it into the list items'''
    #name
       while True:
          self.name=input("Enter the Name of the item here :   ")
          if all(i.isalpha() or i.isspace() for i in self.name):
            break
          else:
            print("The name of Food Item can only include alphabets..")
    #category       
       while True:     
          self.category=input("Enter the Category of the item here :   ")
          if all(i.isalpha() or i.isspace() for i in self.category):
            break
          else:
            print("The category of Food Item can only include alphabets..")
    #quantity        
       while True:     
          self.quantity=int(input("Enter the Quantity of the item here :   "))
          if all(i.isdigit() for i in str(self.quantity)):
            break
          else:
            print("The quantity of Food Item can only include digits..")
    #price
       while True:     
          self.price=float(input("Enter the Price in Rs. of the item here :   "))
          if str(self.price).count('.')==1 and all(i in '.0123456789' for i in str(self.price) ):
            break
          else:
            print("The price of Food Item can only be a floating number..")
    # barcode        
       '''barcode can be of any length and include any character'''
       self.barcode=input("Enter the Barcode of the item here :   ")  
          
    #expiry date          
       while True: 
          exp= input("Enter the Expiry Date of the item here  (YYYY-MM-DD):   ")
          if exp.count("-")==2 and len(exp)==10:
            self.expirydate=date.isoformat(date.fromisoformat(exp))
            break
          else:
            print("Kindly use this format YYYY-MM-DD..(e.g., 2024-11-13)")
       #creating instance of FoodItems class
       instance=mfi.food_items.FoodItems(self.name,self.category,self.quantity,self.price,self.barcode,str(self.expirydate))
       #appending the info in the list items
       self.items.append({'Name':self.name , 'Category':self.category ,'Quantity':self.quantity ,'Price':self.price,'Barcode':self.barcode ,'Expiry_Date': self.expirydate})
       
       #show success message
       print(f"SUCCESS: Food Item added successfully to the record with following details\n{instance}")
       #returning the list self.items
       return self.items 
    
#_________________________________________________________________________________________________________________________________________________________________________________________________________    
       ## editing items
    def editing(self):
        '''Takimg input of Barcode from user to make changes in item list because every item has a unique barcode'''
        bar=input("Enter the barcode of the product that you want to edit: ")
        for item in self.content:
           if item.get("Barcode")==bar:
              while True:
                option=int(input('''
>>What do you want to edit in this item.
                                  
          Digit | Option 
        ------------------                                               
          1     | Name
          2     | Category
          3     | Quantity
          4     | Price                           
          5     | Expiry Date
>>Please choose the coresponding number of your required option
                 '''))
                match option:
                  case 1:
                    while True:
                      item['Name']=input("Enter new name here: ")
                      if all(i.isalpha() or i.isspace() for i in item['Name']):
                         break
                      else:
                         print("The name of Food Item can only include alphabets..")
                  case 2:
                    while True:
                      item['Category']=input("Enter the new category here: ")    
                      if all(i.isalpha() or i.isspace() for i in item['Category']):
                         break
                      else:
                         print("The category of Food Item can only include alphabets..")
                  case 3:
                    while True:
                      item['Quantity']=int(input("Enter the new quantity here: "))
                      if all(i.isdigit() for i in str(item['Quantity'])):
                         break
                      else:
                         print("The quantity of Food Item can only include digits..")
                  case 4:
                    while True:     
                      item['Price']=float(input("Enter the new Price in Rs. of the item here :   "))
                      if str(self.price).count('.')==1 and all(i in '.0123456789' for i in str(self.price) ):
                        break
                      else:
                         print("The price of Food Item can only be a floating number..")         
                  case 5:
                    while True:
                       exp=input("Enter the new expiry date here (YYYY-MM-DD): ")  
                       if exp.count("-")==2 and len(exp)==10:
                         item['Expiry_Date']=date.isoformat(date.fromisoformat(exp))
                         break
                       else:
                            print("Kindly use this format YYYY-MM-DD..(e.g., 2024-11-13)")
                  case _:
                    print("Select a valid option")

                #continuing editing
                op=input(f"""
                         
>>Do you want to continue editing in this item with Barcode:{bar}?
        Press Y to continue
        Press N to exit                                  
""")
                if op.upper()!='Y' or  op.upper()!='YES' or  op.upper()!='CONTINUE' :
                  break

        ##show success message
        print(f"SUCCESS:Item with Barcode{bar} edited successfully")  
        #returning the list self.content 
        return self.content

#__________________________________________________________________________________________________________________________________________________           
    #deletig items
    def deleting(self) :
       '''Taking barcode as input from user and deleting the corresponding item from list'''
       
       bar=input("Enter the barcode of the product that you want to delete from the record here:\n") 
       i=-1
       for item in self.content:
          i+=1
          if item.get('Barcode') ==bar: 
            del self.content[i]  
          #Show success message      
          print(f"SUCCESS:Item with Barcode:{bar} deleted successfully.")   
          #returning the list self.content 
          return self.content 
#________________________________________________________________________________________________________________________________________________________________________    
 #searching items on basis of name
    def search_name(self,name):
      
      '''searching item on the basis of parameter name defined in app.py'''
      results=[]  #for many products with similar names
      for item in self.content:
        
        if item.get("Name").lower()==name.lower():
          '''creating instance of FoodItems class'''
          ins=mfi.food_items.FoodItems(item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date')))
          #appending the findings in result[]
          results.append(ins)
      if len(results)==0:
        return None
      else:
        return results  
#_________________________________________________________________________________________________________________________________________________________________________
 #searching items on basis of category
    def search_category(self,category):
      '''searching ite on the basis of parameter category defined in app.py'''
      results=[]  #for many products with similar names
      for item in self.content:
        if item.get("Category").lower()==category.lower():
          '''creating instance of FoodItems class'''
          ins=mfi.food_items.FoodItems(item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date')))
          #appending the findings in result[]
          results.append(ins)
      if len(results)==0:
        return None
      else:
        return results
#____________________________________________________________________________________________________________________________________________________________________________
 #searching items on basis of quantity
    def search_quantity(self,quantity):
      '''searching ite on the basis of parameter quantity defined in app.py'''
      results=[]  #for many products with similar names
      for item in self.content:
        if item.get("Quantity")==quantity:
          '''creating instance of FoodItems class'''
          ins=mfi.food_items.FoodItems(item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date')))
          #appending the findings in result[]
          results.append(ins)
      if len(results)==0:
        return None
      else:
        return results           
#____________________________________________________________________________________________________________________________________________________________________________    
#searching items on basis of price
    def search_price(self,price):
      '''searching ite on the basis of parameter price defined in app.py'''
      results=[]  #for many products with similar names
      for item in self.content:
        if item.get("Price")==price:
          '''creating instance of FoodItems class'''
          ins=mfi.food_items.FoodItems(item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date')))
          #appending the findings in result[]
          results.append(ins)
      if len(results)==0:
        return None
      else:
        return results
#____________________________________________________________________________________________________________________________________________________________________________          
#searching items on basis of barcode
    def search_barcode(self,barcode):
      '''searching ite on the basis of parameter barcpde defined in app.py
         since barcode is unique ,thus no need to create list
      '''
      
      for item in (self.content):
        if item.get("Barcode")==barcode:
          '''creating instance of FoodItems class'''
          ins=mfi.food_items.FoodItems(item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date')))
          return ins 
        else: 
          return None 
#____________________________________________________________________________________________________________________________________________________________________________            
    #searching items on basis of expiry date
    def search_expdate(self,expdate):
      
      '''searching ite on the basis of parameter expdate defined in app.py'''
      results=[]  #for many products with similar names
      for item in self.content:
        if item.get("Expiry_Date")==expdate:
          '''creating instance of FoodItems class'''
          ins=mfi.food_items.FoodItems(item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date')))
          #appending the findings in result[]
          results.append(ins)
      if len(results)==0:
        return None
      else:
        return results
#____________________________________________________________________________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________________________________________________________________________               
#display csv sheets
    def  disp_csv(self):
      """
    Displays the inventory data in a tabular format using the 'tabulate' library.
    """
      conlist=[]  # Create an empty list to store the table data
      for item in self.content:
         # Extract information from each item dictionary and handle potential missing keys and append it into the conlist
        conlist.append([item.get('Name'),item.get('Category'),item.get('Quantity'),item.get('Price'),item.get('Barcode'),str(item.get('Expiry_Date'))])
      # Use tabulate to create and print the formatted table  
      print(tabulate(conlist, headers=self.header))  


