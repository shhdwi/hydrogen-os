#%%
import os                                             
#imported for choosing files in musicplayer 
import pyttsx3                                        
#pip install pyttsx3
import datetime
import wikipedia                                    
#pip install wikipedia
import webbrowser
from matplotlib import pyplot as plt             
#imported to plot graphs in graphic calculator
import time                                                      
#imported for clock
import numpy as np                                       
#imported to help in plotting graphs
import requests                                              
#imported for taking info from websites
import tkinter as tk                                         
#imported for functioning of GUI 
import tkinter.messagebox                            
#imported for error messages 
import tkinter.filedialog as file                       
#importing for shortening code 
import mysql.connector as mycon               
#imported for mysql connectivity
import tkinter.ttk as ttk                                   
#importing for adding styles
from pygame import mixer                            
#imported for working of music player
mixer.init()                                                      
 #initializing         
paused=False
 #variable used to define the state of music player
import json

def login():                                                      
#Function for the checking login details 
    global username,Password 
#Global variable used to check username and password for login
    with open('database','r') as f1:                 
 #file handling used to check login details 
        d=f1.readlines()                                     
#reads lines from the files and gives a list
        status = False
        for i in range(0,len(d),2):
#range taken in 2 as username and password are alternate
            if (username.get()==d[i].rstrip('\n')) and Password.get()==d[i+1].rstrip('\n'):
#checks if the entered password and login are correct 
                 Main()      
                 status=True
      #  if status==True:
        #              tk.messagebox.showinfo('Thank You!','You have logged out successfully'+'\n'+'close the window')                  
#calling main to open app drawer/main window
        if status==False:
#if login details don’t match
#Message box used to show error
                 tk.messagebox.showerror('ERROR!', 'wrong password') 
                 
def loginopt():                                                     
#Function for the login window 
    global username,Password  
#Global variable used to check username and password for login  
    root2=tk.Toplevel()                                          
#Top level is used to create a new window
    userlab=tk.Label(root2,text='username:')     
#Label for showing where to type username
    userlab.grid(row=0,column=0)
#grid used for arranging items on the login in screen
    username=tk.Entry(root2)                               
#Entry to give a box to enter username
    username.grid(column=1,row=0) 
#grid used for arranging items on the login in screen 
    passlab=tk.Label(root2,text='password:')      
#Label for showing where to type password 
    passlab.grid(row=1,column=0) 
#grid used for arranging items on the login in screen 
#Entry to give a box to enter password showing as * to provide privacy
    Password=tk.Entry(root2,show='*')
    Password.grid(row=1,column=1) 
#grid used for arranging items on the login in screen
#button used for calling function to check login details k  
    tk.Button(root2,text='login check',command=login).grid(column=1,row=2)     


def loginopt2():
#Function for the login window 
    global username,Password
#Global variable used to check username and password for login
    root2=tk.Toplevel()
#Top level is used to create a new window
    userlab=tk.Label(root2,text='username:')       
#Label for showing where to type username
    userlab.grid(row=0,column=0) 
#grid used for arranging items on the login in screen
    username=tk.Entry(root2)                                
#Entry to give a box to enter username
    username.grid(column=1,row=0)
 #grid used for arranging items on the login in screen 
    passlab=tk.Label(root2,text='password:')      
#Label for showing where to type password 
    passlab.grid(row=1,column=0)
 #grid used for arranging items on the login in screen
 #Entry to give a box to enter password showing as * to provide privacy  
    Password=tk.Entry(root2,show='*') 
    Password.grid(row=1,column=1)
#grid used for arranging items on the login in screen
#button used for calling function to check login details  
    tk.Button(root2,text='login check',command=login).grid(column=1,row=2) 


def register():                                                         
#Function for register detail checking
#Global variable to check the new user details 
                    global newpass,confuser,newuser 
                    global username 
#Global variable used to check username for login 
                    global Password 
#Global variable used to check password for login
#Checking if the password entered and confirmed are the same 
                    if newpass.get()==confuser.get(): 
                        if len(newuser.get())>=8:
 #Checking the length of the username to be atleast 8 
                            with open('database','a+') as f1: 
#File handling used to add new user details
                               f1.write(newuser.get()+'\n')                    
                               f1.write(newpass.get()+'\n') 
                               f1.close() 
                            root4=tk.Toplevel()                       
#Top level is used to create a new window
 #Label to show that the details matched the criterion required 
                            tk.Label(root4,text='You have successfully registered').pack() 
 #Button redirecting to the login screen 
                            tk.Button(root4,text='Proceed to login',command=loginopt2).pack()
                            root4.mainloop() 
                        else:
   #Error message
                            tkinter.messagebox.showerror('ERROR', 'pls enter a  username with 8 char’')
                    else:
 #Error message
                        tkinter.messagebox.showerror('ERROR!','Both the passwords dont match')


def registeropt():                                                            
 #Function for the register window  
    global newpass,confuser,newuser  
 #Global variable to check the new user details
    root3=tk.Toplevel()                             
#Top level is used to create a new window
 #Label for showing where to type password
    tk.Label(root3,text='Enter Username:').grid(column=0,row=0)
    newuser=tk.Entry(root3)                    
#Entry to give a box to enter new username 
    newuser.grid(column=1,row=0)        
#grid used for arranging items on the register screen
#Label for showing where to type password                
    tk.Label(root3,text='Enter Password:').grid(column=0,row=1)
    #Entry to give a box to enter new password showing as * to provide privacy 
    newpass=tk.Entry(root3,show='*')
    newpass.grid(column=1,row=1)        
#grid used for arranging items on the register screen
 #Label for showing where to confirm password 
    tk.Label(root3,text='Confirm Password:').grid(column=0,row=2) 
 #Entry to give a box to confirm new password showing as * to provide privacy            
    confuser=tk.Entry(root3,show='*')
    confuser.grid(column=1,row=2) 
#grid used for arranging items on the register screen
#Button to proceed to register checking  
    registerlab=tk.Button(root3,text=' proceed to register',command=register)
    registerlab.grid(row=3,column=1)
#grid used for arranging items on the register screen 
    root3.mainloop()                            
 #To execute the window in mainloop 
def registeropt2():                              
 #Function for the register window  
    global newpass,confuser,newuser
#Global variable to check the new user details
    root3=tk.Toplevel()                         
#Top level is used to create a new window
#Label for showing where to type password
    tk.Label(root3,text='Enter Username:').grid(column=0,row=0)                
    newuser=tk.Entry(root3)                 
#Entry to give a box to enter new username 
    newuser.grid(column=1,row=0)
#grid used for arranging items on the register screen
#Label for showing where to type password                
    tk.Label(root3,text='Enter Password:').grid(column=0,row=1)
