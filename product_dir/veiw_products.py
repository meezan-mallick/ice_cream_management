from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from product_dir import db_connection
import mysql.connector
from tkinter.ttk import Combobox
from tkscrolledframe import ScrolledFrame
#from win32com.client import Dispatch




class view_pro:


    def __init__(self,win):



        sf = ScrolledFrame(win,width=1210,height=620)
        sf.place(x=300,y=152)
        #sf.pack(side="top",expand=1,fill="both")

        sf.bind_arrow_keys(win)
        sf.bind_scroll_wheel(win)

        canvas = sf.display_widget(Canvas)
        canvas.config(bg="bisque2",width=1210,height=1000)



        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")
        list5 = []
        cursor = mydb.cursor()
        cursor.execute("select pro_id from products")
        list6 = cursor.fetchall()

        cursor.execute("select pro_name from products")
        list1 = cursor.fetchall()
        # print(tabulate(list))

        cursor.execute("select pro_cat from products")
        list2 = cursor.fetchall()

        cursor.execute("select pro_quant from products")
        list3 = cursor.fetchall()

        cursor.execute("select pro_price from products")
        list4 = cursor.fetchall()

        cursor.execute("select decp from products")
        list5 = cursor.fetchall()




        title1 = Label(canvas, bg="bisque2", text="ID", font=("calibri Bold", 15)).place(x=70, y=90)

        title2 = Label(canvas, bg="bisque2", text="Product Name", font=("calibri Bold", 15)).place(x=190, y=90)

        title3 = Label(canvas, bg="bisque2", text="Category", font=("calibri Bold", 15)).place(x=450, y=90)

        title4 = Label(canvas, bg="bisque2", text="Quantity", font=("calibri Bold", 15)).place(x=600, y=90)

        title5 = Label(canvas, bg="bisque2", text="Price", font=("calibri Bold", 15)).place(x=720, y=90)

        title6 = Label(canvas, bg="bisque2", text="Description", font=("calibri Bold", 15)).place(x=900, y=90)

        ym1 = 90
        for m in range(0, list6.__len__()):
            label = Label(canvas, bg="bisque2", text=list6[m], font=("calibri regular", 15))
            ym1 = ym1 + 40
            label.place(x=70, y=ym1)

        l1 = list(list1)
        ind = 0

        ym2 = 0
        y1 = 100
        y2 = 90
        for m in range(0, list1.__len__()):

            a = str(l1[ind])

            c = a.replace("('", "")
            d = c.replace("',)", "")


            label = Label(canvas, bg="bisque2", text=d, font=("calibri regular", 15))
            y2 = y2 + 40
            ind=ind+1
            label.place(x=140, y=y2)
            y1 = y2 + 35
            ym2 = y1
            canvas.create_line(40, y1, 1200, y1, fill='black')

        y2 = 90

        for i in range(0, list2.__len__()):
            label = Label(canvas, bg="bisque2", text=list2[i], font=("calibri regular", 13))
            y2 = y2 + 40
            label.place(x=410, y=y2)

        canvas.create_line(40, 80, 1200, 80, fill='black')

        canvas.create_line(40, 120, 1200, 120, fill='black')

        canvas.create_line(40, 80, 40, ym2, fill='black')
        canvas.create_line(130, 80, 130, ym2, fill='black')
        canvas.create_line(390, 80, 390, ym2, fill='black')
        canvas.create_line(590, 80, 590, ym2, fill='black')
        canvas.create_line(700, 80, 700, ym2, fill='black')
        canvas.create_line(800, 80, 800, ym2, fill='black')
        canvas.create_line(1200, 80, 1200, ym2, fill='black')

        a = ""
        temp1 = 0
        temp2 = 0
        for i in range(0, list2.__len__()):
            a = list1[i]

            n = a.__len__()
            temp1 = n
            if (temp1 > temp2):
                print(list1[i])
            temp2 = temp1

        y2 = 90
        for i in range(0, list3.__len__()):
            label = Label(canvas, bg="bisque2", text=list3[i], font=("calibri regular", 15))
            y2 = y2 + 40
            label.place(x=620, y=y2)

        y2 = 90
        for i in range(0, list4.__len__()):
            label = Label(canvas, bg="bisque2", text=list4[i], font=("calibri regular", 15))
            y2 = y2 + 40
            label.place(x=730, y=y2)

        l5 = list(list5)
        ind = 0

        y2 = 90
        for i in range(0, l5.__len__()):
            a = str(l5[ind])

            c = a.replace("('", "")
            d = c.replace("',)", "")

            label = Label(canvas, bg="bisque2", text=d, font=("calibri regular", 15))
            y2 = y2 + 40
            ind = ind + 1
            label.place(x=810, y=y2)
















