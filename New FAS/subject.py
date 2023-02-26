from ast import Sub
from tkinter import* 
import re
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Sub:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x550+50+100")
        self.root.title("Subject Panel | Face Recognition Attendance System")
        self.root.resizable(False, False)

        #-----------Variables-------------------
        #self.var_id=IntVar()
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_sub_id=StringVar()
        self.var_sub_name=StringVar()

    # This part is image labels setting start 
        # backgorund image 
        bg1=Image.open(r"E:\Final Project\New FAS\Images_GUI\bg3.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        #title_lb1 = Label(bg_img,text="Welcome to Student Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        #title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=20,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Enter Subject Details ",font=("Helvetica",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=20,width=660,height=480)

        # Current Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text=" Current Course ",font=("Helvetica",12,"bold"),fg="navyblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

        #label Department
        #dep_label=Label(current_course_frame,text="Department",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        #dep_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        #dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("Helvetica",12),state="readonly")
        #dep_combo["values"]=("Select Department","Science & Tech.", "Management")
        #dep_combo.current(0)
        #dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        # -----------------------------------------------------

        #label Course
        cou_label=Label(current_course_frame,text="Course*",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=0,padx=5,pady=15)

        #combo box 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("Helvetica",12),state="readonly")
        cou_combo["values"]=("Select Course","BE Computer","BE Civil","BCA","BBA")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        #-------------------------------------------------------------


        #-----------------------------------------------------------------

        #label Semester 
        year_label=Label(current_course_frame,text="Semester*",font=("Helvetica",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("Helvetica",12),state="readonly")
        year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text=" Subject Information ",font=("Helvetica",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=160,width=635,height=230)


        #Student name
        student_name_label = Label(class_Student_frame,text="Subject Name* :",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_sub_name,width=15,font=("Helvetica",12))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)


        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=2,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)


        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Show Subject Details ",font=("Helvetica",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=20,width=660,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text=" Search System ",font=("Helvetica",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("Helvetica",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("Helvetica",12),state="readonly")
        search_combo["values"]=("Select","Semester")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        #search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("Helvetica",12))
        search_entry=ttk.Combobox(search_frame,textvariable=self.var_search,width=12,font=("Helvetica",12),state="readonly")
        search_entry["values"] = ("Select Semester", "Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8" )
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("Helvetica",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("sub_id","Course","Semester","sub_name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("sub_id",text="Subject ID")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("sub_name",text="Subject Name")
        self.student_table["show"]="headings"


        # Set Width of Columns 
        self.student_table.column("sub_name",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("sub_id",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    def add_data(self):
        if self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_sub_name.get()=="" :
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into subject values(%s,%s,%s,%s)",(
                self.var_sub_id.get(),
                self.var_course.get(),
                self.var_semester.get(),
                self.var_sub_name.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from subject")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_sub_name.set(data[3]),
        self.var_course.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_sub_id.set(data[0]),
       
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_course.get=="Select Course" or self.var_semester.get()=="Select Semester" or self.var_sub_name.get()=="" :
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to Update this Subject Details!",parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                        mycursor = conn.cursor()
                        mycursor.execute("update subject set sub_name=%s,Course=%s,Semester=%s where sub_id=%s",( 
                        self.var_sub_name.get(),
                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_sub_id.get()   
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

    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_sub_id.get()=="":
            messagebox.showerror("Error","Subject ID is Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from subject where sub_id=%s"
                    val=(self.var_sub_id.get(),)
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

    # Reset Function 
    def reset_data(self):
        self.var_sub_name.set(""),
        self.var_course.set("Select Course"),
        self.var_semester.set("Select Semester"),


        
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT sub_id, Course, Semester, sub_name FROM subject where Semester='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Sub(root)
    root.mainloop()