#Entry to give a box to enter new password showing as * to provide privacy 
    newpass=tk.Entry(root3,show='*')
    newpass.grid(column=1,row=1)
#grid used for arranging items on the register screen
#Label for showing where to confirm password               
    tk.Label(root3,text='Confirm Password:').grid(column=0,row=2)
 #Entry to give a box to confirm new password showing as * to provide privacy 
    confuser=tk.Entry(root3,show='*')
    confuser.grid(column=1,row=2)
#grid used for arranging items on the register screen
#Button to proced to register checking 
    registerlab=tk.Button(root3,text=' proceed to register',command=register) 
    registerlab.grid(row=3,column=1)
#grid used for arranging items on the register screen 
    root3.mainloop()                               
#To execute the window in mainloop 

def newsheading():
      rootn=tk.Toplevel()
      rootn.title('News Headings')
      def speak(str):
          from win32com.client import Dispatch
          speak = Dispatch("SAPI.SpVoice")
          speak.Speak(str)
      Text=tk.Text(rootn)        
      Text.grid(column=0,row=1,columnspan=5)                
      ph1=tk.PhotoImage(file=r'toi.png')
      bottom=tk.Frame(rootn)
      bottom.grid(column=0,row=2)
      def toi():
           Text.delete(1.0,tk.END)
           speak("News for today.. Lets begin")
           url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=debcf199554c41dba1c1c992e175138a"
           news = requests.get(url).text
           news_dict = json.loads(news)
           arts = news_dict['articles']
           for article in arts:   
                  q=article['title']
                  Text.insert(tk.INSERT,q+'\n')     
                  rootn.update()
                  speak(article['title'])        
                     
           speak("Thanks for listening...") 
      toi=tk.Button(bottom,image=ph1,command=toi)
      toi.grid(column=4,row=2)
      
      ph2=tk.PhotoImage(file=r'NEWS.png') 
      def googlenews():
           Text.delete(1.0,tk.END)
           speak("News for today.. Lets begin")
           url = "https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=debcf199554c41dba1c1c992e175138a"
           news = requests.get(url).text
           news_dict = json.loads(news)
           arts = news_dict['articles']
           for article in arts:   
                  q=article['title']
                  Text.insert(tk.INSERT,q+'\n')     
                  rootn.update()
                  speak(article['title'])        
            
           speak("Thanks for listening...") 
      googlenews=tk.Button(rootn,image=ph2,command=googlenews)
      googlenews.grid(column=3,row=2)
      def thehindu():
           Text.delete(1.0,tk.END)
           speak("News for today.. Lets begin")
           url = "https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=debcf199554c41dba1c1c992e175138a"
           news = requests.get(url).text
           news_dict = json.loads(news)
           arts = news_dict['articles']
           for article in arts:   
                  q=article['title']
                  Text.insert(tk.INSERT,q+'\n')     
                  rootn.update()
                  speak(article['title'])        
                
           speak("Thanks for listening...") 
      ph3=tk.PhotoImage(file=r'thehindu.png') 
      hindu=tk.Button(bottom,image=ph3,command=thehindu)
      hindu.grid(column=2,row=2)
      def bbc1():
           Text.delete(1.0,tk.END)
           speak("News for today.. Lets begin")
           url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=debcf199554c41dba1c1c992e175138a"
           news = requests.get(url).text
           news_dict = json.loads(news)
           arts = news_dict['articles']
           for article in arts:   
                  q=article['title']
                  Text.insert(tk.INSERT,q+'\n')     
                  rootn.update()
                  speak(article['title'])        
                 
           speak("Thanks for listening...") 
      ph4=tk.PhotoImage(file=r'bbc.png') 
      bbc=tk.Button(bottom,image=ph4,command=bbc1)
      bbc.grid(column=1,row=2)
      ph5=tk.PhotoImage(file=r'espn.png') 
      def espn1():
           Text.delete(1.0,tk.END)
           speak("News for today.. Lets begin")
           url = "https://newsapi.org/v2/top-headlines?sources=espn&apiKey=debcf199554c41dba1c1c992e175138a"
           news = requests.get(url).text
           news_dict = json.loads(news)
           arts = news_dict['articles']
           for article in arts:   
                  q=article['title']
                  Text.insert(tk.INSERT,q+'\n')     
                  rootn.update()
                  speak(article['title'])        

           speak("Thanks for listening...") 
      espn=tk.Button(bottom,image=ph5,command=espn1)
      espn.grid(column=0,row=2)
      rootn.mainloop()
def Main():                                             
#Function for the main Window 
   root=tk.Toplevel()                              
#Top level is used to create a new window
   from time import strftime                 
#time imported to use in clock
   def time1():                                        
#function for constantly changing the label 
       string = strftime('%H:%M:%S %p \n%d%B,%Y')
#Using for showing  Time and Date
       lbl.config(text = string)                                         
#Config to set the string as time and date
       lbl.after(1000, time1)                                             
#Code to change the label every second
   lbl=tk.Label(root,font=("DS-Digital",75))
#Label to use for clock which is displayed
   lbl.grid(column=1,row=1,columnspan=4) 
#grid used for arranging items on the main screen
   time1()                                                                        
#function called to change time
   root.title('Hydrogen OS')                                          
#Title of window
#Label for giving a welcome message 
   text=tk.Label(root, text ='Welcome to Hydrogen OS')
#grid used for arranging items on the main screen      
   text.grid(row=0,column=1,columnspan=4)
   photo=tk.PhotoImage(file=r'NEWS4.png')
#Photo imported for using as app icon
#Button for accessing application 
   btn1=tk.Button(root,image=photo,text='NEWS',command=newsheading)
   btn1.grid(row=2,column=1) 
#grid used for arranging items on the main screen        
   tk.Label(root, text ='NEWS').grid(row=3,column=1)
   photo1=tk.PhotoImage(file=r'music.png') 
#Photo imported for using as app icon
#Button for accessing application  
   btn2=tk.Button(root,image=photo1,command=Musicplayer)
   btn2.grid(row=2,column=2) 
#grid used for arranging items on the main screen 
   tk.Label(root, text ='MUSIC PLAYER').grid(row=3,column=2)
   photo2=tk.PhotoImage(file=r'calculator.png') 
#Photo imported for using as app icon
#Button for accessing application  
   btn3=tk.Button(root,image=photo2,command=calculator)
   btn3.grid(row=2,column=3)
#grid used for arranging items on the main screen 
   tk.Label(root, text ='CALCULATOR').grid(row=3,column=3)
   photo3=tk.PhotoImage(file=r'phone.png') 
