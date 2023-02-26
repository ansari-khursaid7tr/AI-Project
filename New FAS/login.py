from ctypes import alignment
from re import sub
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
import cv2
import numpy as np
# --------------------------
from train import Train
from student import Student
from subject import Sub
from man_atten import Subject
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from datetime import datetime
import mysql.connector


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Panel | FRAS ADMIN")
        self.root.geometry("380x420+610+170")
        self.root.resizable(False, False)

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"New FAS\Images_GUI\bg3.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=20,y=10,width=340,height=400)

        img1=Image.open(r"New FAS\Images_GUI\log1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=140,y=30, width=100,height=100)

        #get_str = Label(frame1,text="Welcome to Admin Panel",font=("Maven Pro",14,"bold"),fg="white",bg="#002B53")
        #get_str.place(x=80,y=20)

        #label1 
        username =lb1= Label(frame1,text="Username :",font=("Helvetica",13,"bold"),fg="white",bg="#002B53")
        username.place(x=20,y=140)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("Helvetica",11))
        self.txtuser.place(x=23,y=170,width=300)


        #label2 
        pwd =lb1= Label(frame1,text="Password :", font=("Helvetica",13,"bold"),fg="white",bg="#002B53")
        pwd.place(x=20,y=210)

        #entry2 
        self.txtpwd=ttk.Entry(frame1, show = "*", font=("Helvetica",11))
        self.txtpwd.place(x=23,y=240,width=300)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("Helvetica",13,"bold"),bd=0,relief=RIDGE,fg="#17202A",bg="#abb289",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=90,y=300,width=150,height=25)


        # Creating Button Registration
        #loginbtn=Button(frame1,command=self.reg,text="Register",font=("Helvetica",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        #loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forgot Password?",font=("Helvetica",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=10,y=350,width=150,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where Username=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                #self.new_window=Toplevel(self.root)
                #self.app=Face_Recognition_System(self.new_window)
                Face_Recognition_System(self.root)

            conn.commit()
            conn.close()

            
#=======================Reset Passowrd Function=============================
    
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where Username=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set Password=%s where Username=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                self.root2.destroy()
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Username to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where Username=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Username!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+610+170")
                self.root2.configure(bg="#17202a")
                self.root2.resizable(False, False)

                #l=Label(self.root2,text="Forget Password",font=("Helvetica",30,"bold"),fg="#002B53",bg="#fff")
                #l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("Helvetica",12,),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("Helvetica",12,))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("Helvetica",15,"bold"),fg="white",bg="#17202a")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,show="*",font=("Helvetica",12,))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("Helvetica",15,"bold"),bd=0,relief=RIDGE,fg="#17202a",bg="#abb289",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face detection system====================
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x768+0+0")
        self.root.geometry("830x520+300+200")
        self.root.title("Face Recogonition Attendance System")
        self.root.resizable(False, False)

        # backgorund image 
        bg1=Image.open(r"New FAS\Images_GUI\bg3.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        #title_lb1 = Label(bg_img,text="Attendance Managment System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        #title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # -------------------> Student Panel
        std_img_btn=Image.open(r"New FAS\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_panels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=20,y=30,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_panels,text="Student Panel",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=20,y=210,width=180,height=45)



        # -----------------------> Face Recognition
        det_img_btn=Image.open(r"New FAS\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_recog,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=420,y=30,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=420,y=210,width=180,height=45)



        # ------------------------> Attendance 
        att_img_btn=Image.open(r"New FAS\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=620,y=30,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=620,y=210,width=180,height=45)

         
        
        # -----------------------------> Train Data
        tra_img_btn=Image.open(r"New FAS\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_panels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=220,y=30,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_panels,text="Train Data",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=220,y=210,width=180,height=45)


        # -----------------------------------------> Manual Attendance Panel
        dev_img_btn=Image.open(r"New FAS\Images_GUI\exi.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.manual_atten,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=20,y=270,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.manual_atten,text="Manual Att. Panel",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=20,y=450,width=180,height=45)

        # ----------------------------------> Add Subject
        sub_img_btn=Image.open(r"New FAS\Images_GUI\ex.png")
        sub_img_btn=sub_img_btn.resize((180,180),Image.ANTIALIAS)
        self.sub_img1=ImageTk.PhotoImage(sub_img_btn)

        sub_b1 = Button(bg_img,command=self.Sub,image=self.sub_img1,cursor="hand2",)
        sub_b1.place(x=220,y=270,width=180,height=180)

        sub_b1_1 = Button(bg_img,command=self.Sub,text="Subject Panel",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        sub_b1_1.place(x=220,y=450,width=180,height=45)


        # ----------------------------------> HomePage
        exi_img_btn=Image.open(r"New FAS\Images_GUI\exit.png")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=420,y=270,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=420,y=450,width=180,height=45)

        #------------------------------------> Developers
        #dev_frame = Frame(bg_img, bd=2,) 
        #dev_frame.place(x=420,y=270,width=380,height=225)

        #about_label = Label(dev_frame, text="About : ",font=("Helvetica",15,"bold"),fg="#17202a")
        #about_label.place(x=5, y=5)

        #detail_label = Label(dev_frame, text="This is the project based on Artificial Intelligence\n focusing on different machine learning algorithms. \n\n The executive members of the projects are: \n\n 1. Chanda Rawal \n 2. Harimohan Khatri \n 3. Khursaid Ansari \n 4. Navin Saud ",justify= LEFT ,font=("Maven Pro",11,"bold"),fg="#17202a")
        #detail_label.place(x=5, y=35)
         

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("New FAS/data_img")


# ==================Functions Buttons=====================
    def student_panels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def Sub(self):
        self.new_window=Toplevel(self.root)
        self.app=Sub(self.new_window)
    
    def manual_atten(self):
        self.new_window=Toplevel(self.root)
        self.app=Subject(self.new_window)

    def train_panels(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Train(self.new_window)
        data_dir=("New FAS/data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("New FAS/clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)
    
    #def face_rec(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Face_Recognition(self.new_window)
    
    def mark_attendance(self,i,r,n,name,sid):
        with open("New FAS/attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            roll_list=[]
            now=datetime.now()
            d1=now.strftime("%Y/%m/%d")
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
                roll_list.append(entry[2])
                #print(name_list)
                #print(roll_list)

            if ((i not in name_list) and (name not in name_list) and (n not in name_list) and (r not in name_list)):
                #now=datetime.now()
                #d1=now.strftime("%Y/%m/%d")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{name}, {i}, {n}, {r}, {dtString}, {d1}, Present\n")
            #else:
             #   if (d1 not in name_list):
              #      dtString1=now.strftime("%H:%M:%S")
               #     f.writelines(f"{n}, {r}, {i}, {name}, {dtString1}, {d1}, Present\n")
                #    pass
                    

    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                #print(id)
                
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Course from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Semester from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                i=cursor.fetchone()
                i="+".join(i)

                cursor.execute("select Name from student where Student_ID="+str(id))
                name=cursor.fetchone()
                name="+".join(name)


                if confidence > 77:
                    cv2.putText(img,f"Course: {n}",(x,y-105),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(64,15,223),2)
                    cv2.putText(img,f"Sem: {r}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll No: {i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name: {name}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n,name,id)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Not Found",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(255,255,0),3)   

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("New FAS/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("New FAS/clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 27:
                break
        videoCap.release()
        cv2.destroyAllWindows()
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def Close(self):
        root.destroy()


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()