from tkinter import*
from tkinter.font import BOLD
import qrcode
import webbrowser
window = Tk()
window.geometry('300x150')
window.title('qcode maker')
window.config(bg='#fbca03')
def generate():
   img = qrcode.make(input.get())
   img.save('output.png') 
   result = Label(text='output saved',font=BOLD,bg='#aa0505')
   result.place(x=10,y=120)
def web():
   webbrowser.open('www.google.com/search?q='+input.get())
def direct():
   webbrowser.open(input.get())
can = Canvas(window,bg='#aa0505')
can.place(x=0,y=70)
title=Label(window,text='enter your date and get your output',font=BOLD,bg='#fbca03')
title.pack()
input=Entry(window,bd=3)
input.place(x=7,y=45)
b1 = Button(window,bd =2,text='qr code',fg='white',bg='#b97d10',activebackground='white',activeforeground='black',command=generate)
b1.place(x=180,y=40)
b2 = Button(window,bd =2,text='web search',fg='white',bg='#b97d10',activebackground='white',activeforeground='black',command=web)
b2.place(x=130,y=80)
b3= Button(window,bd =2,text='direct search',fg='white',bg='#b97d10',activebackground='white',activeforeground='black',command=direct)
b3.place(x=10,y=80)
window.resizable(0,0)
window.mainloop()



