from datetime import date
from tabulate import *
from tkinter import *
import mysql.connector
from tkinter.ttk import Combobox
from tkscrolledframe import ScrolledFrame



class bill_entry:

    def __init__(self, win):

        sf = ScrolledFrame(win, width=1510, height=620)
        sf.place(x=0, y=152)
        # sf.pack(side="top",expand=1,fill="both")

        sf.bind_arrow_keys(win)
        sf.bind_scroll_wheel(win)

        canvas = sf.display_widget(Canvas)
        canvas.config( width=1610, height=1200)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")
        list5 = []

        cursor = mydb.cursor()
        cursor.execute("select bill_id from bill_records")
        list6 = cursor.fetchall()

        cursor.execute("select bill_date from bill_records")
        list1 = cursor.fetchall()
        # print(tabulate(list))

        cursor.execute("select customer_name from bill_records")
        list2 = cursor.fetchall()

        cursor.execute("select pro_name from bill_records")
        list3 = cursor.fetchall()

        cursor.execute("select pro_quantity from bill_records")
        list4 = cursor.fetchall()

        cursor.execute("select sub_total from bill_records")
        list5 = cursor.fetchall()

        title1 = Label(canvas,  text="Bill ID", font=("calibri Bold", 15)).place(x=70, y=90)

        title2 = Label(canvas,  text="Date", font=("calibri Bold", 15)).place(x=190, y=90)

        title3 = Label(canvas,  text="Customer", font=("calibri Bold", 15)).place(x=280, y=90)

        title4 = Label(canvas,  text="Products", font=("calibri Bold", 15)).place(x=700, y=90)

        title5 = Label(canvas,  text="Quantity", font=("calibri Bold", 15)).place(x=1220, y=90)

        title6 = Label(canvas,  text="Sub Total", font=("calibri Bold", 15)).place(x=1350, y=90)

        ym1 = 90
        for m in range(0, list6.__len__()):
            label = Label(canvas,  text=list6[m], font=("calibri regular", 15))
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

            label = Label(canvas,  text=d, font=("calibri regular", 15))
            y2 = y2 + 40
            ind = ind + 1
            label.place(x=140, y=y2)
            y1 = y2 + 35
            ym2 = y1
            canvas.create_line(40, y1, 1450, y1, fill='black')

        y2 = 90

        for i in range(0, list2.__len__()):
            label = Label(canvas,  text=list2[i], font=("calibri regular", 15))
            y2 = y2 + 40
            label.place(x=290, y=y2)

        canvas.create_line(40, 80, 1450, 80, fill='black')

        canvas.create_line(40, 120, 1450, 120, fill='black')

        canvas.create_line(40, 80, 40, ym2, fill='black')
        canvas.create_line(130, 80, 130, ym2, fill='black')
        canvas.create_line(250, 80, 250, ym2, fill='black')
        canvas.create_line(390, 80, 390, ym2, fill='black')
        canvas.create_line(1200, 80,1200, ym2, fill='black')
        canvas.create_line(1320, 80,1320, ym2, fill='black')
        canvas.create_line(1450, 80,1450, ym2, fill='black')

        '''l3 = list(list3)
        ind = 0
        print(l3)'''

        y2 = 90
        for i in range(0, list3.__len__()):
            '''a = str(l3[ind])

            c = a.replace("('", "")
            d = c.replace("',)", "")'''

            label = Label(canvas,  text=list3[i], font=("calibri regular", 15))
            y2 = y2 + 40
            label.place(x=430, y=y2)

        y2 = 90
        for i in range(0, list4.__len__()):
            label = Label(canvas,  text=list4[i], font=("calibri regular", 15))
            y2 = y2 + 40
            label.place(x=1240, y=y2)



        y2 = 90
        for i in range(0,list5.__len__()):


            label = Label(canvas,  text=list5[i], font=("calibri regular", 15))
            y2 = y2 + 40
            ind = ind + 1
            label.place(x=1370, y=y2)




