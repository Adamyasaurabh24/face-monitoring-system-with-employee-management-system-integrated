from sys import path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import numpy as np
import cv2
import mysql.connector
from time import strftime
from datetime import datetime


class FaceMonitoring:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face monitoring")
       
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:/face monitoring system/images/ramu.webp")
        img_top=img_top.resize((680,780),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=680,height=760)

        img_top1=Image.open(r"C:/face monitoring system/images/ram.webp")
        img_top1=img_top1.resize((850,780),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=670,y=40,width=850,height=760)

        b2=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="light blue",fg="black")
        b2.place(x=330,y=680,width=180,height=40)
    #=============================marking presence================    
    def mark_presence(self,n,i,d):
        with open("krishna.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list)and(i not in name_list)and(d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{d},{dtString},{d1},Present")

# =======================face recognition=====================

    def face_recog(self):
        
        def draw_bound(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="krish@123",database="face_monitoring",port=3306)
                my_cursor=conn.cursor()
                

                my_cursor.execute("select name from employee where id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)
                n="+".join(n)

                my_cursor.execute("select id from employee where id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)
                i="+".join(i)

                my_cursor.execute("select Dep from employee where id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)
                d="+".join(d)
                




                if confidence>75:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                    # cv2.putText(img,"Access Granted",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Name:krishna kartik mishra",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"id:245",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:Development",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_presence(n,i,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Access Denied",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_bound(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("C:/face monitoring system/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/face monitoring system/classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recogniton",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

            
if __name__=="__main__":
    root=Tk()
    obj=FaceMonitoring(root)
    root.mainloop()