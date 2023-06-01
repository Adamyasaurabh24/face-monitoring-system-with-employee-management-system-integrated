from cgitb import text
from msilib.schema import Font
from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from helpdesk import Help
from train import Train_Faces
from facemonitoring import FaceMonitoring
from employee import Employee
from markpresence import MARKPRESENCE



class face_monitoring_system():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE MONITORING SYSTEM")
        
        #head image
        img=Image.open(r"C:/face monitoring system/images/face.png")
        img=img.resize((1530,210),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=210)
        f_lbl.pack(anchor="nw")
        
        #background image
        img1=Image.open(r"C:/face monitoring system/images/back.jpg")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=210,width=1530,height=710)
        
        title_lbl=Label(bg_img,text=" FACIAL MONITORING SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        #==================time==================

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


         
        #employee details
        img5=Image.open(r"C:/face monitoring system/images/employee.png")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.employee_details)
        b1.place(x=300,y=100,width=200,height=180)

        b2=Button(bg_img,text="EMPLOYEE DETAILS",cursor="hand2",command=self.employee_details,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2.place(x=300,y=240,width=200,height=40)
        
        #face detector
        img6=Image.open(r"C:/face monitoring system/images/HI.jpg")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_monitoring)
        b3.place(x=530,y=100,width=200,height=180)

        b3=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_monitoring,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b3.place(x=530,y=240,width=200,height=40)
        
        #marks presence
        img7=Image.open(r"C:/face monitoring system/images/emp.png")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.mark_presence)
        b4.place(x=770,y=100,width=210,height=180)

        b4=Button(bg_img,text="PRESENCE MARKING",cursor="hand2",command=self.mark_presence,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4.place(x=770,y=240,width=210,height=40)
        
        #help desk
        img8=Image.open(r"C:/face monitoring system/images/help.png")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_desk)
        b5.place(x=1000,y=100,width=200,height=180)

        b5=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5.place(x=1000,y=240,width=200,height=40)
        
        #train faces
        img9=Image.open(r"C:/face monitoring system/images/train.jpg")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b6.place(x=420,y=350,width=200,height=160)

        b6=Button(bg_img,text="TRAIN FACES",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b6.place(x=420,y=510,width=200,height=40)
        
        #photos
        img10=Image.open(r"C:/face monitoring system/images/faces.jpg")
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b7.place(x=670,y=350,width=200,height=160)

        b7=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7.place(x=670,y=510,width=200,height=40)

        
        #terminate
        img11=Image.open(r"C:/face monitoring system/images/term.jpg")
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b7.place(x=910,y=350,width=200,height=160)

        b7=Button(bg_img,text="TERMINATE",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7.place(x=910,y=510,width=200,height=40)

    def open_img(self):
        os.startfile("data")    
  #==================functions button===========================
   
    def employee_details(self):
        self.new_window=Toplevel(self.root) 
        self.app=Employee(self.new_window)   
    
    def mark_presence(self):
        self.new_window=Toplevel(self.root) 
        self.app=MARKPRESENCE(self.new_window)   
    
    def train_data(self):
        self.new_window=Toplevel(self.root) 
        self.app=Train_Faces(self.new_window)   
    
    def face_monitoring(self):
        self.new_window=Toplevel(self.root) 
        self.app=FaceMonitoring(self.new_window)
    
    def help_desk(self):
        self.new_window=Toplevel(self.root) 
        self.app=Help(self.new_window)
    
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Confirmation","Are you sure you want to exit this project",parent=self.root)    
        if self.exit>0:
            self.root.destroy()
        else:
             return

if __name__=="__main__":
    root=Tk()
    obj=face_monitoring_system(root)
    root.mainloop()
     
    
 
