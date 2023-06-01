from distutils import dep_util
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
from mysqlx import Column
import os
import csv
from tkinter import filedialog




mydata=[]
class MARKPRESENCE():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("MARK PRESENCE")

        self.var_presentyid=StringVar()
        self.var_employeeno=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_present=StringVar()
        
        img=Image.open(r"C:/face monitoring system/images/PRESENCE.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        f_lbl.pack(anchor="nw")

        img1=Image.open(r"C:/face monitoring system/images/po.png")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_img=Label(self.root,image=self.photoimg1)
        f_img.place(x=800,y=0,width=800,height=200)


        #background image
        img2=Image.open(r"C:/face monitoring system/images/back.jpg")
        img2=img2.resize((1530,710),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="EXPORT AND IMPORT DATA",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

         
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Employee Presence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
        
        imgleft=Image.open(r"C:/face monitoring system/images/pop.jpg")
        imgleft=imgleft.resize((720,120),Image.ANTIALIAS)
        self.photoimgleft=ImageTk.PhotoImage(imgleft)
        f_lbl=Label(left_frame,image=self.photoimgleft)
        f_lbl.place(x=10,y=0,width=700,height=120)
          
        l_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        l_frame.place(x=0,y=125,width=720,height=400)
 
        presence_lbl=Label(l_frame,text="Presenty Id:",font=("times new roman",12,"bold"),bg="white")
        presence_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        presence_entry=ttk.Entry(l_frame,width=20,textvariable=self.var_presentyid,font=("times new roman",12,"bold"))
        presence_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        e_lbl=Label(l_frame,text="Employee No:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        employeeid_entry=ttk.Entry(l_frame,width=20,textvariable=self.var_employeeno,font=("times new roman",12,"bold"))
        employeeid_entry.grid(row=0,column=3,padx=10,sticky=W) 
        
        e_lbl=Label(l_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        employeeno_entry=ttk.Entry(l_frame,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        employeeno_entry.grid(row=1,column=1,padx=10,sticky=W)
        
        e_lbl=Label(l_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        employeedob_entry=ttk.Entry(l_frame,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        employeedob_entry.grid(row=1,column=3,padx=10,sticky=W)

        e_lbl=Label(l_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        employeemail_entry=ttk.Entry(l_frame,width=20,textvariable=self.var_time,font=("times new roman",12,"bold"))
        employeemail_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        e_lbl=Label(l_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        employeemail_entry=ttk.Entry(l_frame,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        employeemail_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        e_lbl=Label(l_frame,text="Presenty Status",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(l_frame,font=("times new roman",12,"bold"),width=18,textvariable=self.var_present,state="readonly")
        gender_combo["values"]=("Status","Present","Absent")
        gender_combo.grid(row=3,column=1,padx=8,pady=4,sticky=W)
        gender_combo.current(0)

        
        bt_frame=Frame(l_frame,bd=2,relief=RIDGE,bg="white")
        bt_frame.place(x=0,y=340,width=700,height=30)
        
        import_btn=Button(bt_frame,text="Import csv",command=self.importcsv,width=25,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(bt_frame,text="Export csv",command=self.exportcsv,width=25,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)
        
        
        reset_btn=Button(bt_frame,text="Reset",width=25,command=self.resetdata,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Presence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=450)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.presentyreporttable=ttk.Treeview(table_frame,column=("Presenty Id","Employee No","Name","Department","Time","Date","Presenty Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.presentyreporttable.xview) 
        scroll_y.config(command=self.presentyreporttable.yview) 
        
        self.presentyreporttable.heading("Presenty Id",text="Presenty Id")
        self.presentyreporttable.heading("Employee No",text="Employee No")
        self.presentyreporttable.heading("Name",text="Name")
        self.presentyreporttable.heading("Department",text="Department")
        self.presentyreporttable.heading("Time",text="Time")
        self.presentyreporttable.heading("Date",text="Date")
        self.presentyreporttable.heading("Presenty Status",text="Presenty Status")
        self.presentyreporttable["show"]="headings"

        self.presentyreporttable.column("Presenty Id",width=100)
        self.presentyreporttable.column("Employee No",width=100)
        self.presentyreporttable.column("Name",width=100)
        self.presentyreporttable.column("Department",width=100)
        self.presentyreporttable.column("Time",width=100)
        self.presentyreporttable.column("Date",width=100)
        self.presentyreporttable.column("Presenty Status",width=100)

        self.presentyreporttable.pack(fill=BOTH,expand=1)
        self.presentyreporttable.bind("<ButtonRelease>",self.getcursor)

    def fetchdata(self,rows):
        self.presentyreporttable.delete(*self.presentyreporttable.get_children())
        for i in rows:
            self.presentyreporttable.insert("",END,values=i)
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)    

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data has been exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)           

    def getcursor(self,event=""):
        cursor=self.presentyreporttable.focus()
        content=self.presentyreporttable.item(cursor)
        rows=content['values']
        self.var_presentyid.set(rows[0])
        self.var_employeeno.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_present.set(rows[6])

    
            

    def resetdata(self):
        self.var_presentyid.set("")
        self.var_employeeno.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_present.set("")
    






if __name__=="__main__":
    root=Tk()
    obj=MARKPRESENCE(root)
    root.mainloop()        