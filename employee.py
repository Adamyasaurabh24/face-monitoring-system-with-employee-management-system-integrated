from distutils import dep_util
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2





class Employee():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")
    
 #=====================database variables=======================
        self.var_Dep=StringVar()
        self.var_subdep=StringVar()
        self.var_year=StringVar()
        self.var_package=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_division=StringVar()
        self.var_empno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_employer=StringVar()















    #====================HEAD IMAGE============================
        img=Image.open(r"C:/face monitoring system/images/employee.png")
        img=img.resize((1530,190),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=190)
        f_lbl.pack(anchor="nw")
        
       
     #==================BACKGROUND IMAGE==============================
        img1=Image.open(r"C:/face monitoring system/images/back.jpg")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=180,width=1530,height=700)
        
        title_lbl=Label(bg_img,text=" EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#======================mainframe==================
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
    #left frame
        
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)
        
        #===============leftimage======================
        
        imgleft=Image.open(r"C:/face monitoring system/images/empp.webp")
        imgleft=imgleft.resize((720,120),Image.ANTIALIAS)
        self.photoimgleft=ImageTk.PhotoImage(imgleft)
        f_lbl=Label(left_frame,image=self.photoimgleft)
        f_lbl.place(x=10,y=0,width=700,height=120)
        
        #==================current deployment information====================
        
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current deployment details",font=("times new roman",12,"bold"))
        current_frame.place(x=10,y=125,width=700,height=130)
        #=========department======================
        dep_lbl=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lbl.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_Dep,font=("times new roman",12,"bold"),width=18,state="readonly")
        dep_combo["values"]=("Select Department","HR","Training","Finance","Sales","Development")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        #=================Sub department============================
        c_lbl=Label(current_frame,text=" Sub Department",font=("times new roman",12,"bold"),bg="white")
        c_lbl.grid(row=0,column=4,padx=3,sticky=W)

        c_combo=ttk.Combobox(current_frame,textvariable=self.var_subdep,font=("times new roman",12,"bold"),width=20,state="readonly")
        c_combo["values"]=("Select  Sub Department","Tester","Developer","Finance advisor","Sales manager","Project Head")
        c_combo.current(0)
        c_combo.grid(row=0,column=5,padx=3,pady=1,sticky=W)
        #=====================current working year==================
        year_lbl=Label(current_frame,text="Working Year",font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=18,state="readonly")
        year_combo["values"]=("Select Working Year","First","Second","Third","Fourth","More than four")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=4,pady=8,sticky=W)
        #===================current package==========================
        s_lbl=Label(current_frame,text=" Current Package",font=("times new roman",12,"bold"),bg="white")
        s_lbl.grid(row=1,column=4,padx=2,sticky=W)

        s_combo=ttk.Combobox(current_frame,textvariable=self.var_package,font=("times new roman",12,"bold"),width=20,state="readonly")
        s_combo["values"]=("Select current package","4-lpa","6-lpa","8-lpa","10-lpa","More than 10-lpa")
        s_combo.current(0)
        s_combo.grid(row=1,column=5,padx=4,pady=3,sticky=W)
        
         #================Employees information=====================

        employee_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Employee's details",font=("times new roman",12,"bold"))
        employee_frame.place(x=10,y=260,width=700,height=250)
        #=====================employee id====================
        e_lbl=Label(employee_frame,text="Employee Id:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        employeeid_entry=ttk.Entry(employee_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        employeeid_entry.grid(row=0,column=1,padx=10,sticky=W)
        #====================employee name=====================
        e_lbl=Label(employee_frame,text="Employee Name:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        employeename_entry=ttk.Entry(employee_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        employeename_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #===========================employee division================
        e_lbl=Label(employee_frame,text="Employee division:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        division_combo=ttk.Combobox(employee_frame,textvariable=self.var_division,font=("times new roman",12,"bold"),width=18,state="readonly")
        division_combo["values"]=("Select Division","A","B","C","D")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=8,pady=4,sticky=W)
        #=========================employee number=============
        e_lbl=Label(employee_frame,text="Employee no:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        employeeno_entry=ttk.Entry(employee_frame,textvariable=self.var_empno,width=20,font=("times new roman",12,"bold"))
        employeeno_entry.grid(row=1,column=3,padx=10,sticky=W)
        #====================employee gender================
        e_lbl=Label(employee_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(employee_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Trans","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=8,pady=4,sticky=W)
        #===================date of birth of employee=======
        e_lbl=Label(employee_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=2,column=2,padx=10,sticky=W)
        
        employeedob_entry=ttk.Entry(employee_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        employeedob_entry.grid(row=2,column=3,padx=10,sticky=W)
        #==================employee email===================
        e_lbl=Label(employee_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        employeemail_entry=ttk.Entry(employee_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        employeemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #========================employee phone number===============
        e_lbl=Label(employee_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        employeephone_entry=ttk.Entry(employee_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        employeephone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #========================employee address==============
        e_lbl=Label(employee_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        employeeaddress_entry=ttk.Entry(employee_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        employeeaddress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #=======================employer name==================
        e_lbl=Label(employee_frame,text="Employer Name:",font=("times new roman",12,"bold"),bg="white")
        e_lbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        employer_entry=ttk.Entry(employee_frame,textvariable=self.var_employer,width=20,font=("times new roman",12,"bold"))
        employer_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #==============radio buttons for taking image=============
        self.var_radio1=StringVar()
        take_pic=ttk.Radiobutton(employee_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        take_pic.grid(row=6,column=0)
        
        take_pic1=ttk.Radiobutton(employee_frame,variable=self.var_radio1,text="No photo Sample",value="No")
        take_pic1.grid(row=6,column=1)
        
        take_photo=Button(employee_frame,command=self.generate_dataset,text="Take photo sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo.grid(row=6,column=2)
        update_photo=Button(employee_frame,text="update photo sample",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo.grid(row=6,column=3)
        #=================button frame=========================
        bt_frame=Frame(employee_frame,bd=2,relief=RIDGE,bg="white")
        bt_frame.place(x=0,y=200,width=700,height=30)
        
        save_btn=Button(bt_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(bt_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(bt_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(bt_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
    #right frame
        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)
        
        imgright=Image.open(r"C:/face monitoring system/images/pppp.jpg")
        imgright=imgright.resize((720,120),Image.ANTIALIAS)
        self.photoimgright=ImageTk.PhotoImage(imgright)
        f_lbl=Label(right_frame,image=self.photoimgright)
        f_lbl.place(x=10,y=0,width=700,height=120)
    
    #search system
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search Details",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=125,width=700,height=80)

        search_lbl=Label(search_frame,text="Search by:",font=("times new roman",12,"bold"),bg="white")
        search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=20,state="readonly")
        search_combo["values"]=("Select","employee no","phone no.","employee id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=4,pady=3,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showall_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

    #==================table frame========================

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=700,height=300)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("Dep","subdep","year","package","id","name","div","empno","gender","dob","email","phone","address","employer","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.employee_table.xview) 
        scroll_y.config(command=self.employee_table.yview) 

        self.employee_table.heading("Dep",text="Department",anchor=W)
        self.employee_table.heading("subdep",text="Sub Department",anchor=W)
        self.employee_table.heading("year",text="Working Year",anchor=W)
        self.employee_table.heading("package",text="Package",anchor=W)
        self.employee_table.heading("id",text="Employee Id",anchor=W)
        self.employee_table.heading("name",text="Employee Name",anchor=W)
        self.employee_table.heading("div",text="Employee Division",anchor=W)
        self.employee_table.heading("empno",text="Employee Number",anchor=W)
        self.employee_table.heading("gender",text="Gender",anchor=W)
        self.employee_table.heading("dob",text="D.O.B",anchor=W)
        self.employee_table.heading("email",text="Email",anchor=W)
        self.employee_table.heading("phone",text="Phone No",anchor=W)
        self.employee_table.heading("address",text="Address",anchor=W)
        self.employee_table.heading("employer",text="Employer",anchor=W)
        self.employee_table.heading("photo",text="Photo Sample Status",anchor=W)
        self.employee_table["show"]="headings"

        self.employee_table.column("Dep",width=100)
        self.employee_table.column("subdep",width=120)
        self.employee_table.column("year",width=100)
        self.employee_table.column("package",width=100)
        self.employee_table.column("id",width=100)
        self.employee_table.column("name",width=150)
        self.employee_table.column("div",width=130)
        self.employee_table.column("empno",width=130)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("employer",width=100)
        self.employee_table.column("photo",width=150)
        

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
#==================functions required=======================
    
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_subdep.get()=="" or self.var_year.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="krish@123",database="face_monitoring")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_Dep.get(),
                                                                                                            self.var_subdep.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_package.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_division.get(),
                                                                                                            self.var_empno.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_employer.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            
                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#==================fetching data from database======================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="krish@123",database="face_monitoring")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()        

    def get_cursor(self,event=""):
        cursor=self.employee_table.focus()
        content=self.employee_table.item(cursor)
        data=content["values"]

        self.var_Dep.set(data[0]),
        self.var_subdep.set(data[1]),
        self.var_year.set(data[2]),
        self.var_package.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_division.set(data[6]),
        self.var_empno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_employer.set(data[13]),
        self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_subdep.get()=="" or self.var_year.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update employee details",parent=self.root)
                if update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="krish@123",database="face_monitoring")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update employee set Dep=%s,subdep=%s,year=%s,package=%s,name=%s,division=%s,empno=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,employer=%s,photosample=%s where id=%s",(
                                                                                                                                                                                                        
                                                                                                                                                                                             self.var_Dep.get(),
                                                                                                                                                                                             self.var_subdep.get(),
                                                                                                                                                                                             self.var_year.get(),
                                                                                                                                                                                             self.var_package.get(),
                                                                                                                                                                                        
                                                                                                                                                                                             self.var_name.get(),
                                                                                                                                                                                             self.var_division.get(),
                                                                                                                                                                                             self.var_empno.get(),
                                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                                             self.var_dob.get(),
                                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                                             self.var_phone.get(),
                                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                                             self.var_employer.get(),
                                                                                                                                                                                             self.var_radio1.get(),
                                                                                                                                                                                             self.var_id.get()
                                                                                                                                                                                            
                                                                                                                                                                                         ))
            
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Employee details have been updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Employee id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Delete Page","Do you want to delete this employee",parent=self.root)
                if delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="krish@123",database="face_monitoring")
                     my_cursor=conn.cursor()
                     sql="delete from employee where id=%s"
                     val=(self.var_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employee details",parent=self.root) 

            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_subdep.set("Select subdepartment")
        self.var_year.set("Select year")
        self.var_package.set("Select package")
        self.var_id.set("")
        self.var_name.set("")
        self.var_division.set("Select division")
        self.var_empno.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_employer.set("")
        self.var_radio1.set("")
 #============================taking photo samples======================
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_subdep.get()=="" or self.var_year.get()=="":
            messagebox.showerror("error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="krish@123",database="face_monitoring")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update employee set Dep=%s,subdep=%s,year=%s,package=%s,name=%s,division=%s,empno=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,employer=%s,photosample=%s where id=%s",(
                                                                                                                                                                                                        
                                                                                                                                                                                             self.var_Dep.get(),
                                                                                                                                                                                             self.var_subdep.get(),
                                                                                                                                                                                             self.var_year.get(),
                                                                                                                                                                                             self.var_package.get(),
                                                                                                                                                                                        
                                                                                                                                                                                             self.var_name.get(),
                                                                                                                                                                                             self.var_division.get(),
                                                                                                                                                                                             self.var_empno.get(),
                                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                                             self.var_dob.get(),
                                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                                             self.var_phone.get(),
                                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                                             self.var_employer.get(),
                                                                                                                                                                                             self.var_radio1.get(),
                                                                                                                                                                                             self.var_id.get()==id+1
                                                                                                                                                                                            
                                                                                                                                                                                         ))    
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
#==================loading data on face from opencv==============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                image_id=0
                while True:
                    ret,frame_1=cap.read()
                    if face_crop(frame_1) is not None:
                        image_id+=1
                        face=cv2.resize(face_crop(frame_1),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(image_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(image_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generation of image dataset completed!!")

            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()        