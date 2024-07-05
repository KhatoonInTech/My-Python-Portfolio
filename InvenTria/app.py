#importing package IMS 
import IMS_package as pkg
from datetime import date
#_________________________________________________________________________________
#Greeting User
def greet():
    print("""
                     ------------------------------------------------
                          --------------------------------------
                      ||  Welcome to Inventory Management System  ||
                          ---------------------------------------
                     ------------------------------------------------  

""")
    user_name=input("Enter User Name here  :                   ")

    return user_name
#___________________________________________________________________________    
    
#options
def options():
    op=int(input("""
          ______________________________________________________________________________________
          |                                                                                    |
          | What would you like to do? Please select the corresponding digit...                |
          |                                                                                    |
          |                  Digits  |  Actions                                                |
          |                -------------------------------------------------                   |
          |                 1       | Add Food Items to the Record                             |
          |                 2       | Edit Food Items in the Record                            |
          |                 3       | Remove food Items from the Record                        |
          |                 4       | Display the Record                                       |
          |                 5       | Search for a Food Item in the Record                     |
          |                 --------------------------------------------------                 |
          |                 0       | EXIT                                                     |
          |                 --------------------------------------------------                 |
          |____________________________________________________________________________________|
"""))    
    return op

#_____________________________________________________________________________________________

#continue app
def con():
    con=input("""
  >>>Do you want to continue?
              Y= yes
              N= no
""")
    return con

#___________________________________________________________________________________________________

# main function
def main():
    user=greet()  #greeting user
    while True:
      database=input("Enter the name of DataBase(CSV file) here: ").strip() #using strip() to remove white spaces to remove error
      database+=".csv"     #Adding .csv with user provided name of database so as to create a csv file
      f=pkg.Mod_Filing.filing.csvfiling(database)  #creating instance of class csvfile in module filing.py
      exist=f.create()          #creating csv file
      inven=pkg.inventory.Inventory(database) ##creating instance of class Inventory in module inventory.py to avoid repetition
      if exist==0:
        print(f"""

  >>>CONGRATS {user}, your DataBase : {database} created successfully.

  ---------------------------------------------------------------------------------------------------------
  """)
        break
      elif exist==1:
        print(f"""

  >>>Dear {user}, A DataBase with this name {database} already exists in your machine.
  >>> If you want to make a new DataBase ,please, use a different name.

  ---------------------------------------------------------------------------------------------------------
  """)
        db=input("""
>Do you want to continue with existing DataBase?
                > Enter Y to continue with existing DataBase
                > Enter N to create a new DataBase
""")
        if db.lower()=='y' or db.lower()=='yes':
           print(f"""
------------------------------------------------------------------------------------
                  We are redirecting you to existing DataBase {database}.
------------------------------------------------------------------------------------                  
""") 
           break
        
#__________________________________________________________________________________________________________________________        
    while True:
        op=options()  #asking for action selection

        if op== 0:    #EXIT
            print("""
------------------------------------------------------------------------------------
                  We are logging you off .
------------------------------------------------------------------------------------                  
""")
            break
        else:
            match op:
#_________________________________________________________________________________________________________                
                case 1:        #adding food items
                    add_list=[]
                    while True:
                      l=inven.adding()
                      for dic in l:
                         add_list.append(dic)
                      cont=con()
                      if cont.lower()!='y' or cont.lower()!='yes':
                          break
                    f.adding_to_file(add_list) 
#_______________________________________________________________________________________________________
                case 2:        #editing food items
                    add_list=[]
                    l=inven.editing()
                    for i in l:
                      add_list.append(i)  #appending in add_list
                      
                    f.update(add_list) #updating csv file
#_______________________________________________________________________________________________________
                case 3:        #deleting food items
                    add_list=[]
                    l=inven.deleting()
                    for i in l:
                      add_list.append(i)  #appending in add_list
                      
                    f.update(add_list) #updating csv file
#_______________________________________________________________________________________________________
                case 4:        #displaying food items
                    inven.disp_csv() 
                    print("""
_______________________________________________________________________________________________________
""")
#_______________________________________________________________________________________________________
                case 5:        #searching food items in the record
                    filter=int(input("""
>>>What filter you want to use to search your desired item in the Record.
                                     
                Digits   | Filters
              -------------------------------------
                1        | Search by Name           
                2        | Search by Category             
                3        | Search by Quantity             
                4        | Search by Price             
                5        | Search by Barcode             
                6        | Search by Expiry Date 
              --------------------------------------            
                
"""))
# search by name                    
                    if filter==1:
                      while True:
                         name=input("Enter the Name of the item here :   ")
                         if all(i.isalpha() or i.isspace() for i in name):
                            break
                         else:
                            print("The name of Food Item can only include alphabets..")
                      found=inven.search_name(name)
                      if found==None:
                         print(f"""
---------------------------------------------------------------------------------------------------------------                               
                               No product found based on your search for Name:{name} 
--------------------------------------------------------------------------------------------------------------- 
""")                        
                      else:   
                          print(f'''
    We found following result(s) for your search for Name:{name}                            
    ------------------------------------------------------------------------
    ''')                      
                          for i in range(len(found))  :
                            print(found[i])           
