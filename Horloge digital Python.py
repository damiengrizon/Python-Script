from tkinter import *
from datetime import datetime

app_window = Tk()
app_window.title("horloge numérique")
app_window.geometry("370x150")
app_window.resizable(1,1)

text_fond = ("Forte", 68, 'bold')
background = "#33FFAA"
foreground = "#FFFFFF"
border_width = 25

label = Label(app_window, font = text_fond, bg = background, fg = foreground, bd =  border_width)

label.grid(row=0, column=1)

def digital_clock() :
    now = datetime.now()
    time_live = now.strftime('%H:%M:%S')
    label.config(text = time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()