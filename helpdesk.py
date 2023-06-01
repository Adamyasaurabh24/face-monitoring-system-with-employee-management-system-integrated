from tkinter import*
from tkinter import ttk
from turtle import title
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk") 

        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="blue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images/help.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        adm_label=Label(f_lbl,text="Email your queries at:-",font=("times new roman",25,"bold"),bg="white",fg="black")
        adm_label.place(x=750,y=500)
        adm_label=Label(f_lbl,text="pandeyadamyasaurabh@gmail.com",font=("times new roman",20,"bold"),bg="blue",fg="white")
        adm_label.place(x=1100,y=550)
        adm_label1=Label(f_lbl,text="annup1245@gmail.com",font=("times new roman",20,"bold"),bg="blue",fg="white")
        adm_label1.place(x=1100,y=600)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()    

