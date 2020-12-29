# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:26:40 2020

@author: Gurkirat
"""
import tkinter
import PIL
import os
import PIL.Image, PIL.ImageTk




from sklearn.metrics import pairwise
import pickle
import tensorflow as tf
from tkinter import *
from tkinter import messagebox
import numpy as np
import os
import cv2
from PIL import Image, ImageDraw
import PIL.ImageOps
from keras.models import load_model
import tkinter as tk
from PIL import ImageTk, Image
from drowsiness_detection import fun
from yawn import fun1

sroot = Tk()
sroot.title('Accident Prevention')
sroot.minsize(height=516,width=1020)
sroot.configure(bg='white')
facial="C:/Users/Gurkirat/Desktop/New Folder/driver.jpg"
img0 = ImageTk.PhotoImage(Image.open(facial))
panel = Button(sroot,image=img0)
panel.image = img0
panel.place(x=0,y=0)

#chilanka
Label(sroot,text=" Accident Prevention ",font='Timesnewroman 40 ',bg='white',fg='black').place(x=535,y=10)

def main():
    window=tkinter.Tk()

    face="C:/Users/Gurkirat/Desktop/New Folder/face.jpg"
    img = ImageTk.PhotoImage(Image.open(face))
    voice="C:/Users/Gurkirat/Desktop/New Folder/voice.jpg"
    img = ImageTk.PhotoImage(Image.open(voice))
    
    window.title('Accident Prevention')
    window.geometry('1000x700')


    window = Frame( window)
    window.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    window.configure(relief=GROOVE)
    window.configure(borderwidth="2")
    window.configure(relief=GROOVE)
    window.configure(background="#d9d9d9")
    window.configure(highlightbackground="#d9d9d9")
    window.configure(highlightcolor="black")
    window.configure(width=925)
    
    window.configure(background="#d9d9d9")
    window.configure(highlightbackground="#d9d9d9")
    window.configure(highlightcolor="black")
    lblHeading = Label(window,text = "\t\t\t\t Accident Prevention \t\t\t\t",font=('Calibri',30,'bold'), bg="#d9d9d9",height=3).pack()
    b1=Button(window,padx=16,pady=4,bd=4,fg="white",font=('arial',16,'bold'),width=22,height=2,bg="gray25",text='Yawn Detector',command=fun1)
    b1.place(x=100,y=420)
    b2=Button(window,padx=16,pady=4,bd=4,fg="white",font=('arial',16,'bold'),width=22,height=2,bg="gray25",text='Drowsiness Detector',command=fun)
    b2.place(x=550,y=420)
    
    
    face="C:/Users/Gurkirat/Desktop/New Folder/yawn.jpg"
    img1 = ImageTk.PhotoImage(Image.open(face))
    panel = Button(window, image = img1,command=fun1)
    panel.image = img1
    panel.place(x=100,y=110)
    voice="C:/Users/Gurkirat/Desktop/New Folder/drow.jpg"
    img2 = ImageTk.PhotoImage(Image.open(voice))
    panel2 = Button(window, image = img2,command=fun)
    panel2.image = img2
    panel2.place(x=550,y=110)
    window.mainloop()
   
def call_mainroot():
	sroot.destroy()
	main()
sroot.after(2500,call_mainroot)



mainloop()
    
