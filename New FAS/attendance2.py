# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x600+0+0")
        self.root.title("Attendance Panel | FRAS")
        self.root.resizable(False, False)

        #-----------Variables-------------------
        self.var_course=StringVar()
        self.var_filter=StringVar()
        self.var_key=StringVar()
        self.var_sem=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # This part is image labels setting start 
        # backgorund image 
        bg1=Image.open(r"E:\Final Project\New FAS\Images_GUI\bg3.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        #title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        #title_lb1.place(x=0,y=0,width=1366,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=20,width=1355,height=569)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Enter Attendance Details ",font=("Helvetica",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=5,width=660,height=550)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(left_frame,text="Course :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        #studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("Helvetica",12))
        #studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        studentId_combo=ttk.Combobox(left_frame,textvariable=self.var_course,width=15,font=("Helvetica",12),state="readonly")
        studentId_combo["values"]=("Select Course","BE Computer","BE Civil","BCA","BBA")
        studentId_combo.current(0)
        studentId_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Semester Label
        sem_label=Label(left_frame,text="Semester",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        sem_label.grid(row=0,column=2,padx=5,sticky=W)

        #combo box 
        sem_combo=ttk.Combobox(left_frame,textvariable=self.var_sem,width=15,font=("Helvetica",12),state="readonly")
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll No:",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=15,font=("Helvetica",12))
        student_roll_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Name :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("Helvetica",12))
        student_name_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Department
        # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_frame,text="Time :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("Helvetica",12))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("Helvetica",12))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend Status:",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("Helvetica",12),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        filter_label = Label(left_frame, text="Filter Date:",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        filter_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        filter_entry = ttk.Entry(left_frame,textvariable=self.var_filter,width=15,font=("Helvetica",12))
        filter_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=140,width=635,height=310)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Semester", "Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="Course")
        self.attendanceReport_left.heading("Semester",text="Semester")
        self.attendanceReport_left.heading("Roll_No",text="Roll No")
        self.attendanceReport_left.heading("Name",text="Name")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend Status")
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("ID",width=100)
        self.attendanceReport_left.column("Semester",width=100)
        self.attendanceReport_left.column("Roll_No",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=460,width=635,height=60)

        #Improt button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Update",width=12,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Student Attendance Details ",font=("Helvetica",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=5,width=660,height=550)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=140,width=635,height=370)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Semester","Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Course")
        self.attendanceReport.heading("Semester",text="Semester")
        self.attendanceReport.heading("Roll_No",text="Roll No")
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend Status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Semester",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
        
        # =================================update for mysql button================
        #search_label = Label(right_frame,text="Search:",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        #search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        #self.var_searchTX=StringVar()
        #combo box 
        #search_combo=ttk.Combobox(right_frame,textvariable=self.var_searchTX,width=12,font=("Helvetica",12),state="readonly")
        #search_combo["values"]=("Select","Course")
        #search_combo.current(0)
        #search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        #self.var_search=StringVar()
        #search_entry = ttk.Entry(right_frame,textvariable=self.var_search,width=12,font=("Helvetica",12))
        #search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System ",font=("Helvetica",12,"bold"),fg="navyblue")
        #search_frame.place(x=10,y=5,width=635,height=80)
        search_frame.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #Phone Number
        search_label = Label(search_frame,text="Course & Sem:",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("Helvetica",12),state="readonly")
        search_combo["values"]=("Select Course","BE Computer", "BE Civil", "BCA", "BBA")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        self.var_search=StringVar()
        search_entry_combo = ttk.Combobox(search_frame,textvariable=self.var_search,width=12,font=("Helvetica",12), state="readonly")
        search_entry_combo["values"]=("Select Semester", "Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        search_entry_combo.current(0)
        search_entry_combo.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

    #Update button
        #del_btn=Button(right_frame,command=self.update_data,text="Update",width=12,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        #del_btn.grid(row=3,column=0,padx=6,pady=10,sticky=W)
    
    #Show All Button
        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)


    #Update button
        del_btn=Button(right_frame,command=self.delete_data,text="Delete Entry",width=12,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=3,column=0,padx=6,pady=10,sticky=W)
    
    
    def search_data(self):
        if self.var_search.get()=="Select Semester" or self.var_searchTX.get()=="Select Course":
            messagebox.showerror("Error","Select Combo Option and Enter Entry Box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT std_id,std_sem,std_roll_no, std_name, std_time,std_date, std_attendance FROM stdattendance where std_id= '" +str(self.var_searchTX.get()) + "' and std_sem= '"+ str(self.var_search.get()) +"'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.attendanceReport.delete(*self.attendanceReport.get_children())
                    for i in rows:
                        self.attendanceReport.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    
    
    
    # ===============================update function for mysql database=================
    def update_data(self):
        if self.var_course.get()=="" or self.var_sem.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_roll_no=%s",( 
                    self.var_course.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_roll.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student Roll No Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where key_id=%s"
                    val=(self.var_key.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from stdattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_course.set("")
        self.var_sem.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir="New FAS/",title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0]),
        self.var_sem.set(data[1])
        self.var_roll.set(data[2]),
        self.var_name.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attend.set(data[6]),
        self.var_key.set(data[7])

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0]),
        self.var_sem.set(data[1])
        self.var_roll.set(data[2]),
        self.var_name.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attend.set(data[6]),
        self.var_key.set(data[7])      
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_course.get()=="" or self.var_sem.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_course.get(),
                self.var_sem.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get(),
                self.var_key.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()