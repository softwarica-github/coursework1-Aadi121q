from tkinter import *
from tkinter import messagebox
from argparse import FileType
#from stegano import lsb
from tkinter.filedialog import *
from PIL import ImageTk,Image
#from  stegano.lsbset import generators
from stegano import lsb
from tkinter import font as tkFont
from stegano import exifHeader as aaa
import os
from subprocess import Popen


def encode():
	main.destroy()
	enc=Tk()
	enc.attributes("-fullscreen", True)
	enc.wm_attributes('-transparentcolor')
	img=ImageTk.PhotoImage(Image.open("bg2.jpg"))
	fontl = tkFont.Font(family='Algerian', size=32)
	label1=Label(enc,image=img)
	label1.pack()

	LabelTitle=Label(text="ENCODE",bg="red",fg="white",width=20)
	LabelTitle['font']=fontl
	LabelTitle.place(relx=0.6, rely=0.1)

	def openfile():
		global fileopen
		global imagee
		
		fileopen=StringVar()
		fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*"))) 
		imagee=ImageTk.PhotoImage(Image.open(fileopen))
		
		Labelpath=Label(text=fileopen)
		Labelpath.place(relx=0.6, rely=0.25, height=21, width=450)

		Labelimg=Label(image=imagee)
		Labelimg.place(relx=0.7, rely=0.3, height=200, width=200)
		
main.mainloop()