#Photo imported for using as app icon 
   btn4=tk.Button(root,image=photo3,command=contacts)
#Button for accessing application
   btn4.grid(row=2,column=4) 
#grid used for arranging items on the main screen 
   tk.Label(root, text ='Contacts' ).grid(row=3,column=4)
   photo4=tk.PhotoImage(file=r'stocks.png') 
#Photo imported for using as app icon
   btn5=tk.Button(root,image=photo4,command=graphs)
#Button for accessing application
   btn5.grid(row=4,column=1)
#grid used for arranging items on the main screen 
   tk.Label(root, text ='GRAPHS').grid(row=5,column=1)
   photo5=tk.PhotoImage(file=r'Wallet.png')
#Photo imported for using as app icon 
   btn6=tk.Button(root,image=photo5,command=GST) 
#Button for accessing application
   btn6.grid(row=4,column=2) 
#grid used for arranging items on the main screen 
   tk.Label(root, text ='GST').grid(row=5,column=2)
   photo7=tk.PhotoImage(file=r'clock.png') 
#Photo imported for using as app icon
   btn8=tk.Button(root,image=photo7,command=clock)
#Button for accessing application 
   btn8.grid(row=4,column=3) 
#grid used for arranging items on the main screen 
   tk.Label(root, text ='CLOCK').grid(row=5,column=3)
   photo6=tk.PhotoImage(file=r'robot.png')
#Photo imported for using as app icon
   btn7=tk.Button(root,image=photo6,command=Assistant)
    #Button for accessing application
   btn7.grid(row=4,column=4)
#grid used for arranging items on the main screen 
   tk.Label(root, text ='ASSISTANT').grid(row=5,column=4)
   root.mainloop()#To execute the window in mainloop


def Musicplayer():                                                             
#Function for music player app

    global statusbar                                                          
 #global variable for te programme title bar
    root2=tk.Toplevel()                                                        
#Toplevel used for a new window  
    root2.title('Music Player')                                               
 #gives a name to the window
    menubar=tk.Menu(root2)                                                     
#menubar 
    root2.config(menu=menubar)                                                
 #config for menu
    subMenu=tk.Menu(menubar,tearoff=0)                                         
#creating the sub menu and tearoff used  for removing things that are not needed 
    def browse_file():                                                        
 #lets you browse for an audio file to play music
        global filename 
        filename=file.askopenfilename() 
#getting the name of file to display on statusbar
        print(filename) 
 
 
    menubar.add_cascade(label='File',menu=subMenu) 
 # cascade used to add things on menubar
    subMenu.add_command(label='open',command=browse_file) 
# adding things to sub menubar
    subMenu.add_command(label='Exit',command=root2.destroy)
# Exiting the program from the subtitle bar
    subMenu=tk.Menu(menubar,tearoff=0) 
    menubar.add_cascade(label='Help',menu=subMenu) 
    subMenu.add_command(label='About',command=about_us) 
    text=tk.Label(root2, text ='Music Player') 
    text.pack() 
    middleframe=tk.Frame(root2,relief=tk.RAISED,borderwidth=2)
# frame used to keep Play ,Pause and Stop in one place 
    middleframe.pack(padx=10,pady=10) 
    bottomframe=tk.Frame(root2)
#frame used to place the mute,volume and rewind in one place 
    bottomframe.pack(padx=10,pady=30) 
    photo5=tk.PhotoImage(file=r'play.png') 
    btn5=tk.Button(middleframe,image=photo5,command=play_music) 
    btn5.image=photo5 
    btn5.grid(row=0,column=0,padx=10) 
    photo6=tk.PhotoImage(file=r'stop.png') 
    btn6=tk.Button(middleframe,image=photo6,command=stop_music) 
    btn6.image=photo6 
    btn6.grid(row=0,column=1,padx=10) 
    photo7=tk.PhotoImage(file=r'pause.png') 
    btn7=tk.Button(middleframe,image=photo7,command=pause_music) 
    btn7.image=photo7 
    btn7.grid(row=0,column=2,padx=10) 
    photo8=tk.PhotoImage(file=r'rewind.png') 
    btn8=tk.Button(bottomframe,image=photo8,command=play_music) 
    btn8.image=photo8 
    btn8.grid(row=1,column=0,padx=10) 
    def mute_music(): 
         mixer.music.set_volume(0) 
#pygame module used to set volume
         scale.set(0) 
    mute=tk.PhotoImage(file=r'mute.png') 
    btn9=tk.Button(bottomframe,image=mute,command=mute_music) 
    btn9.grid(row=1,column=2,padx=10) 
    scale=tk.Scale(bottomframe,from_=0,to=100,orient=tk.HORIZONTAL,command=set_vol) 
#volume scale is defined and calibrated with tkinter scale
    scale.set(50) 
#default volume scale is set as 50
    mixer.music.set_volume(0.5) 
    scale.grid(row=1,column=1,padx=10) 
    statusbar=tk.Label(root2,text='Welcome to Music Player',relief=tk.SUNKEN,anchor=tk.W) 
    statusbar.pack(side=tk.BOTTOM,fill=tk.X) 
    root2.mainloop()

def play_music(): 
   global paused 
   if paused: 
       paused =False                           
 #checks if music is paused 
       mixer.music.unpause() 
       statusbar['text']="Now Playing   "+os.path.basename(filename) 
   else: 
       try:                    
          mixer.music.load(filename) 
          mixer.music.play() 
          statusbar['text']="Now Playing   "+os.path.basename(filename) 
       except: 
          tkinter.messagebox.showerror('ERROR!', 'Select a Music File' ) 
def stop_music(): 
    mixer.music.stop()
#pygame module used to stop music 
    statusbar['text']="Music Stopped" 
def pause_music(): 
    global paused 
    paused=True 
    mixer.music.pause() 
#Pygame module used to pause the music
    statusbar['text']="Music Paused" 
def set_vol(val): 
    volume=int(val)/100
#volume scale is set  
    mixer.music.set_volume(volume) 
def about_us(): 
#shows about the music player
    tkinter.messagebox.showinfo('About','Music Player version 1.1.0')


def calculator():                                                              
#Function for calculator app    
    root3=tk.Toplevel()                                                        
#Top level is used to create a new window  
    root3.title('Calculator')                                                  
#Title of window     
    E1=tk.Entry(root3,width=35,borderwidth=5)                                  
#Entry to accept numbers to equate   
    E1.grid(row=1,column=0,columnspan=3,padx=10,pady=10)                      
 #grid for arrangement of the entry 
    def button_click(number):                                                  
#Function to give a number when the button is clicked
        current=E1.get()                                                       
        E1.delete(0,len(current))                                              