list1=["FROZEN_SWEETS","FALOODA","MILK_SHAKE","ICE_CREAM","SUNDAE","SANDWICH"]



class update_product:
    def __init__(self, win):
        add_frame = Frame(win, bg="bisque2", bd=5, relief=GROOVE)
        add_frame.place(x=299, y=150, width=1236, height=650)

        canvas1 = Canvas(add_frame, width=1100, height=550, bg="black").place(x=50, y=30)

        # id=Label(self.add_frame,bg="snow", text="Product Id : ", font=("calibri Bold",15)).place(x=150, y=50)

        name = Label(add_frame, fg="white", bg="black", text="Product Name: ", font=("calibri Bold", 15)).place(x=250,y=150)

        cat = Label(add_frame, fg="white", bg="black", text="Category : ", font=("calibri Bold", 15)).place(x=250,y=220)

        qua = Label(add_frame, fg="white", bg="black", text="Quantity : ", font=("calibri Bold", 15)).place(x=250,y=290)

        pri = Label(add_frame, fg="white", bg="black", text="Price : ", font=("calibri Bold", 15)).place(x=250, y=360)

        decrp = Label(add_frame, fg="white", bg="black", text="Description : ", font=("calibri Bold", 15)).place(x=250,y=410)

        pro_id= Label(add_frame, fg="white", bg="black", text="SELECT PRODUCT : ", font=("calibri Bold", 15)).place(x=100, y=50)

        # text fields

        name = StringVar()
        ice_creame = StringVar()
        qua = IntVar()
        price = IntVar()
        decr = StringVar()

       # pro_idtf = Entry(add_frame, bg="snow", textvariable=name, font=("calibri Bold", 15))
        #pro_idtf.place(x=300, y=50)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")

        cursor = mydb.cursor()
        cursor.execute("select pro_name from products")
        pro_list = cursor.fetchall()


        id_combo = Combobox(add_frame)
        id_combo['values'] = pro_list
        id_combo.place(x=300, y=50)

        nametf = Entry(add_frame, bg="snow", textvariable=name, font=("calibri Bold", 15))
        nametf.place(x=450, y=150)

        combo = ttk.Combobox(add_frame, textvariable=ice_creame, width=18, height=40, font=("calibri Bold", 15))
        combo['values'] = list1
        combo.place(x=450, y=220)

        quatf = Entry(add_frame, bg="snow", textvariable=qua, font=("calibri Bold", 15))
        quatf.place(x=450, y=290)

        pritf = Entry(add_frame, bg="snow", textvariable=price, font=("calibri Bold", 15))
        pritf.place(x=450, y=360)

        decrptf = Entry(add_frame, bg="snow", textvariable=decr, font=("calibri Bold", 15))
        decrptf.place(x=450, y=410)





        def search():
            id=id_combo.get()
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")
            cursor = mydb.cursor()
            cursor.execute("select * from products where pro_name= '"+id+"' ")
            final_list = cursor.fetchall()
            print()


            a=final_list[0][2]
            b=0

            if(a=="FROZEN_SWEETS"):
                b=0

            elif(a=="FALOODA"):
                b=1

            elif (a == "MILK_SHAKE"):
                b = 2

            elif (a == "ICE_CREAM"):
                b = 3

            elif (a == "SUNDAE"):
                b = 4

            elif (a == "ICE_CREAME_SANDWICH"):
                b = 5



            nametf.insert(END,final_list[0][1])
            combo.current(b)
            quatf.delete(0,END)
            quatf.insert(END,final_list[0][3])
            pritf.delete(0),END
            pritf.insert(END,final_list[0][4])
            decrptf.insert(END,final_list[0][5])


        search = Button(add_frame, text="SEARCH", command=search, font=("calibri Bold", 13)).place(x=600, y=50)

        # define a function for submit






        def submit():

            a = nametf.get()
            b = ice_creame.get()
            c = quatf.get()
            d = pritf.get()
            e = decrptf

            qua = int(c)
            price = int(d)

            if (a == ""):
                messagebox.showerror("REQUIRED FIELD", "NAME FIELD IS EMPTY")
                nametf.focus()

            elif (b == ""):
                messagebox.showerror("REQUIRED FIELD", "category FIELD IS EMPTY")
                combo.focus()

            elif (c == ""):
                messagebox.showerror("REQUIRED FIELD", "quantity FIELD IS EMPTY")
                quatf.focus()


            elif (qua <= 1):
                messagebox.showerror("REQUIRED FIELD", "quantity cant be zero")
                quatf.focus()

            elif (d == ""):
                messagebox.showerror("REQUIRED FIELD", "price FIELD IS EMPTY")
                pritf.focus()

            elif (price <= 1):
                messagebox.showerror("REQUIRED FIELD", "price cant be zero")
                pritf.focus()

            elif (e == ""):
                messagebox.showerror("REQUIRED FIELD", "description FIELD IS EMPTY")
                decrptf


            else:
                a = nametf.get()
                b = ice_creame.get()
                c = quatf.get()
                d = pritf.get()
                e = decrptf.get()

                mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")

                cursor = mydb.cursor()

                sql = "update products set pro_name= '"+a+"',pro_cat= '"+b+"',pro_quant= '"+c+"',pro_price= '"+d+"',decp= '"+e+"' where pro_name='" + id_combo.get() + "'"
                cursor.execute(sql)
                mydb.commit()
                speak = Dispatch(("SAPI.SpVoice"))
                speak.Speak("updated successfully")
                messagebox.showinfo("REQUIRED FIELD", "UPDATED")

                nametf.delete(0, END)
                # ice_creame.delete(0,END)
                quatf.delete(0, END)
                pritf.delete(0, END)
                decrptf.delete(0, END)


        def mk():
            print(nametf.get())

        b1 = Button(add_frame, text="UPDATE", command=submit, font=("calibri Bold", 13)).place(x=450, y=470)

        def mkmk():
            print(nametf.type())


        def reset():
            nametf.delete(0, END)
            # ice_creame.delete(0,END)
            quatf.delete(0, END)
            pritf.delete(0, END)
            decrptf.delete(0, END)


        b2 = Button(add_frame, text="RESET", command=reset, font=("calibri Bold", 13)).place(x=550, y=470)











