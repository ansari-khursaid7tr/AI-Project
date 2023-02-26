from tkinter import *
from FMD import *
from FAS import *
import tkinter as tk
import os
import PIL.Image

window = tk.Tk()
window.title("AI Based Object Detection & Intelligent Chatbot (ABODIC)")
window.geometry("900x550+300+200")
window.resizable(False,False)
#window.attributes("-fullscreen", True)

BG_BUTTON = "#ABB289"
BG_FRAME = "#17202A"
BG_IMAGE = "#ABB289"

def face_mask_train():
    os.system('python FMD/train_fmd.py')

def face_mask():
    #newWindow = Toplevel(window)
    #newWindow.title("Face Mask Detection")
    #newWindow.geometry('400x400')
    #newWindow.resizable(False, False)
    os.system('python FMD/fmd_main.py')

def smile_predictor_train():
    os.system('python SP/train_model.py -d SP/SMILEs -m SP/model.h5')

def smile_predictor():
    #newWindow = Toplevel(window)
    #newWindow.title("Smile Predictor")
    os.system('python SP/sp_main.py -c SP/haarcascade_frontalface_default.xml -m SP/model.h5')

def color_predictor():
    #newWindow = Toplevel(window)
    #newWindow.title("Color Predictor")
    os.system('python CP/cp_main.py')

def gender_predictor_train():
    os.system('python GP/train.py')

def gender_predictor():
    #newWindow = Toplevel(window)
    #newWindow.title("Gender Predictor")
    os.system('python GP/gp_main.py')

def face_recognition():
    os.system('python "New FAS"/login.py')  

def chatbot():
    #newWindow = Toplevel(window)
    #newWindow.title("ChatBot")
    os.system('python ChatBot/cb_main.py')

#For Frames
Body = Frame(window, width=1000, height=1000, bg="#ABB289")
Body.pack(pady = 10, padx = 10)

#----Frame1
Frame1 = Frame(Body, width=280, height= 250, bg=BG_FRAME, highlightbackground="#adacb1", highlightthickness=1)
Frame1.place(x=10, y=10)

#---Frame1 Content
photo1 = PhotoImage(file="assets/image/fmd.png")
myimage1 = Label(Frame1, image=photo1, height=120, width= 120, background="#17202A", justify="center")
myimage1.place(x=70, y=20)

button11=Button(window, text="Train", padx=2, cursor='hand2', pady=2, font="Helvetica", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command= face_mask_train)
button11.place(x=30, y=190)

button1=Button(window, text="Face Mask Detection", cursor='hand2',padx=2, pady=2, font="Helvetica", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command= face_mask)
button1.place(x=90, y=190)

#----Frame2
Frame2 = Frame(Body, width=280, height= 250, bg=BG_FRAME, highlightbackground="#adacb1", highlightthickness=1)
Frame2.place(x=298, y=10)

#---Frame2 Content
photo2 = PhotoImage(file="assets/image/sp.png")
myimage2 = Label(Frame2, image=photo2, width=120, height=120, background="#17202A", justify="center")
myimage2.place(x=70, y=20)

button21=Button(window, text="Train", padx=3, cursor='hand2',pady=3, font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command=smile_predictor_train)
button21.place(x=345, y=190)

button2=Button(window, text="Smile Predictor", padx=3,cursor='hand2', pady=3, font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command=smile_predictor)
button2.place(x=415, y=190)

#----Frame3
Frame3 = Frame(Body, width=280, height= 250, bg=BG_FRAME, highlightbackground="#adacb1", highlightthickness=1)
Frame3.place(x=586, y=10)

#---Frame3 Content
photo3 = PhotoImage(file="assets/image/cp.png")
myimage3 = Label(Frame3, image=photo3, width=120, height=120, background="#17202A", justify="center")
myimage3.place(x=70, y=20)

button3=Button(window, text="Color Predictor", padx=3,cursor='hand2', pady=3, font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command= color_predictor)
button3.place(x=665, y=190)

#----Frame4
Frame4 = Frame(Body, width=280, height= 250, bg=BG_FRAME, highlightbackground="#adacb1", highlightthickness=1)
Frame4.place(x=10, y=275)

#---Frame4 Content
photo4 = PhotoImage(file="assets/image/gp.png")
myimage4 = Label(Frame4, image=photo4, width=120, height=120, background="#17202A")
myimage4.place(x=70, y=30)

button41=Button(window, text="Train", padx=3, pady=3,cursor='hand2', font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command= gender_predictor_train)
button41.place(x=45, y=460)

button4=Button(window, text="Gender Predictor", padx=3,cursor='hand2', pady=3, font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command= gender_predictor)
button4.place(x=115, y=460)

#----Frame5
Frame5 = Frame(Body, width=280, height= 250, bg=BG_FRAME, highlightbackground="#adacb1", highlightthickness=1)
Frame5.place(x=298, y=275)

#---Frame5 Content
photo5 = PhotoImage(file="assets/image/fd.png")
myimage5 = Label(Frame5, image=photo5, width=120, height=120, background="#17202A", justify="center")
myimage5.place(x=70, y=30)

button5=Button(window, text="Face Recognition", padx=3,cursor='hand2', pady=3, font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command=face_recognition)
button5.place(x=370, y=460)

#----Frame6
Frame6 = Frame(Body, width=280, height= 250, bg=BG_FRAME, highlightbackground="#adacb1", highlightthickness=1)
Frame6.place(x=586, y=275)

#---Frame6 Content
photo6 = PhotoImage(file="assets/image/cb.png")
myimage6 = Label(Frame6, image=photo6, width=120, height=120, background="#17202A", justify="center")
myimage6.place(x=70, y=30)

button6=Button(window, text="ChatBot", padx=3, pady=3,cursor='hand2', font="Poppins", background=BG_BUTTON, highlightthickness=0, borderwidth=1, relief="solid", command= chatbot)
button6.place(x=680, y=460)

window.mainloop()
