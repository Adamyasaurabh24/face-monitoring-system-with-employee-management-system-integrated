from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        self.var_f=StringVar()
        self.var_l=StringVar()
        self.var_con=StringVar()
        self.var_email=StringVar()
        self.var_secureq=StringVar()
        self.var_securea=StringVar()
        self.var_pas=StringVar()
        self.var_conf=StringVar()


        self.bg=ImageTk.PhotoImage(file=r"C:/face monitoring system/images/blu.jpg") 
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"C:/face monitoring system/images/rop.jpg")
        l_lbl=Label(self.root,image=self.bg1,bg="white")
        l_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        regis=Label(frame,text="REGISTER HERE",font=("times nw roman",20,"bold"),fg="red",bg="white")
        regis.place(x=20,y=20)

        fname=Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_f,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="LAST Name:",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_l,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_con,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="EMAIL:",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_mail=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_mail.place(x=370,y=200,width=250)
        

        secure=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        secure.place(x=50,y=240)

        self.coomb=ttk.Combobox(frame,textvariable=self.var_secureq,font=("times new roman",15,"bold"),state="readonly")
        self.coomb["values"]=("Select","Your birth place","your girlfriend name","your pet name")
        self.coomb.place(x=50,y=270,width=250)
        self.coomb.current(0)


        security=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security.place(x=370,y=240)

        self.txt_secure=ttk.Entry(frame,textvariable=self.var_securea,font=("times new roman",15))
        self.txt_secure.place(x=370,y=270,width=250)

        psw=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        psw.place(x=50,y=310)

        self.txt_ps=ttk.Entry(frame,textvariable=self.var_pas,font=("times new roman",15))
        self.txt_ps.place(x=50,y=340,width=250)

        confirm=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm.place(x=370,y=310)

        self.txt_con=ttk.Entry(frame,textvariable=self.var_conf,font=("times new roman",15))
        self.txt_con.place(x=370,y=340,width=250)
        

        self.var_check=IntVar()
        checkb=Checkbutton(frame,variable=self.var_check,text="All details provided above are correct",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkb.place(x=50,y=380)
        
        img=Image.open(r"C:/face monitoring system/images/reg.jpg")
        img=img.resize((200,70),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"C:/face monitoring system/images/log.jpg")
        img1=img1.resize((200,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=350,y=420,width=300)

    def register_data(self):
        if self.var_f.get()=="" or self.var_email.get()=="" or self.var_secureq.get()=="Select":
            messagebox.showerror("Error","All fields are required!")
        elif self.var_pas.get()!=self.var_conf.get():
            messagebox.showerror("Error","Password and Confirm password must be same!")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please tick the above check box!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="krish@123",database="face_monitoring")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist! Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                       self.var_f.get(),
                                                                                       self.var_l.get(),
                                                                                       self.var_con.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_secureq.get(),
                                                                                       self.var_securea.get(),
                                                                                       self.var_pas.get()
                                                                                       
                                                                                        )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","You have registered successfully!")                                                                               





if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()        