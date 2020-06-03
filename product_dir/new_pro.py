from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from product_dir import db_connection
# import mysql.connector
#from win32com.client import Dispatch


list1=["FROZEN_SWEETS","FALOODA","MILK_SHAKE","ICE_CREAM","SUNDAE","SANDWICH"]



class add_pro:
    def __init__(self,win):

        add_frame=Frame(win,bg="bisque2",bd=5,relief=GROOVE)
        add_frame.place(x=299, y=150, width=1236, height=650)

        canvas1=Canvas(add_frame,width=600,height=500,bg="black").place(x=270, y=40)


        #id=Label(self.add_frame,bg="snow", text="Product Id : ", font=("calibri Bold",15)).place(x=150, y=50)

        name = Label(add_frame,fg="white",bg="black", text="Product Name: ", font=("calibri Bold",15)).place(x=350, y=100)

        cat = Label(add_frame,fg="white",bg="black", text="Category : ", font=("calibri Bold",15)).place(x=350, y=170)

        qua = Label(add_frame,fg="white",bg="black", text="Quantity : ", font=("calibri Bold",15)).place(x=350, y=260)

        pri = Label(add_frame,fg="white",bg="black", text="Price : ", font=("calibri Bold",15)).place(x=350, y=330)

        decrp = Label(add_frame,fg="white",bg="black", text="Description : ", font=("calibri Bold",15)).place(x=350, y=400)

#text fields

        name= StringVar()
        ice_creame = StringVar()
        qua= IntVar()
        price= IntVar()
        decr= StringVar()


        nametf=Entry(add_frame,bg="snow",textvariable=name, font=("calibri Bold",15))
        nametf.place(x=550, y=100)


        combo = ttk.Combobox(add_frame,textvariable=ice_creame,width=18,height=40,font=("calibri Bold",15))
        combo['values']=list1
        combo.current(0)
        combo.place(x=550, y=170)

        quatf = Entry(add_frame, bg="snow",textvariable=qua, font=("calibri Bold", 15))
        quatf.place(x=550, y=260)


        pritf = Entry(add_frame, bg="snow",textvariable=price, font=("calibri Bold", 15))
        pritf.place(x=550, y=330)

        decrptf = Entry(add_frame, bg="snow",textvariable=decr, font=("calibri Bold", 15))
        decrptf.place(x=550, y=400)
#define a function for submit

        def submit():

            a=nametf.get()
            b=ice_creame.get()
            c=quatf.get()
            d=pritf.get()
            e=decrptf

            qua = int(c)
            price=int(d)

            if(a==""):
                messagebox.showerror("REQUIRED FIELD","NAME FIELD IS EMPTY")
                nametf.focus()

            elif (b== ""):
                messagebox.showerror("REQUIRED FIELD", "category FIELD IS EMPTY")
                combo.focus()

            elif (c== ""):
                messagebox.showerror("REQUIRED FIELD", "quantity FIELD IS EMPTY")
                quatf.focus()


            elif (qua<=1):
                messagebox.showerror("REQUIRED FIELD", "quantity cant be zero")
                quatf.focus()

            elif (d== ""):
                messagebox.showerror("REQUIRED FIELD", "price FIELD IS EMPTY")
                pritf.focus()

            elif (price<=1):
                messagebox.showerror("REQUIRED FIELD", "price cant be zero")
                pritf.focus()

            elif (e==""):
                messagebox.showerror("REQUIRED FIELD", "description FIELD IS EMPTY")
                decrptf


            else:
                a = nametf.get()
                b = ice_creame.get()
                c = quatf.get()
                d = pritf.get()
                e = decrptf.get()


                mk = db_connection.bd_conn(a,b,c,d,e,id)
                print(mk.id)
                my_id=str(mk.id)
                msg=mk.name+"'s ID IS :"+my_id
                speak = Dispatch(("SAPI.SpVoice"))
                speak.Speak("new product has been added")
                messagebox.showinfo("successful",msg)



                nametf.delete(0,END)
                #ice_creame.delete(0,END)
                quatf.delete(0,END)
                pritf.delete(0,END)
                decrptf.delete(0,END)



        def mk():
            print(nametf.get())


        b1=Button(add_frame,text="SUBMIT", command=submit,font=("calibri Bold", 13)).place(x=450, y=470)


        def mkmk():
            print(nametf.type())

        def reset():
            nametf.delete(0, END)
            # ice_creame.delete(0,END)
            quatf.delete(0, END)
            pritf.delete(0, END)
            decrptf.delete(0, END)

        b2=Button(add_frame,text="RESET", command=reset,font=("calibri Bold", 13)).place(x=550, y=470)