#deletes if there is any previous number after any function is clicked
        E1.insert(0,str(current)+str(number))                                  
#inserts numbers you click
    def button_equal():                                                       
 #Function to give a solution when the button is clicked                                         
        sec_number=E1.get()                                                   
 #takes the second number's value
        E1.delete(0,len(sec_number))                                           
#deletes the second number to print the result
        if math=='Addition':                                                  
 #checks and adds the number
            E1.insert(0,f_num+int(sec_number)) 
        elif math=='Subtraction':                                              
#checks and subtracts the number 
            E1.insert(0,f_num-int(sec_number)) 
        elif math=='Division':                                                 
#checks and divides the number 
            E1.insert(0,f_num/int(sec_number)) 
        elif math=='Multiplication':                                           
#checks and multiplies the number 
            E1.insert(0,f_num*int(sec_number)) 
        elif math=='exp':                                                      
#checks to exponentially increase the number
            E1.insert(0,f_num**int(sec_number)) 
        else: 
           tkinter.messagebox.showerror('ERROR!', 'Enter a valid operation')   
#error message
           button_clear()                                                      
#calls the function to clear the entry box
    def button_clear():                                                        
#Function to clear the number 
        c1=E1.get()  
        E1.delete(0,len(c1)) 
    def button_Del():                                                          
#Function to clear the last digit 
        c1=E1.get() 
        E1.delete(len(c1)-1) 
    def button_add():                                                          
#Function to add 
        first_number=E1.get() 
        global f_num 
        global math 
        math='Addition'                                                        
#sets the value of variable to be Addition so that it adds the two numbers
        f_num=float(first_number) 
        E1.delete(0,len(first_number))  
    def button_Exp(): 
        first_number=E1.get() 
        global f_num 
        global math 
        math='exp'                                                             
#sets the value of variable to be Addition so that it powers the two numbers 
        f_num=float(first_number) 
        E1.delete(0,len(first_number)) 
    def button_Divide(): 
        first_number=E1.get() 
        global f_num 
        global math 
        math='Division'                                                        
#sets the value of variable to be Addition so that it divides the two numbers
        f_num=float(first_number) 
        E1.delete(0,len(first_number)) 
    def button_subtract(): 
        first_number=E1.get() 
        global f_num 
        global math 
        math='subtraction'                                                     
#sets the value of variable to be Addition so that it subtracts the two numbers 
        f_num=float(first_number) 
        E1.delete(0,len(first_number))
    def button_Multiply(): 
        first_number=E1.get() 
        global f_num 
        global math 
        math='Multiplication'                                                 
 #sets the value of variable to be Addition so that it multiplying the two numbers 
        f_num=float(first_number) 
        E1.delete(0,len(first_number)) 
    btn_0=tk.Button(root3,text='0',padx=40,pady=20,command=lambda: button_click(0))
#Button for typing 0 
    btn_1=tk.Button(root3,text='1',padx=40,pady=20,command=lambda: button_click(1))
#Button for typing 1 
    btn_2=tk.Button(root3,text='2',padx=40,pady=20,command=lambda: button_click(2))
#Button for typing 2 
    btn_3=tk.Button(root3,text='3',padx=40,pady=20,command=lambda: button_click(3))
#Button for typing 3 
    btn_4=tk.Button(root3,text='4',padx=40,pady=20,command=lambda: button_click(4))
#Button for typing 4 
    btn_5=tk.Button(root3,text='5',padx=40,pady=20,command=lambda: button_click(5))
#Button for typing 5 
    btn_6=tk.Button(root3,text='6',padx=40,pady=20,command=lambda: button_click(6))
#Button for typing 6 
    btn_7=tk.Button(root3,text='7',padx=40,pady=20,command=lambda: button_click(7))
#Button for typing 7 
    btn_8=tk.Button(root3,text='8',padx=40,pady=20,command=lambda: button_click(8))
#Button for typing 8 
    btn_9=tk.Button(root3,text='9',padx=40,pady=20,command=lambda: button_click(9))
#Button for typing 9 
    btn_add=tk.Button(root3,text='+',padx=39,pady=20,command= button_add) 
 #Button for adding
    btn_sub=tk.Button(root3,text='-',padx=40,pady=20,command= button_subtract)
 #Button for subtracting
    btn_mul=tk.Button(root3,text='x',padx=42,pady=20,command= button_Multiply) 
#Button for multiplying
    btn_div=tk.Button(root3,text='/',padx=40,pady=20,command= button_Divide)   
#Button for dividing
    btn_exp=tk.Button(root3,text='exp',padx=34,pady=20,command= button_Exp)    
#Button for Exponential function
    btn_equal=tk.Button(root3,text='=',padx=40,pady=20,command=button_equal)   
#Button for equating
    btn_clear=tk.Button(root3,text='Clear',padx=29,pady=20,command= button_clear)
#Button for clearing  
    btn_del=tk.Button(root3,text='Del',padx=34,pady=20,command= button_Del)   
 #Button for deleting
    btn_0.grid(row=5,column=0)                                                 
#grid used for arranging items on the calculator screen  
    btn_1.grid(row=4,column=0)                                                 
#grid used for arranging items on the calculator screen 
    btn_2.grid(row=4,column=1)                                                 
#grid used for arranging items on the calculator screen 
    btn_3.grid(row=4,column=2)                                                 
#grid used for arranging items on the calculator screen 
    btn_4.grid(row=3,column=0)                                                 
#grid used for arranging items on the calculator screen 
    btn_5.grid(row=3,column=1)                                                 
#grid used for arranging items on the calculator screen 
    btn_6.grid(row=3,column=2)                                                 
#grid used for arranging items on the calculator screen   
    btn_7.grid(row=2,column=0)                                                 
#grid used for arranging items on the calculator screen 
    btn_8.grid(row=2,column=1)                                                 
#grid used for arranging items on the calculator screen 
    btn_9.grid(row=2,column=2)                                                 
#grid used for arranging items on the calculator screen 
    btn_add.grid(row=6,column=0)                                               
#grid used for arranging items on the calculator screen 
    btn_mul.grid(row=7,column=1)                                               
#grid used for arranging items on the calculator screen 
    btn_div.grid(row=7,column=2)                                               
#grid used for arranging items on the calculator screen 
    btn_sub.grid(row=7,column=0)                                               
#grid used for arranging items on the calculator screen 
    btn_exp.grid(row=6,column=2)                                               
#grid used for arranging items on the calculator screen 
    btn_equal.grid(row=6,column=1)                                             
#grid used for arranging items on the calculator screen 
    btn_clear.grid(row=5,column=1)                                             
