from  tkinter import *
import os
def md():
    os.system("py intrusion.py")    
def ud():
    os.system("py user.py")
screen=Tk() 
screen.title("INTRUSION DETECTION") 
screen.geometry("900x600")

l1=Label(screen,text="Intrusion Detection",font='Times 20 bold',width=100,height=4,bg='black',fg='white')

btn1=Button(screen, text='Start Tracking',font='Times 16 bold',width=35,height=4,bg='blue',fg='white',command = md)
btn2=Button(screen, text='Set Target Email',font='Times 16 bold',width=35,height=4,bg='blue',fg='white',command = ud)

l1.pack()
btn1.pack(pady=50)
btn2.pack(pady = 50)
screen.mainloop()
