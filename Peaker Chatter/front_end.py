from tkinter import *
from PIL import Image,ImageTk
import history as h
import responses as r
import random



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
            
   
              
#_________________________________________________________________________________________________________________________
def main():
    global labe,next,log_get,track_history
    log_get = log.get().title()
    la.place_forget()
    log.place_forget()
    signin.place_forget()
    heading.place_forget()
    
    #showing the welcoming text
    lab=Label(fr,text="""
    Welcome to the world of 
    <<<   PEAKY
                            BLINDERS   >>>    
            ----------------------------""",font=("Arial Black",10),bg="#3D3A31",fg='white',width=65,height=5,justify='center')
    lab.place(x=350,y=50)
    
    # creating a csv file to create history of user conversationwith the bot
    track_history=h.database.csvfiling(log_get)
    track_history.create()

    #showing congratulations message
    labe=Label(fr,text=f"""
    Congrats {log_get}, you're now an official buudy in the club of 
    <<<   PEAKY
                            BLINDERS   >>>    
            ----------------------------""",font=("Arial Black",15),bg="white",fg='#3D3A31',width=65,height=7,justify='center')
    labe.place(x=220,y=200)
     #showing NEXT button
    next=Button(fr,text='NEXT >>',font=("Arial Black",13),width=15,height=3,bg='#3D3A31',fg='white',command=lambda : userchat(0))
    next.place(x=570,y=470)

#_______________________________________________________________________________________________________________________________________________  
#manipulating user side of chat
def userchat(value):
    if value==0:  #coming from 'next' button 
        next.place_forget()
        labe.place_forget()
    if value==1:  #coming frm 'reply' button
        botname.place_forget()
        botresp.place_forget()
        reply.place_forget()

    global enter,head,user_input
    head=Label(fr,text=f"{log_get} : ",font=("Arial Black",10),bg="#161511",fg='white',width=15,height=2,justify='left')
    head.place(x=60,y=200)

    #taking input from user
    user_input=Entry(fr,bg='#8B8B8B',fg='black',borderwidth=10,width=142)
    user_input.insert(0,"...")
    user_input.place(x=235,y=200)
    
    #displaying send button
    enter=Button(fr,text='SEND',font=("Arial Black",10),width=10,height=2,bg='#161511',fg='white',command= botchat)
    enter.place(x=1130,y=200)
   
#___________________________________________________________________________________________________________________________________________________________   
#manipulating bot side of chat
def botchat():   
    user_input_get= user_input.get()
    global botname,botresp,reply
    botname=Label(fr,text=f"Peaker : ",font=("Arial Black",10),bg="#161511",fg='white',width=15,height=2,justify='left')
    botname.place(x=60,y=350)  

    reply=Button(fr,text='Reply',font=("Arial Black",10),width=10,height=2,bg='#161511',fg='white',command= lambda : userchat(1))
    reply.place(x=1130,y=350)

    #displaying bot responses
    bot_output=chatbot(user_input_get,log_get).replace("?","?\n")
    botresp=Label(fr,text=f'''{bot_output.replace(".",".\n")}''',bg='#8B8B8B',fg='black',font=("Arial BlackSSS",10),justify='left')
    botresp.config(width=110,height=10)
    botresp.place(x=235,y=300)
    #storing in database
    track_history.adding_to_file([{log_get:user_input_get ,"Peaker":bot_output}])
    

#_________________________________________________________________________________________________________________________________

def login():
    signup.place_forget()
    global signin,heading,log

    #instructing user to input user
    heading=Label(fr,text="User Name:",font=("Arial Black",10),bg="#3D3A31",fg='white',width=10,height=2,justify='left')
    heading.place(x=400,y=350)

    #taking username from user
    log=Entry(fr,bg='#8B8B8B',fg='black',borderwidth=10,width=35)
    log.insert(0,'Your Username')
    log.place(x=540,y=350)
    
    #Log In Button
    signin=Button(fr,text='Log in',font=("Arial Black",10),width=10,height=1,bg='#3D3A31',fg='white',command=main)
    signin.place(x=800,y=350)
   
#___________________________________________________________________________________________________________
root=Tk()
root.geometry("2048x2048")
root.config(background="#39352C")
root.title("PeaKer Chatter")
root.iconbitmap(r"C:\Users\Super\Desktop\Chatbot\icon.ico")

fr=Frame(root).pack()
#displaying image
img=ImageTk.PhotoImage(Image.open(r"C:\Users\Super\Desktop\Chatbot\ii.jpg"))
l=Label(fr,image=img).pack(padx=30,pady=30)
global la,signup
#showing the welcoming text
la=Label(fr,text="""
Welcome to the world of 
<<<   PEAKY
                        BLINDERS   >>>    
           ----------------------------""",font=("Arial Black",15),bg="#3D3A31",fg='white',width=30,height=5,justify='left')
la.place(x=480,y=150)

#sign up button for user
signup=Button(fr,text='Sign up',font=("Arial Black",15),width=15,height=3,bg='#3D3A31',fg='white',command=login)
signup.place(x=570,y=350)

root.mainloop()