#grid used for arranging items on the calculator screen 
    btn_del.grid(row=5,column=2)                                               
#grid used for arranging items on the calculator screen 
    root3.mainloop()                                                           
#To execute the window in mainloop     


def graphs():                                                                  
#Function for graph app
    rootgr=tk.Toplevel()                                                       
#Top level is used to create a new window  
    x=0                                                                        
#variable for x axis                                                           
    rootgr.title('graphs')                                                     
#Title of window             
    def functions():                                                           
#Function to equate the function   
        global x 
        x=np.linspace(int(ra1.get()),int(ra2.get()),10000)                  
#breaks the range into 10000 equal parts 
        eq1= Xentry.get()                                                      
#takes the equation 
        try:                                                                   
#tries and then replaces wherever needed to make the program user friendly
           string1=eq1.replace('cos','np.cos')                                 
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('sin','np.sin')                             
#replaces the code with a numpy part to execute as per the user wants 
           string1=string1.replace('^','**')                                   
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('log','np.log10')                           
#replaces the code with a numpy part to execute as per the user wants 
           string1=string1.replace('ln','np.log')                              
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('tan','np.tan')                             
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('floor','np.floor')                         
#replaces the code with a numpy part to execute as per the user wants 
           string1=string1.replace('ceil','np.ceil')                           
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('x','(x)')                                  
#replaces the code with a numpy part to execute as per the user wants
           y=eval(string1) 
           plt.plot(x,y) 
           plt.xlim(int(ra1.get()),int(ra2.get())) 
           plt.savefig(r'graph.png')                                           
#save the graph
           plt.show() 
           root2gr=tk.Toplevel()                                               
#Top level is used to create a new window 
           root2gr.title('graph')                                              
#Title of window 
           photo8=tk.PhotoImage(file=r'graph.png')                             
#Photo imported for using as graph                 
           ph=tk.Label(root2gr,image=photo8)                                  
 #Label to show the graph 
           ph.grid(row=2,column=5)                                             
#grid used for arranging graph
           root2gr.mainloop()                                                  
#To execute the window in mainloop
        except :                                                 
#checking for errors
            c1=eq1.count('(') 
            c2=eq1.count(')') 
            if c1 != c2: 
                    tkinter.messagebox.showerror('ERROR!', 'close the brackets! or try using "*" sign')
#Error message
            if 'sin' or'cos' or 'tan' or'log'or 'ln'or 'floor'or'ceil'or'^'in eq1 and '(' not in eq1: 
                tkinter.messagebox.showerror('ERROR!', 'Use brackets \nFor example:\nsin(x+1)\n'+'Or\n'+'Use "*" while Multiplying' )
#Error message 
            elif '*'not in eq1: 
                    tkinter.messagebox.showerror('ERROR!', 'Use "*" while Multiplying' )
#Error message 
            else: 
                    tkinter.messagebox.showerror('ERROR!', 'Enter a valid input' )
#Error message 
    tk.Label(rootgr,text="Enter the equation: ").grid(row=0,column=0)          
#Label for showing where to type the equation 
    Xentry=tk.Entry(rootgr,width=35,borderwidth=5)                             
#Entry to give a box to enter equation 
    Xentry.grid(row=1,column=0,columnspan=3,padx=10,pady=10)                   
#grid used for arranging items on the graph screen 
    tk.Label(rootgr,text="Enter Starting Limit: ").grid(row=2,column=0)        
#Label for showing where to type starting limit
    ra1=tk.Entry(rootgr)                                                       
#Entry to give a box to enter starting limit
    ra1.grid(row=2,column=1)                                                   
#grid used for arranging items on the calculator screen 
    tk.Label(rootgr,text="Enter Ending Limit: ").grid(row=3,column=0)          
#Label for showing where to type ending limit 
    ra2=tk.Entry(rootgr)                                                       
#Entry to give a box to enter ending limit   
    ra2.grid(row=3,column=1)                                                   
#grid used for arranging items on the calculator screen 
    tk.Button(rootgr,text='plot',command=functions).grid(row=4,column=1)       
#Button for plotting
    rootgr.mainloop()                                                          
#To execute the window in mainloop 


def stopclock():                                                               
#Function for stopclock
    def update_timeText():                                                     
#function to constantly update the stopwatch
        global state                                                          
#Global variable used to check to start the stopwatch
        global timer                                                           
#Global variable used to use as the label
        if (state):                                                            
#this code changes the stopwatch seconds minutes and hours
            timer[2] += 1 
            if (timer[2] >= 60): 
                timer[2] = 0   
                timer[1] += 1 
            if (timer[1] >= 60): 
                 timer[0] += 1 
                 timer[1] = 0 
            timeString = pattern.format(timer[0], timer[1], timer[2])          
#this sets the pattern of the label 
            timeText.configure(text=timeString)                                
#configures the label
        root7.after(1000, update_timeText)                                     
#updates the label every second
    def start():                                                               
#function that describes the start of stopwatch
        
        global state 
        state = True 
    def pause():                                                               
#function that stops the stopwatch
        global state 
        state = False 
    def reset():                                                               
#function that resets the stopwatch
        global timer 
        timer = [0, 0, 0] 
        timeText.configure(text='00:00:00') 
    def exist():                                                               
#function that ends the stopwatch and quits the application
        root7.destroy() 
    global state 
    state = False                                                              
#global variable to start or stop the stopwatch
    root7=tk.Toplevel() 
    root7.title('Stopwatch') 
    timer=[0, 0, 0] 
    
    pattern='{0:02d}:{1:02d}:{2:02d}' 
    timeText=tk.Label(root7, text="00:00:00", font=("Helvetica", 150)) 
    timeText.pack() 
    startButton = tk.Button(root7, text='Start', command=start) 
    startButton.pack() 
    pauseButton = tk.Button(root7, text='Pause', command=pause) 
    pauseButton.pack() 
    resetButton = tk.Button(root7, text='Reset', command=reset) 
    resetButton.pack() 
    quitButton = tk.Button(root7, text='Quit', command=exist) 
    quitButton.pack() 
    update_timeText()
    reset()
    root7.mainloop()  


def timer1():                                                                 
 #Function for timer
       def countDown():                                                       
 #function to constantly update the timer
           lbl1.config(height=3, font=('times', 20, 'bold')) 
           a=r.get() 
           for k in range(int(a), 0, -1):                                      
#for decreasing the number every second               
               lbl1["text"] = k                                                
#text to display in label
               root2.update()                                                  
#updates the label to the new value
               time.sleep(1)                                                   
#updates the label every second 
           tkinter.messagebox.showinfo('Timer','Time Up!') 
       root2 =tk.Toplevel()                                                    