# search by category                    
                    elif filter==2:
                      while True:
                         cat=input("Enter the Category of the item here :   ")
                         if all(i.isalpha() or i.isspace() for i in cat):
                            break
                         else:
                            print("The category of Food Item can only include alphabets..")
                      found=inven.search_category(cat)
                      if found==None:
                         print(f"""
---------------------------------------------------------------------------------------------------------------                               
                               No product found based on your search for Category:{cat} 
--------------------------------------------------------------------------------------------------------------- 
""")                        
                      else:  
                          print(f'''
    We found following result(s) for your search for Category:{cat}                            
    ------------------------------------------------------------------------
    ''')
                          for i in range(len(found))  :
                            print(found[i])    

# search by Quantity                    
                    elif filter==3:
                     while True:     
                      quantity=int(input("Enter the Quantity of the item here :   "))
                      if all(i.isdigit() for i in str(quantity)):
                        break
                      else:
                        print("The quantity of Food Item can only include digits..")
                      found=inven.search_quantity(quantity)
                      if found==None:
                         print(f"""
---------------------------------------------------------------------------------------------------------------                               
                               No product found based on your search for Quantity:{quantity} 
--------------------------------------------------------------------------------------------------------------- 
""")                        
                      else:  
                          print(f'''
    We found following result(s) for your search for Quantity:{quantity}                            
    ------------------------------------------------------------------------
    ''')
                          for i in range(len(found))  :
                            print(found[i])                                                                     
                                        

# search by Price                    
                    elif filter==4:
                     while True:     
                      price=float(input("Enter the Price in Rs. of the item here :   "))
                      if str(price).count('.')==1 and all(i in '.0123456789' for i in str(price) ):
                        break
                      else:
                        print("The price of Food Item can only be a floating number..")
                      found=inven.search_price(price)
                      if found==None:
                         print(f"""
---------------------------------------------------------------------------------------------------------------                               
                               No product found based on your search for Price:{price} 
--------------------------------------------------------------------------------------------------------------- 
""")                        
                      else:  
                          print(f'''
    We found following result(s) for your search for Price:{price}                            
    ------------------------------------------------------------------------
    ''')
                          for i in range(len(found))  :
                            print(found[i])             

# search by Barcode                    
                    elif filter==5:
                      '''barcode can be of any length and include any character'''
                      barcode=input("Enter the Barcode of the item here :   ")  
                      found=inven.search_barcode(barcode)
                      if found==None:
                         print(f"""
---------------------------------------------------------------------------------------------------------------                               
                               No product found based on your search for Bar/code:{barcode} 
--------------------------------------------------------------------------------------------------------------- 
""")                        
                      else:  
                          print(f'''
    We found following result(s) for your search for Barcode:{barcode}                            
    ------------------------------------------------------------------------
    ''')
                          print(found)                                                                                              
  
# search by Expiry Date                    
                    elif filter==6:
                      while True: 
                          exp= input("Enter the Expiry Date of the item here  (YYYY-MM-DD):   ")
                          if exp.count("-")==2 and len(exp)==10:
                            exp=date.isoformat(date.fromisoformat(exp))
                            break
                          else:
                            print("Kindly use this format YYYY-MM-DD..(e.g., 2024-11-13)")
                      found=inven.search_expdate(exp)
                      if found==None:
                         print(f"""
---------------------------------------------------------------------------------------------------------------                               
                               No product found based on your search for Expiry Date:{exp} 
--------------------------------------------------------------------------------------------------------------- 
""")                        
                      else:  
                          print(f'''
    We found following result(s) for your search for Expiry Date:{exp}                            
    ------------------------------------------------------------------------
    ''')
                          for i in range(len(found)):
                            print(found[i]) 

# for invalid input
                    else:
                       print("""
>>Please , Enter a Valid digit..
""")                                        
#_______________________________________________________________________________________________________
                case _:        # Invalid choice
                  print("""
>>Please , Enter a Valid digit..
""")                      
main()   