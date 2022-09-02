from re import L
from tkinter import *
import os

def restart():
    os.system("restart /r /t 1")
def restart_time():
    os.system("restart /r /t 20")
def log_out():
    os.system("restart -l")
def shutdown():
    os.system("restart /s /t 1")

st = Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="sky Blue")

r_button = Button(st,text="Restart",font=("Time New Roman",12,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=210,y=20,height=30,width=110)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",12,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=210,y=70,height=30,width=110)

lg_button = Button(st,text="Log-out",font=("Time New Roman",12,"bold"),relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=210,y=120,height=30,width=110)

sd_button = Button(st,text="Shut Down",font=("Time New Roman",12,"bold"),relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=210,y=170,height=30,width=110)





st.mainloop()