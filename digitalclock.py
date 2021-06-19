from tkinter import *
import time 
window=Tk()
window.resizable(0,0)
window.title("Digital clock")

l=Label(window,bg='maroon',fg='white',font=('Árial',75,'bold'),relief='groove',bd=7)
l.grid(row=0,column=1)
def changetime():
	tm=time.strftime("%H:%M:%S")
	l.config(text=tm)
	l.after(200,changetime)
changetime()
window.mainloop()