class delete:
    def __init__(self, win):
        del_frame = Frame(win, bg="bisque2", bd=5, relief=GROOVE)
        del_frame.place(x=299, y=150, width=1236, height=650)

        canvas1 = Canvas(del_frame, width=600, height=550, bg="black").place(x=300, y=30)

        pro_id = Label(del_frame, fg="white", bg="black", text="SELECT PROCUCT : ", font=("calibri Bold", 15)).place(
            x=400, y=50)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")

        cursor = mydb.cursor()
        cursor.execute("select pro_name from products")
        pro_list = cursor.fetchall()

        id_combo = Combobox(del_frame)
        id_combo['values'] = pro_list
        id_combo.place(x=600, y=50)





        def search():


            id = id_combo.get()


            if(id==""):
                messagebox.showerror("REQUIRED FIELD", "ID FIELD IS EMPTY")

            else:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018",
                                               database="ice_creame")
                cursor = mydb.cursor()
                cursor.execute("select * from products where pro_name= '" + id + "' ")
                final_list = cursor.fetchall()
                print()

                name = Label(del_frame, fg="white", bg="black", text=final_list[0][1], font=("calibri Bold", 15)).place(
                    x=500, y=150)

                cat = Label(del_frame, fg="white", bg="black", text=final_list[0][2], font=("calibri Bold", 15)).place(
                    x=500, y=220)

                qua = Label(del_frame, fg="white", bg="black", text=final_list[0][3], font=("calibri Bold", 15)).place(
                    x=500, y=290)

                pri = Label(del_frame, fg="white", bg="black", text=final_list[0][4], font=("calibri Bold", 15)).place(
                    x=500, y=360)

                decrp = Label(del_frame, fg="white", bg="black", text=final_list[0][5],
                              font=("calibri Bold", 15)).place(x=500, y=410)




        search = Button(del_frame, text="SEARCH", command=search, font=("calibri Bold", 13)).place(x=800, y=50)



        def delete():

            id = id_combo.get()

            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")
            cursor = mydb.cursor()

            cursor.execute("delete from products where pro_name= '" + id + "' ")
            mydb.commit()
            speak = Dispatch(("SAPI.SpVoice"))
            speak.Speak("deleted successfully")
            messagebox.showinfo("REQUIRED FIELD", "DELETED")

        delete1 = Button(del_frame, text="DELETE", command=delete, font=("calibri Bold", 13)).place(x=600, y=500)