#Top level is used to create a new window 
       root2.title("Timer")                                                    
#Title of window 
       r=tk.Entry(root2)                                                       
#takes for how many secs you want the timer to work
       r.pack()                                                                
#packs the entry box
       tk.Button(root2,text='start timer',command=countDown).pack()            
#Button to start function of timer 
       lbl1 = tk.Label(root2)                                                  
#Label to use for timer
       lbl1.pack(fill='both', expand=1)                                        
#packs the label on which the timer will start
       root2.mainloop()                                                        
#To execute the window in mainloop 


def clock():                                                                   
#Function for calculator app 
         root5= tk.Toplevel()                                                 
 #Top level is used to create a new window
         root5.title('Clock')                                                 
 #Title of window
         from time import strftime                                            
 #time imported to use in clock
         def time1():                                                         
 #function for constantly changing the label 
            string = strftime('%H:%M:%S %p \n%d%B,%Y')                         
#Using for showing  Time and Date
            lbl.config(text = string)                                          
#Config to set the string as time and date
            lbl.after(1000, time1)                                              
#Code to change the label every second
         lbl=tk.Label(root5,font=("DS-Digital",75))                            
#Label to use for clock which is displayed
         lbl.grid(column=1,row=1,columnspan=4)                                 
#grid used for arranging items on the main screen
         time1()                                                               
#function called to change time
         btn7=tk.Button(root5,text='stopwatch',command=stopclock)             
 #Button to access stopwatch              
         btn7.grid(column=2,row=1)                                             
#grid used for arranging items on the clock
         btn8=tk.Button(root5,text='timer',command=timer1)                     
#Button to access timer  
         btn8.grid(column=3,row=1)                                             
#grid used for arranging items on the clock
         root5.mainloop()                                                      
#To execute the window in mainloop


def GST():                                                                     
#Function for GST
  status='Inc'                                                                
 #Variable defined as default calculating method
  rootG=tk.Toplevel()                                                          
#Top level is used to create a new window  
  rootG.title('GST')                                                           
#Title of window 
  p=0                                                                          
#variable determining the percentage
  def btn5():                                                                  
#Function for defining 5% gst
      global p 
      p=5 
  def btn12():                                                                 
#Function for defining 12% gst 
      global p 
      p=12 
  def btn18():                                                                 
#Function for defining 18% gst 
      global p 
      p=18 
  def btn28():                                                                 
#Function for defining 28% gst 
      global p 
      p=28 
  def Inc():                                                                   
#Function to define include gst option 
      global status   
      status='Inc' 
  def Exc():                                                                   
#Function to define exclude gst option
      global status 
      status='Exc' 
  tk.Label(rootG,text='Indian GST Calculator').grid(row=0,column=0,columnspan=4)
#Label to show the top message
  tk.Label(rootG,text='''Select GST rate:''').grid(row=1,column=0,columnspan=4)
#Label to show the part to select the percentage 
  btn5=tk.Button(rootG,text='5%',command=btn5).grid(row=2,column=0)             
#Button to set 5% as rate
  btn12=tk.Button(rootG,text='12%',command=btn12).grid(row=2,column=1)          
#Button to set 12% as rate 
  btn18=tk.Button(rootG,text='18%',command=btn18).grid(row=2,column=2)          
#Button to set 18% as rate 
  btn28=tk.Button(rootG,text='28%',command=btn28).grid(row=2,column=3)          
#Button to set 28% as rate 
  tk.Label(rootG,text='''Select value Including or Excluding GST''').grid(row=3,column=0,columnspan=4)
#Label to show the part to choose type of GST  
  Inc=tk.Button(rootG,text='Including GST',command=Inc).grid(row=4,column=0,columnspan=2)
#Button to select the type of GST 
  Exc=tk.Button(rootG,text='Excluding GST',command=Exc).grid(row=4,column=2,columnspan=2)
#Button to select the type of GST 
  x1=tk.Entry(rootG)                                                           
#place to enter the Amount 
  x1.grid(row=5,column=0,columnspan=4) 
  def submit():                        
    try:                                        
#Function for defining submit button
      y1=x1.get() 
      s1=int(y1) 
      global p,status 
      def excgst(s1,p):                                                        
#Function to calculate exclude gst option
                    t=s1-s1*(p/100) 
                    return t 
      def incgst(s1,p):                                                        
#Function to calculate include gst option
                    t=s1*100/(100-p) 
                    return t 
      if status=='Inc':
          tkinter.messagebox.showinfo('GST','the value is :\n'+str(incgst(s1,p))) 
          #tk.(rootG,text=str(incgst(s1,p))).grid()                        
#Label to show the result 
      if status=='Exc': 
          tkinter.messagebox.showinfo('GST','the value is :\n'+str(excgst(s1,p)))                        
#Label to show the result
    except Exception as e:
        tkinter.messagebox.showerror('Error',e)
        
  submit=tk.Button(rootG,text='submit',command=submit).grid(row=6,column=0,columnspan=4)
#Button to start executing the GST function 
  rootG.mainloop()                                                             
#To execute the window in mainloop
def contacts():                         
#function for contacts app
      root9=tk.Toplevel()                     
#Top level is used to create a new window
      try:                              
#try is used to use the sql table if it already exists
          mc=mycon.connect(host="localhost",user="root",passwd="",database="csproject")#connection establisher
          q=mc.cursor()                 
#cursor object
      except:                           
#except creates a table if the database doesn't exist
          mc=mycon.connect(host="localhost",user="root",passwd="")
#connection establisher
          q=mc.cursor()                 
#cursor object
#commands to create a database and table
          query1="create database csproject"
          query2="""create table contacts
          (Name varchar(30),
          Phone_no varchar(20) primary key)"""
          print('table has been created')
          q1='use csproject;'
          q.execute(query1)
          q.execute(q1)
          q.execute(query2)
          mc.commit()                   
#commit flushes the changes to mysql client
      def add():                        
#function to add contacts
          def add_num():                
#function for adding value in the table
              try:                      
#try and except for checking for errors in the input data              
                  n=name.get()
                  no=int(number.get())
                  values=(n,no)
                  q.execute("insert into contacts values (%s,%s)",values)
                  mc.commit()           
#commit flushes the changes to mysql client
                  tkinter.messagebox.showinfo("Contact","Contact has been successfully saved")
              except Exception as err:
# used for error message
                  tkinter.messagebox.showerror("Error",err)
          a=tk.Toplevel()               
#Top level is used to create a new window
          tk.Label(a,text="Enter Name").grid(row=0,column=0)
#grid used for arranging items
          name=tk.Entry(a)              
#Entry to give a box to enter name
          name.grid(row=0,column=1)
