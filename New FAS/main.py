from operator import is_not
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
import cv2
import numpy as np
import mysql.connector
from datetime import *

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x768+0+0")
        self.root.geometry("830x520+300+200")
        self.root.title("Face Recogonition Attendance System")
        self.root.resizable(False, False)

# This part is image labels setting start 
        # first header image  
        #img=Image.open(r"E:\Final Project\New FAS\Images_GUI\banner.jpg")
        #img=img.resize((1366,130),Image.ANTIALIAS)
        #self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        #f_lb1 = Label(self.root,image=self.photoimg)
        #f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"E:\Final Project\New FAS\Images_GUI\bg3.png")
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
        std_img_btn=Image.open(r"E:\Final Project\New FAS\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_panels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=20,y=30,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_panels,text="Student Panel",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=20,y=210,width=180,height=45)



        # -----------------------> Face Recognition
        det_img_btn=Image.open(r"E:\Final Project\New FAS\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_recog,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=420,y=30,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=420,y=210,width=180,height=45)



        # ------------------------> Attendance 
        att_img_btn=Image.open(r"E:\Final Project\New FAS\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=620,y=30,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=620,y=210,width=180,height=45)

         
        
        # -----------------------------> Train Data
        tra_img_btn=Image.open(r"E:\Final Project\New FAS\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_panels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=220,y=30,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_panels,text="Train Data",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=220,y=210,width=180,height=45)


        # -----------------------------------------> Developers
        dev_img_btn=Image.open(r"E:\Final Project\New FAS\Images_GUI\dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=20,y=270,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=20,y=450,width=180,height=45)

        # exit   button 8
        #exi_img_btn=Image.open(r"E:\Final Project\New FAS\Images_GUI\exi.jpg")
        #exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        #self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        #exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        #exi_b1.place(x=250,y=330,width=180,height=180)

        #exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("Helvetica",15,"bold"),bg="white",fg="navyblue")
        #exi_b1_1.place(x=250,y=510,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")


# ==================Functions Buttons=====================
    def student_panels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_panels(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Train(self.new_window)
        data_dir=("data_img")
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
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!",parent=self.root)
    
    #def face_rec(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Face_Recognition(self.new_window)
    def mark_attendance(self,i,r,n,name,sid):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            date_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            #if((sid not in name_list) and (name not in name_list) and (i not in name_list)):
            #    now=datetime.now()
            #    d1=now.strftime("%Y/%m/%d")
            #    dtString=now.strftime("%H:%M:%S")
             #   f.writelines(f"{n}, {r}, {i}, {name}, {dtString}, {d1}, Present\n")

            if ((i not in name_list) and (name not in name_list) and (sid not in name_list) and (r not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%Y/%m/%d")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{n}, {r}, {i}, {name}, {dtString}, {d1}, Present\n")

            #else:
            #    now1=datetime.now()
             #   d2=now1.strftime("%Y/%m/%d")
             #   dtString1=now1.strftime("%H:%M:%S")
             #   if((d2 not in date_list) and (i in name_list) and (name in name_list) and (r in name_list) and (sid in name_list) and (n in name_list)):
             #       f.writelines(f"{n}, {r}, {i}, {name}, {dtString1}, {d2}, Present\n")

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

                #cursor.execute("select Student_ID from student where Student_ID="+str(id))
                #sid=cursor.fetchone()
                #sid="+".join(str(sid))


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
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

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
    obj=Face_Recognition_System(root)
    root.mainloop()
