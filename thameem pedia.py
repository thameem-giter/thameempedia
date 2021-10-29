from tkinter import *
from tkinter.font import BOLD, Font
import wikipedia
import webbrowser
window = Tk()
window.config(bg='#2C2B27')
window.title('Thameem pedia')
window.geometry('642x507')
def wiki():
    inp = input.get()
    text.insert(INSERT,wikipedia.summary(inp))
def wait():
    waiting = Label(window,text='please wait.......')
doubt = Label(window,text='Your Doubt : ',font=10,bg='#2C2B27',fg='#FFFFFF')
doubt.place(x=5,y=60)
title = Label(window,text='Unlish your Doubt with Thameem',font=BOLD,fg='#FFFFFF',bg='#2C2B27')
title.pack()
input = Entry(window,bd=0)
input.place(x=110,y=62)
b1 = Button(window,bd=0,text='hit me',font=BOLD,command=wiki,bg='#F1C40F')
b1.place(x=280,y=58)
text = Text(window,bg='#2C2B27',fg='#FFFFFF')
text.place(x=-2,y=100)
window.mainloop()