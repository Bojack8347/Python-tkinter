import time
import tkinter as tk
from tkinter import YES

import plyer
from plyer import notification
###Author: Tian Qin 4/22/2021
###Version 2


def reminder(minutes=30,start=False):
    while start:
        notification.notify(
            title="**Please Drink Water now!!",
            message=" The U.S. National Academies of Sciences, Engineering, and Medicine determined that"
                    " an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for"
                    " men. About 11.5 cups (2.7 liters) of fluids a day for women",
            app_icon= "water_bottle.ico",
            # displaying time
            timeout=7
        )

        time.sleep(60*minutes)
def Start():
    #Start button
    # global start
    # start=not start
    window.destroy()

def get_min():
    global minutes
    global start
    start=not start
    minutes= int(entry.get())

if __name__ == "__main__":

    window = tk.Tk()
    window.geometry("275x180")
    window.title('Hello Joy!')


    photo = tk.PhotoImage(file='download.png')

    tk.Label(text="Hello, Joy",fg='white',
            image=photo,
            compound = tk.CENTER).place(relx=0.5,rely=0.5,anchor ='center')# greeting

    label = tk.Label(text="请设置提醒间隔(分钟为单位)")
    entry = tk.Entry(window)

    label.pack()
    entry.pack()

    minutes=3 #initialize
    start = False
    button1 = tk.Button(
        text="确认",
        width=10,
        height=2,
        bg="#34A2FE",
        fg="yellow",command=get_min
    ).place(x=95,y=60)



    button2 = tk.Button(
        text="Start reminding",
        width=15,
        height=2,
        bg="purple",
        fg="yellow",command=window.destroy
    ).place(x=80,y=120)




    window.mainloop()

    reminder(minutes,start)




