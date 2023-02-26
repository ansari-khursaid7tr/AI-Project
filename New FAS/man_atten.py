import csv
from datetime import datetime
from optparse import Values
import os
from tkinter import* 
import re
from tkinter import ttk
from tkinter import filedialog
from unicodedata import name
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

my_data = []
class Subject:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x550+50+100")
        self.root.title("Manual Attendance Panel | Face Recognition Attendance System")
        self.root.resizable(False, False)

        #-----------Variables-------------------
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_subject=StringVar()
        self.var_std_name=StringVar()
        self.var_attend=StringVar()
        self.var_roll=StringVar()
        self.var_date = StringVar()

    # This part is image labels setting start 
        # backgorund image 
        bg1=Image.open(r"New FAS\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=20,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Enter Class Details ",font=("Helvetica",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=20,width=660,height=480)

        # Current Course 
        global current_course_frame
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text=" Current Course ",font=("Helvetica",12,"bold"),fg="navyblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

        #label Course
        cou_label=Label(current_course_frame,text="Course*",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("Helvetica",12),state="readonly")
        cou_combo["values"]=("Select Course","BE Computer","BE Civil","BCA","BBA")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        #-----------------------------------------------------------------

        #label Semester 
        year_label=Label(current_course_frame,text="Semester*",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=0,column=2,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("Helvetica",12),state="readonly")
        year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        #Fetch Button
        fetch_btn=Button(current_course_frame,command=self.fetch_sub,text="Fetch Details",width=12,font=("Helvetica",10,"bold"),fg="white",bg="navyblue")
        fetch_btn.grid(row=0,column=4,padx=5,pady=5,sticky=W)

        #Class Student Information
        global class_Student_frame
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text=" Class Student Information ",font=("Helvetica",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=160,width=635,height=230)

        #subject button
        subject_label=Label(current_course_frame,text="Subject*",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        subject_label.grid(row=1,column=0,padx=5,sticky=W)          

        #combo box 
        #subject_combo=ttk.Combobox(current_course_frame, textvariable=self.var_subject,width=15,font=("Helvetica",12),state="readonly")
        #subject_combo["values"]=(mydata)
        #subject_combo.current([0])
        #subject_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Name* :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        #student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("Helvetica",12))
        #student_name_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Class Didvision
        student_div_label = Label(class_Student_frame,text="Attend Status* :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_attend,width=13,font=("Helvetica",12),state="readonly")
        div_combo["values"]=("Present","Absent", "Leave")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date Thing
        date_label = Label(class_Student_frame,text="Date * :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(class_Student_frame,textvariable=self.var_date,width=15,font=("Helvetica",12), state="readonly")
        date_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll No* :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("Helvetica",12), state="readonly")
        student_roll_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #update button
        #update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        #update_btn.grid(row=0,column=2,padx=5,pady=8,sticky=W)

        #delete button
        #del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        #del_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.exportCsv,text="Export Csv",width=9,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)

        showAll_btn=Button(btn_frame,command=self.fetch_data,text="Refresh",width=10,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=6,padx=5,pady=10,sticky=W)

        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Attendance Details ",font=("Helvetica",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=20,width=660,height=480)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=10,width=635,height=440)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("Course","Semester","Subject","Roll No","Name","Attend Status", "Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Subject",text="Subject")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Attend Status",text="Attend Status")
        self.student_table.heading("Date", text="Date")
        self.student_table["show"]="headings"


        # Set Width of Columns 
        self.student_table.column("Course",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Subject",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Attend Status",width=100)
        self.student_table.column("Date", width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    def add_data(self):
        if self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_subject.get()=="" or self.var_std_name.get()=="" or self.var_attend.get()=="" :
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
            try:
                name = self.var_std_name.get()
                sub = self.var_subject.get()
                sem = self.var_semester.get()
                
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor2 = conn.cursor()
                mycursor2.execute("select Roll_No from student where Course ='" +str(self.var_course.get())+"' and Semester='" +str(self.var_semester.get())+"' and Name= '" +str(self.var_std_name.get())+"'")
                data2 = mycursor2.fetchall()
                mydata2 = [row2[0] for row2 in data2]
                #print(mydata2[0])

                roll = mydata2[0]
                with open("New FAS/man_atten.csv","r+",newline="\n") as f:
                    myDatalist=f.readlines()
                    now = datetime.now()
                    d1=now.strftime("%Y/%m/%d")
                    name_list=[]
                    roll_list=[]
                    sub_list=[]
                    sem_list=[]
                    for line in myDatalist:
                        entry=line.split((","))
                        name_list.append(entry[4])
                        roll_list.append(entry[3])
                        sub_list.append(entry[2])
                        sem_list.append(entry[1])
                    
                    #print(sub_list)

                    if((sub not in sub_list) and (roll in roll_list) or (roll not in roll_list)):
                        f.writelines(f"{self.var_course.get()},{sem},{sub},{roll},{name},{self.var_attend.get()}, {d1}\n")
                        messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                    
                    else:
                        messagebox.showerror("Error", "Data Already Exists!", parent=self.root)

                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        with open("New FAS/man_atten.csv","r+",newline="\n") as f:
            data=csv.reader(f,delimiter=",")
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0]),
        self.var_semester.set(data[1]),
        self.var_subject.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_std_name.set(data[4]),      
        self.var_attend.set(data[5]),
        self.var_date.set(data[6]),

    # ========================================Update Function==========================
    def update_data(self):
        if self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_subject.get()=="" or self.var_std_name.get()=="" or self.var_attend.get()=="" or self.var_roll.get()=="" :
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                roll = self.var_roll.get()
                if Update > 0:
                    with open("New FAS/man_atten.csv","r+",newline="\n") as f:
                        data=csv.reader(f,delimiter=",")
                        if roll in data:
                            pass
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_roll.get()=="" and self.var_subject.get() == "" and self.var_std_name.get()=="":
            messagebox.showerror("Error","Empty Fields Detected!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    with open("man_atten.csv","r+",newline="\n") as f:
                        myDatalist=f.readlines()
                        name_list=[]
                        roll_list=[]
                        sub_list=[]
                        sem_list=[]

                        #print(myDatalist)

                        for line in myDatalist:
                            entry=line.split((","))
                            name_list.append(entry[4])
                            roll_list.append(entry[3])
                            sub_list.append(entry[2])
                            sem_list.append(entry[1])
                            print(name_list)
                            print(line)

                            if (str(self.var_std_name.get()) in name_list and str(self.var_roll.get()) in roll_list and str(self.var_subject.get()) in sub_list):
                                line.remove()
                else:
                    if not delete:
                        return

                
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_name.set(""),
        self.var_subject.set(""),
        self.var_course.set("Select Course"),
        self.var_semester.set("Select Semester"),
        self.var_attend.set("Present"),
        self.var_roll.set(""),
        self.var_date.set(""),
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                with open("man_atten.csv","r+",newline="\n") as f:
                    name = self.var_std_name.get()
                    data=csv.reader(f,delimiter=",")
                    name_list=[]
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        if name in name_list:
                            self.student_table.insert("",END,values=i)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def fetch_sub(self):
        global mydata
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()
        mycursor.execute("select sub_name from subject where Course ='" +str(self.var_course.get())+"' and Semester='" +str(self.var_semester.get())+"'")
        data = mycursor.fetchall()
        #data = [r for r, in my_data]
        mydata = [row[0] for row in data]
        #print(mydata)     

        #combo box for subject
        subject_combo=ttk.Combobox(current_course_frame,textvariable=self.var_subject,width=15,font=("Helvetica",12),state="readonly")
        subject_combo["values"]=(mydata)
        #subject_combo.current([0])
        #subject_combo.place(x=130,y=150)
        subject_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        mycursor1 = conn.cursor()
        mycursor1.execute("select Name from student where Course ='" +str(self.var_course.get())+"' and Semester='" +str(self.var_semester.get())+"'")
        data1 = mycursor1.fetchall()
        mydata1 = [row1[0] for row1 in data1]
        #print(mydata1)

        #combo box for name
        name_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_std_name,width=15,font=("Helvetica",12),state="readonly")
        name_combo["values"]=(mydata1)
        #subject_combo.current([0])
        #name_combo.place(x=160,y=255)
        name_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        conn.commit()
        conn.close()   

    def exportCsv(self):
        try:
            with open("New FAS/man_atten.csv","r+",newline="\n") as f:
                data=csv.reader(f,delimiter=",")
                #data=f.readlines()
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in data:
                        exp_write.writerow(i)
                    messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Subject(root)
    root.mainloop()
