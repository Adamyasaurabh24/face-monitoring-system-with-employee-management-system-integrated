from atexit import register
from email import message
from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import face_monitoring_system

def main():
    win=Tk()
    app=loginsystem(win)
    win.mainloop()
 

class loginsystem:
    def __init__(self,root):
          self.root=root
          self.root.title("LOGIN")
          self.root.geometry("1550x800+0+0")

         

          self.bg=ImageTk.PhotoImage(file=r"C:/face monitoring system/images/back.jpg")
          labelbg=Label(self.root,image=self.bg)
          labelbg.place(x=0,y=0,relwidth=1,relheight=1)

          title_lbl=Label(labelbg,text="FACIAL MONITORING SYSTEM",font=("times new roman",30,"bold"),fg="black",bg="lightblue")
          title_lbl.place(x=0,y=0,width=1550,height=100)
         

          frame=Frame(self.root,bg="black")
          frame.place(x=610,y=170,width=340,height=450)

          img=Image.open(r"C:/face monitoring system/images/jo.png")
          img=img.resize((240,130),Image.ANTIALIAS)
          self.photoimage=ImageTk.PhotoImage(img)
          lbl=Label(image=self.photoimage,bg="black",borderwidth=0)
          lbl.place(x=660,y=175,width=240,height=130)
          
          adm=Label(frame,text="Admin login",font=("times new roman",20,"bold"),fg="white",bg="black")
          adm.place(x=95,y=130)

          user=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
          user.place(x=40,y=170)

          self.user1=ttk.Entry(frame,font=("times new roman",15,"bold"))
          self.user1.place(x=40,y=200,width=270)

          passw=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
          passw.place(x=40,y=240)

          self.pass1=ttk.Entry(frame,font=("times new roman",15,"bold"))
          self.pass1.place(x=40,y=270,width=270)

          img1=Image.open(r"C:/face monitoring system/images/ko.webp")
          img1=img1.resize((23,21),Image.ANTIALIAS)
          self.photoimage1=ImageTk.PhotoImage(img1)
          lbl=Label(image=self.photoimage1,bg="black",borderwidth=0)
          lbl.place(x=620,y=345,width=23,height=21)

          img2=Image.open(r"C:/face monitoring system/images/lop.png")
          img2=img2.resize((26,24),Image.ANTIALIAS)
          self.photoimage2=ImageTk.PhotoImage(img2)
          lbl=Label(image=self.photoimage2,bg="black",borderwidth=0)
          lbl.place(x=620,y=415,width=26,height=24)
          
          log=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=2,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
          log.place(x=115,y=320,width=100,height=40)

          register=Button(frame,text=" New User Register",command=self.register_win,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
          register.place(x=18,y=380,width=120)
          
          forg=Button(frame,text="Forgot Password ",command=self.forgotpass,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
          forg.place(x=15,y=400,width=120)
    
    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.user1.get()=="" or self.pass1.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.user1.get()=="krishna" and self.pass1.get()=="krish":
            messagebox.showinfo("Success","Welcome to Face Monitoring System")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="krish@123",database="face_monitoring")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                     self.user1.get(),
                                                                                     self.pass1.get()
                                                                                       ))

            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("Yes/No","Only admins allowed,Access now!")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=face_monitoring_system(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close() 
    
    def resetpass(self):
        if self.coomb.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_secure.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)    
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="krish@123",database="face_monitoring")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityq=%s and securitya=%s")
            value=(self.user1.get(),self.coomb.get(),self.txt_secure.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer!",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.user1.get())
                my_cursor.execute(query,value)  
                conn.commit()
                conn.close()
                messagebox.showinfo("Important","Your password has been reset! Please login with new password",parent=self.root2)
                self.root2.destroy()



    def forgotpass(self):
        if self.user1.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="krish@123",database="face_monitoring")
            my_cursor=conn.cursor() 
            query=("select * from register where email=%s")
            value=(self.user1.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row) 
            if row==None:
                messagebox.showerror("Error","Please enter valid email!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="darkblue",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                secure=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                secure.place(x=50,y=80)

                self.coomb=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.coomb["values"]=("Select","Your birth place","your girlfriend name","your pet name")
                self.coomb.place(x=50,y=110,width=250)
                self.coomb.current(0)


                security=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security.place(x=50,y=150)

                self.txt_secure=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_secure.place(x=50,y=180,width=250)

                newpass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                newpass.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.resetpass,font=("times new roman",15,"bold"),fg="red",bg="green")
                btn.place(x=130,y=290)

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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=350,y=420,width=300)

    def register_data(self):
        if self.var_f.get()=="" or self.var_email.get()=="" or self.var_secureq.get()=="Select":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        elif self.var_pas.get()!=self.var_conf.get():
            messagebox.showerror("Error","Password and Confirm password must be same!",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please tick the above check box!",parent=self.root)
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
    def return_login(self):
         self.root.destroy()


if __name__=="__main__":
     main()       