#grid used for arranging items
          tk.Label(a,text="Enter Number").grid(row=1,column=0)
#grid used for arranging items
          number=tk.Entry(a)              
#Entry to give a box to enter number
          number.grid(row=1,column=1)
#grid used for arranging items
          tk.Button(a,text="Add",command=add_num).grid(row=2,column=0,columnspan=2)
#Button used for adding in table
          a.mainloop()                  
#To execute the window in mainloop
      def Delete():                     
#function to delete contacts
          def del_num():                
#function to delete by number
            try:                       
#try and except for checking for errors in the input data
              a1=(dn.get(),)
              q.execute('delete from contacts where Phone_no = %s',a1)
#deletes from table
              mc.commit()               
#commit flushes the changes to mysql client
              if q.rowcount ==0:        
#rowcount checks how many rows are affected
                  tkinter.messagebox.showerror("Contact","There is no such Number in your directory")
              else:
                tkinter.messagebox.showinfo("Contact","Contact has been successfully deleted")
            except Exception as err:
# used for error message
                  tkinter.messagebox.showerror("Error",err)
          def del_name():                
#function to delete by name
            try:                         
#try and except for checking for errors in the input data
              a2=(dn.get(),)
              q.execute('delete from contacts where Name like "%s"',a2)
#deletes from table
              mc.commit()              
 #commit flushes the changes to mysql client
              if q.rowcount ==0:        
#rowcount checks how many rows are affected
#messagebox used to give user info
                  tkinter.messagebox.showerror("Contact","There is no such Name in your directory")
              else:
                  tkinter.messagebox.showinfo("Contact","Contact has been successfully deleted")
            except Exception as err:
# used for error message
                  tkinter.messagebox.showerror("Error",err.msg)
          def Del_num():                    
#function for window to delete by number
              global dn                     
#Global variable used to get entry data
              d=tk.Toplevel()               
#Top level is used to create a new window
              tk.Label(d,text="Enter Number whose contact is to be discarded").grid(row=0,column=0)
#grid used for arranging items
              dn=tk.Entry(d)                
#Entry to give a box to enter number
              dn.grid(row=0,column=1)       
#grid used for arranging items
              tk.Button(d,text="Delete",command=del_num).grid(row=1,column=0,columnspan=2)
#Button used for deleting from table
              d.mainloop()                  
#To execute the window in mainloop
          def Del_name():                   
#function for window to delete by name
              global dna                    
#Global variable used to get entry data
              e=tk.Toplevel()              
 #Top level is used to create a new window
              tk.Label(e,text="Enter Name whose contact is to be discarded").grid(row=0,column=0)
#grid used for arranging items
              dna=tk.Entry(e)               
#Entry to give a box to enter name
              dna.grid(row=0,column=1)      
#grid used for arranging items
              tk.Button(e,text="Delete",command=del_name).grid(row=1,column=0,columnspan=2)
#Button used for deleting from table
              e.mainloop()                  
#To execute the window in mainloop
          b=tk.Toplevel()                   
#Top level is used to create a new window
          tk.Button(b,text="Delete by Number",command=Del_num).grid()
#Button used for opening new screen
          tk.Button(b,text="Delete by Name",command=Del_name).grid()
#Button used for opening new screen
          b.mainloop()                      
#To execute the window in mainloop
      def Update():                         
#function for window to update details
          def upda_num():                   
#function for updating by number
            try:                            
#try and except for checking for errors in the input data
              q.execute('update contacts set Phone_no = %s where Name = %s',(unew.get(),un.get()))
#updates the table data
              mc.commit()                   
#commit flushes the changes to mysql client
              if q.rowcount == 0:           
#rowcount checks how many rows are affected
                  tkinter.messagebox.showerror("Contact","There is no such Name in your directory")
              else:
                  tkinter.messagebox.showinfo("Contact","Contact has been successfully updated")
            except Exception as err:
# used for error message
                  tkinter.messagebox.showerror("Error",err)
          def upda_name():                 
 #function for updating by name
            try:                            
#try and except for checking for errors in the input data
              q.execute('update contacts set Name= %s where Phone_no = %s ',(unewa.get(),una.get()))
#updates the table data
              mc.commit()                   
#commit flushes the changes to mysql client
              if q.rowcount == 0:           
#rowcount checks how many rows are affected
                  tkinter.messagebox.showerror("Contact","There is no such Number in your directory")
              else:
                  tkinter.messagebox.showinfo("Contact","Contact has been successfully updated")
            except Exception as err:
# used for error message
                  tkinter.messagebox.showerror("Error",err)
          def upd_num():                    
#function for window to update by number
              global un,unew                
#Global variable used to get entry data
              f=tk.Toplevel()               
#Top level is used to create a new window
              tk.Label(f,text="Enter Name").grid(row=0,column=0)
              un=tk.Entry(f)                
#Entry to give a box to enter name
              un.grid(row=0,column=1)       
#grid used for arranging items
              tk.Label(f,text="Enter New Number").grid(row=1,column=0)
#grid used for arranging items
              unew=tk.Entry(f)              
#Entry to give a box to enter new number
              unew.grid(row=1,column=1)     
#grid used for arranging items
              tk.Button(f,text="Update",command=upda_num).grid(row=2,column=0,columnspan=2)
#Button used for updating contact
              f.mainloop()                  
#To execute the window in mainloop
          def upd_name():                   
#function for window to update by name
              global una,unewa              
#Global variable used to get entry data
              g=tk.Toplevel()               
#Top level is used to create a new window
              tk.Label(g,text="Enter Number").grid(row=0,column=0)
#grid used for arranging items
              una=tk.Entry(g)               
#Entry to give a box to enter number
              una.grid(row=0,column=1)      
#grid used for arranging items
              tk.Label(g,text="Enter New Name").grid(row=1,column=0)
#grid used for arranging items
              unewa=tk.Entry(g)            
 #Entry to give a box to enter  new name
              unewa.grid(row=1,column=1)    
#grid used for arranging items
              tk.Button(g,text="Update",command=upda_name).grid(row=2,column=0,columnspan=2)#Button used for updating contact
              g.mainloop()                  
#To execute the window in mainloop
          c=tk.Toplevel()                   
#Top level is used to create a new window
          tk.Button(c,text="Update Name",command=upd_name).grid()
#Button used for opening new screen
          tk.Button(c,text="Update Number",command=upd_num).grid()
#Button used for opening new screen
          c.mainloop()                      
#To execute the window in mainloop
      def see():                            
#function to see contacts window
          def se():                         
#funtion to display contacts
              numbers.delete(1.0,tk.END)    
#deletes earlier information in the textbox
              q.execute('select * from contacts')
