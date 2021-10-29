from tkinter.font import BOLD
import wolframalpha
import wikipedia
from tkinter import *
import customtkinter
import gtts
from playsound import playsound
from pytube import YouTube
window = Tk()
window.geometry('642x500')
window.title('thameem pedia 2.0')
window.config(bg='#171717')
title =Label(window,text='Thameem Pedia',bg='#171717',fg='#3498DB')
title.place(x=180,y=80)
title.config(font=('Roboto',25,BOLD))
input = customtkinter.CTkEntry(master=window,corner_radius=10,height=35,width=300)
input.place(x=160,y=150)
ans = Label(window,text='Answer : ',font=15,bg='#171717',fg='#FFFFFF')
ans.place(x=5,y=200)
text = Text(window,bg='#171717',fg='#FFFFFF',highlightbackground='#171717',bd=0,highlightcolor='#171717')
text.place(x=-2,y=225)
def search():
    text.delete("1.0","end")
    try:  
       app_id ='5UWY93-AXVXT5QQ6G'
       client = wolframalpha.Client(app_id)
       inp = client.query(input.get())
       res = next(inp.results).text
       text.insert(INSERT,res)
    except :
        inp = input.get()
        text.insert(INSERT,wikipedia.summary(inp)) 
def hi():
    voice = gtts.gTTS('hi,i am Thameem pedia, your personal answering assistant, i can help you with maths problem and article writing and so on, i was build using wolframalpha the answer engine and wikipedia.i was build my thameem. if you get any bug in the program email my creator at thameem 2 1 2 6 @ gmail dot com')
    voice.save("thameempedia.mp3") 
    playsound("thameempedia.mp3") 
def hear():
    inp = text.get('1.0',"end")
    sound = gtts.gTTS(text=inp)
    sound.save('res.mp3')
    playsound('res.mp3')
def clear():
    input.delete(0,'end')
def Downloader():
    url =YouTube(str(input.get()))
    video =url.streams.first()
    video.download()
    Label(window, text ="Successfully Downloaded", font ="arial 15").place(x =180, y =200)
b1 = customtkinter.CTkButton(master=window,corner_radius=10,command=search,text='Go',width=30)
b1.place(x=455,y=150)
window.bind('<Return>',lambda event:search())
b2 = customtkinter.CTkButton(master=window,corner_radius=10,command=hi,text='press to get intro')
b2.place(x=490,y=150)
b3 = customtkinter.CTkButton(master=window,corner_radius=10,command=clear,text='x',height=0,width=0)
b3.place(x=10000,y=150)
window.bind('<Delete>',lambda event:clear())
b4 = customtkinter.CTkButton(master=window,corner_radius=10,command=hear,text='read answer')
b4.place(x=490,y=190)
b5 = Button(window,command=Downloader).pack()
text.config(font=('Roboto',10))
window.resizable(0,1)
window.mainloop()