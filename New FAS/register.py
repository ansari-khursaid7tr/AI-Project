from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Registration Panel | FRAS")
        self.root.geometry("710x430+0+0")
        self.root.resizable(False, False)

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_key=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        #self.bg=ImageTk.PhotoImage(file=r"E:\Final Project\New FAS\Images_GUI\bgReg.jpg")
        
        #lb1_bg=Label(self.root,image=self.bg)
        #lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#17202A")
        frame.place(x=0,y=0,width=900,height=580)
        

        # img1=Image.open(r"C:\Users\Muhammad Waseem\Documents\Python_Test_Projects\Images_GUI\reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        

       # get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="white",bg="#17202a")
        #get_str.place(x=340,y=10)

        #label1 
        fname =lb1= Label(frame,text="Name:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
        fname.place(x=50,y=40)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("Helvetica",12,))
        self.txtuser.place(x=50,y=70,width=270)


        #label2 
        uname =lb1= Label(frame,text="Username:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
        uname.place(x=50,y=115)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("Helvetica",12,))
        self.txtpwd.place(x=50,y=145,width=270)

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
        pwd.place(x=50,y=190)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd, show="*", font=("Helvetica",15,))
        self.txtuser.place(x=50,y=220,width=270)

        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
        cpwd.place(x=50,y=265)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,show="*",font=("Helvetica",15,))
        self.txtpwd.place(x=50,y=295,width=270)

        # ==================== section 2 -------- 2nd Column===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
        cnum.place(x=390,y=190)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("Helvetica",15,))
        self.txtuser.place(x=390,y=220,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("Helvetica",14,"bold"),fg="white",bg="#17202a")
        ssq.place(x=390,y=40)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("Helvetica",15,),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=390,y=70,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
        sa.place(x=390,y=115)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("Helvetica",15,))
        self.txtpwd.place(x=390,y=145,width=270)

        # ========================= Section 4-----Column 2=============================

        # Checkbutton
        #checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("Helvetica",13,"bold"),fg="white",bg="#17202a")
        #checkbtn.place(x=390,y=265,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("Helvetica",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B43",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=170,y=360,width=270,height=35)

        # Creating Button Login
        #loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        #loginbtn.place(x=533,y=510,width=270,height=35)




    def reg(self):
        if (self.var_fname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Password does not match!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from regteach where Username=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists,please try another Username")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_key.get(),
                    self.var_fname.get(),
                    self.var_email.get(),
                    self.var_cnum.get(),
                    #self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
                    self.root.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()