#command to see all the table contents
              h=q.fetchall()                
#gets all the table contents
              for i in h :                  
#to print in a row type format
                  numbers.insert(tk.INSERT,(str(i)+'\n'))
#inserts data on the text box
          k=tk.Toplevel()               
#Top level is used to create a new window
          numbers=tk.Text(k)           
 #Text box used to show the
          numbers.grid()                
#grid used for arranging items
          tk.Button(k,text="See contacts",command=se).grid()
#Button used for opening new screen
          k.mainloop()                  
#To execute the window in mainloop
      ttk.Label(root9,text="Contacts").grid(columnspan=1) 
#grid used for arranging items
      ttk.Button(root9,text="Add Contact",command=add).grid(columnspan=1)
#Button used for opening new screen
      ttk.Button(root9,text="Delete Contact",command=Delete).grid(columnspan=1)
#Button used for opening new screen
      ttk.Button(root9,text="Modify Contact",command=Update).grid(columnspan=1)
#Button used for opening new screen
      ttk.Button(root9,text="See Contacts",command=see).grid(columnspan=1)
#Button used for opening new screen
      root9.mainloop()                  
#To execute the window in mainloop
      


def Assistant():           
#function for assistant
   rootas=tk.Toplevel()   
#creating new window 
   rootas.title('ASSISTANT')
   engine = pyttsx3.init('sapi5')   
#defining variable ‘engine’ for python text to speech
   voices = engine.getProperty('voices') 
#getting voices from engine(defined earlier)
   engine.setProperty('voice', voices[0].id) 
#selecting male voice for assistant (for female voice use(‘voices[1].id’)




   def speak(audio):                       
# function for converting text to speech
       engine.say(audio)
       engine.runAndWait()
   def wishMe():                               
# greeting by assistant
      hour = int(datetime.datetime.now().hour)  
# date time module used to get exact time 
      if hour>=0 and hour<12:
        speak("Good Morning!")
    
      elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    
      else:
        speak("Good Evening!")  
      speak("I am Your assistant , Bumble BEE. Please tell me how may I help you")  
   wishMe()
   Text=tk.Text(rootas)        
#Text box used to show the conversation
   Text.grid()                
#grid used for arranging items   
   
   def fun1(query):                       
# functions that assistant can do
       if 'wikipedia' in query:         
#wikipedia module used to search wikipedia
           speak('SEARCHING WIKIPEDIA...')
           query=query.replace('wikipedia','')
           results = wikipedia.summary(query, sentences=2)
           Text.insert(tk.INSERT,f"BumbleBee: {results}\n")
           rootas.update()
           speak("According to Wikipedia")
           speak(results)
       elif 'open clock'in query:
           Text.insert(tk.INSERT,'BumbleBee:opening clock\n')
           rootas.update()
           speak("OPENING CLOCK")
           clock()
       elif 'open graph'in query:
           Text.insert(tk.INSERT,'BumbleBee:opening Graphs\n')
           rootas.update()
           speak("OPENING GRAPHS")
           graphs()
       elif 'open news ' in query:
           Text.insert(tk.INSERT,'BumbleBee:opening News \n')
           rootas.update()
           speak("OPENING NEWS")
           newsheading() 
       elif 'open gst'in query:
           Text.insert(tk.INSERT,'BumbleBee:opening GST\n')
           rootas.update()
           speak("OPENING G.S.T.")
           GST()
       elif 'open calculator'in query:
           Text.insert(tk.INSERT,'BumbleBee:opening Calculator\n')
           rootas.update()
           speak("OPENING Calculator.")
           calculator()
       elif 'open music'in query:
           Text.insert(tk.INSERT,'BumbleBee:opening Music Player\n')
           rootas.update()
           speak("OPENING MUSIC PLAYER.")
           Musicplayer()
       elif 'open google' in query:
           Text.insert(tk.INSERT,'BumbleBee:opening Google\n')
           rootas.update()
           webbrowser.open("google.com")
           speak("OPENING GOOGLE...")
       elif 'hey' in query or 'hi' in query:
           Text.insert(tk.INSERT,'BumbleBee:Heyy!,My Name is BumbleBee ,How May I help You?\n')
           rootas.update()
           speak("My Name is BUMBLE BEEEEE!!! ,How May I help You?")
       elif 'what can you do' in query:
           Text.insert(tk.INSERT,'''BumbleBee:Hi! I am here to help you can try these:
               Open Calculator 
               Open music
               Open clock 
               Open Graphs
               Open news
               Open Google
               Open youtube
               Open website example.com
               Wikipedia Search ''')
           rootas.update()
           speak('''Hi!, I am here to help you can try these:
                     ''')           
       elif 'open youtube' in query:
           Text.insert(tk.INSERT,'BumbleBee:opening Youtube\n')
           rootas.update()
           webbrowser.open("youtube.com")
           speak("OPENING Youtube...")
       elif 'open website' in query:
           s1=query
           s1=s1.replace('open website','')
           Text.insert(tk.INSERT,'BumbleBee:opening'+s1+'\n')
           print(s1)
           rootas.update()
           try:
              webbrowser.open("https://www."+s1[1:])
              speak('opening'+s1)
           except:
               tkinter.messagebox.showerror('ERROR!', 'invalid website url' ) 
               speak('invalid webite url')
               speak('try again')
               
   def takecommand():
       query=E1.get()
       Text.delete(1.0,tk.END)
       E1.delete(0,tk.END)
       Text.insert(tk.INSERT,'USER: '+query+'\n')
       rootas.update()
       print(query)
       fun1(query)
       
   E1=tk.Entry(rootas,width=35,borderwidth=5)                                  
#Entry to accept numbers to equate   
   E1.grid(row=1,column=0,columnspan=3,padx=10,pady=10)                       
#grid for arrangement of the entry 
   b1=tk.Button(rootas,text='Submit',command=takecommand)
   b1.grid()


   rootas.mainloop()

root=tk.Tk() 
                                                             
#Tk used to open opening screen
pht=tk.PhotoImage(file=r'LOGO.png')                  
#photo image for importing image 
btn2=tk.Label(root,image=pht)                              
#label to display image
btn2.grid(columnspan=1)
tk.Label(root,text="LOGIN",font=("Calibri", 13)).grid()
#label for opening message 
loginopt=tk.Button(root,text='Existing User',command=loginopt)
#Button for logging in 
loginopt.grid() #grid used for arranging items on the opening screen
#Button for register new user
registeropt=tk.Button(root,text='New User',command=registeropt)
registeropt.grid(padx=30,pady=20)  
#grid used for arranging items on the opening screen
root.mainloop()                                                               
 #To execute the window in mainloop
