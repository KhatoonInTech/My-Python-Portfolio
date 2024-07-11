import history as h
import responses as r
from turtle import*
import colorsys
import winsound as ws
import random
from tabulate import tabulate


#_______________________________________________________________________________
def welcome():   #welcoming user with flowery patttern
    speed(5e100000000000)
    bgcolor("black")
    h=0
    
    for i in range(16):
        for j in range(18):
            c=colorsys.hsv_to_rgb(h,1,1)
            h+=0.005
            color(c)
            ws.Beep(random.randint(150,1500),random.randint(30,60))
            rt(90)
            circle(150-j*6,90)
            lt(90)
            circle(150-j*6,90)
            rt(180)
            circle(40,24)

 
#_________________________________________________________________________________ 
def login()  :   #greet and login
   print("""
             <<<<         PEAKY
                             BLINDERSSS      >>>>
  
              -------------------------------------
                   --------------------------
          
""")
   user=input("""
  >>Enter user name here:
""")
   

   return user  #returning user name
#_____________________________________________________________________________________________
def chatbot(prm_user_input,user):      #generating responses from bot side
    bot=r.bot_responses.Responses(user)
    for keywords ,responses in bot.peaky_blinders_chatbot.items() :
        #if keywords lies in user input  ..
            if keywords.lower() in prm_user_input.lower():
                bot_output=responses
                return bot_output
            
    #partial search    
    for keywords,responses in bot.peaky_blinders_chatbot.items() :
            if any(word.lower() in prm_user_input.lower() for word in keywords.split() ) :
                bot_output=responses
                return bot_output          
                    
    #if user input does't lie in keywords
    bot_output=bot.no_info_responses[random.randint(0,len(bot.no_info_responses))]
    return bot_output     
            
            
#_____________________________________________________________________________________________
def main():     #main function
    
    user=login()
    track_history=h.database.csvfiling(user)
    track_history.create()
    

    while True:
        user_input=input(f'{user} : ')   
        exit=["bye","see you later", "later","adios","peace out", "catch you on the flip side","i gotta go","talk to you later","exit", "quit"]   
        # when user asks for history
        rec_keys=['show record','show history','display record','display history','keep track']
        if any( keywords.lower() in user_input.lower() for keywords in rec_keys):
           
                print(f'''
  Peaker  : Oh my gosh ,you got the sacred spirits of Peaky Blinders to probe into my secrets...😎
            Here's the our secret convo record😉
                Go to the path:  {track_history.database}      
''')         
                    
        else:
            #getting bot responses
            bot_output=chatbot(user_input,user)

            #keeping record of the conversation
            track_history.adding_to_file([{user:user_input ,"Peaker":bot_output}])

            #printing out bot's response 
            print(f'''
    Peaker : {bot_output}
    ----------------------------------------------------------------------------------------------
    ''')  
            #breaking while loop when user wants to discontinue 
            if any(keyword in user_input.lower() for keyword in exit):
              break
      
         
    
        
main()    