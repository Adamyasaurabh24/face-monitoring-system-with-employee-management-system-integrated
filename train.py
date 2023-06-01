from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os 
import numpy as np
import cv2


class Train_Faces:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Faces")
        title_lbl=Label(self.root,text="TRAIN FACES",font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:/face monitoring system/images/traan.jpeg")
        img_top=img_top.resize((1530,285),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=285)

        # TRAIN  BUTTON
        b22=Button(self.root,text="Train Faces",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white",activebackground="red",activeforeground="white")
        b22.place(x=0,y=340,width=1530,height=40)

        img_bottom=Image.open(r"C:/face monitoring system/images/piti.png")
        img_bottom=img_bottom.resize((1530,490),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=390,width=1530,height=490)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)    
        

        #=====================training the classifier and saving the context================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Train_Faces(root)
    root.mainloop()