from tkinter import *
from product_dir import db_connection
import mysql.connector
from tkinter.ttk import Combobox

from datetime import date
from tabulate import *




class bill_frame:
    def __init__(self,win):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")




        my_frame=Frame(win,bg="snow",bd=5,relief=GROOVE)
        my_frame.place(x=0, y=150, width=1536, height=650)

        l = Label(my_frame, text="Customer Name:", font=("Times New Roman", 16))
        l.place(x=50,y=50)
        cus_tf=Entry(my_frame)
        cus_tf.place(x=250,y=50,width=150,height=30)

        l1 = Label(my_frame, text="Customer phone no:", font=("Times New Roman", 16))
        l1.place(x=50,y=100)
        #cus_no = Entry(my_frame)
        #cus_no.place(x=700, y=50, width=150, height=30)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")

        cursor = mydb.cursor()
        cursor.execute("select ph_no from customer")
        c_list = cursor.fetchall()
        print(c_list[0][0])

        no = Combobox(my_frame)
        no['values'] = c_list
        no.current(0)
        no.place(x=250,y=100, width=150, height=30)

        def customer_db():

            cursor = mydb.cursor()
            cursor.execute("select name from customer where ph_no= '"+no.get()+"' ")
            name = cursor.fetchall()
            print()

            cus_tf.delete(END,0)
            cus_tf.insert(END,name[0])
            print()

        get_cst = Button(my_frame, text="GET CUSTOMER", font=("Times New Roman", 16), command=customer_db)
        get_cst.place(x=150, y=150, width=200, height=30)


        cursor = mydb.cursor()
        cursor.execute("select pro_name from products")
        list = cursor.fetchall()

        combo = Combobox(my_frame)
        combo['values'] = list
        combo.current(0)
        combo.place(x=250, y=200, width=150, height=30)


        #print(list)


        pro = Label(my_frame, text="product", font=("Times New Roman", 16))
        pro.place(x=50, y=200)
        pro_tf = Entry(my_frame)
        #pro_tf.place(x=300, y=100, width=150, height=30)


        qua = Label(my_frame, text="Quantity", font=("Times New Roman", 16))
        qua.place(x=50,y=250)

        sp=Spinbox(my_frame,from_=1,to=50)
        sp.place(x=250, y=250, width=150, height=30)






        bill_frame = Frame(my_frame, bg="lightgreen",bd=5,relief=GROOVE)
        bill_frame.place(x=420, y=50, width=1100, height=550)



        title = ["ID", "NAME", "CATGRY", "PRICE", "QUANTITY", "TOTAL"]
        a="PRODUCT ID \t\t PRODUCT NAME\t\t \t PRICE \t\t \t QUANTITY\t\t TOTAL"

        lab = Label(bill_frame, text=a,
                    font=("Times New Roman", 13), bg="lightgreen")
        lab.grid(row=0, column=0)


        row = Label(bill_frame, text="20",state=DISABLED)

        total = Label(bill_frame, text="0", state=DISABLED)

        max_item = Label(bill_frame, text="0", state=DISABLED)

        name_list=[]
        quanty_list=[]
        price_list=[]
        tol_list=[]

        maxitem=0

        def add():

            maxitem=int(max_item['text'])

            maxitem=maxitem+1
            max_item.config(text=maxitem)


            if(maxitem<16):
                ab = int(row['text'])
                ab = ab + 30
                row.config(text=ab)

                tot = int(total['text'])

                if (cus_tf.get() == ""):
                    messagebox.showerror("REQUIRED FIELD", "CUSTOMER NAME MISSING")

                elif (no.get() == ""):
                    messagebox.showerror("REQUIRED FIELD", "CUSTOMER PHONE NUMBER")

                elif (combo.get() == ""):
                    messagebox.showerror("REQUIRED FIELD", "SELECT PRODUCT")
                else:
                    mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018",
                                                   database="ice_creame")

                    cursor = mydb.cursor()

                    query = "select * from products where pro_name='" + combo.get() + "'"
                    cursor.execute(query)
                    list1 = cursor.fetchall()

                    id = list1[0][0]
                    name = list1[0][1]
                    price = list1[0][4]
                    quant = int(sp.get())
                    final_total = price * quant

                    tot = tot + final_total
                    total.config(text=tot)

                    # print(tabulate(list1))

                    record = "" + str(id) + "     " + name + "     " + str(price) + "     " + str(
                        quant) + "     " + str(total)
                    record1 = Label(bill_frame, text=str(id), font=("Times New Roman", 16), bg="lightgreen")
                    record1.place(x=30, y=ab)

                    record2 = Label(bill_frame, text=name, font=("Times New Roman", 16), bg="lightgreen")
                    record2.place(x=210, y=ab)

                    record3 = Label(bill_frame, text=str(price), font=("Times New Roman", 16), bg="lightgreen")
                    record3.place(x=510, y=ab)

                    record4 = Label(bill_frame, text=str(quant), font=("Times New Roman", 16), bg="lightgreen")
                    record4.place(x=740, y=ab)

                    record5 = Label(bill_frame, text=str(final_total), font=("Times New Roman", 16), bg="lightgreen")
                    record5.place(x=940, y=ab)

                    '''record6 = Label(bill_frame, text="GRANT TOTAL :"+str(total['text']), font=("Times New Roman", 16), bg="lightgreen")
                    record6.place(x=900, y=300)'''

                    # date = Label(bill_frame, text=d1, bg="lightgreen", font=("Times New Roman", 16))
                    # date.place(x=450, y=50)

                    # line=Label(bill_frame, text=d1,bg="lightgreen",font=("calibri", 16))
                    # line.place(x=1300,y=10)

                    name_list.append(name)
                    quanty_list.append(quant)
                    price_list.append(price)
                    tol_list.append(final_total)

                    def check():

                        a = str(cus_tf.get())
                        b = str(total['text'])
                        print(name_list)

                        bill = Tk()
                        # bill.geometry("520x720")
                        bill.minsize(520, 750)
                        bill.maxsize(520, 750)

                        mycanvas = Canvas(bill, width=1000, height=1000, background='snow')
                        mycanvas.place(x=0, y=0)

                        mycanvas.create_line(0, 90, 520, 90, fill='black')

                        addrs = Label(mycanvas, text="Havmor \n University campus Ahmedabad \n www.meezanmalek.com",
                                      font=("calibri regular", 13), bg="snow").place(x=150, y=20)

                        name = Label(mycanvas, text="Name : " + a + " ", font=("calibri regular", 13), bg="snow").place(
                            x=30, y=100)
                        date = Label(mycanvas, text="Date : " + d1 + " ", font=("calibri regular", 13),
                                     bg="snow").place(x=370, y=100)

                        mycanvas.create_line(0, 130, 520, 130, fill='black')

                        item = Label(mycanvas, text="Item ", font=("calibri regular", 13), bg="snow").place(x=40, y=140)
                        qty = Label(mycanvas, text="Quantity", font=("calibri regular", 13), bg="snow").place(x=200,
                                                                                                              y=140)
                        pri = Label(mycanvas, text="Price", font=("calibri regular", 13), bg="snow").place(x=310, y=140)
                        amt = Label(mycanvas, text="Amount", font=("calibri regular", 13), bg="snow").place(x=400,
                                                                                                            y=140)

                        ym1 = 150
                        for m in range(0, name_list.__len__()):
                            name = Label(mycanvas, text=name_list[m], font=("calibri regular", 13), bg="snow")
                            ym1 = ym1 + 30
                            name.place(x=30, y=ym1)

                        tot_qunt = 0
                        ym2 = 150
                        for m in range(0, quanty_list.__len__()):
                            name = Label(mycanvas, text=quanty_list[m], font=("calibri regular", 13), bg="snow")
                            tot_qunt = tot_qunt + quanty_list[m]
                            ym2 = ym2 + 30
                            name.place(x=220, y=ym2)

                        print(price_list)

                        ym3 = 150
                        for z in range(0, price_list.__len__()):
                            name = Label(mycanvas, text=price_list[z], font=("calibri regular", 13), bg="snow")
                            ym3 = ym3 + 30
                            name.place(x=320, y=ym3)

                        sub_total = 0

                        ym3 = 150
                        for z in range(0, price_list.__len__()):
                            name = Label(mycanvas, text=tol_list[z], font=("calibri regular", 13), bg="snow")
                            sub_total = sub_total + tol_list[z]
                            ym3 = ym3 + 30
                            name.place(x=420, y=ym3)

                        print(sub_total)
                        ym3 = ym3 + 40
                        mycanvas.create_line(0, ym3, 520, ym3, fill='black')
                        ym3 = ym3 + 20
                        sub = Label(mycanvas, text="Sub Total : " + str(sub_total) + " ", font=("calibri Bold", 13),
                                    bg="snow")
                        sub.place(x=350, y=ym3)

                        tot_qun = Label(mycanvas, text="Total Quantity : " + str(tot_qunt) + " ",
                                        font=("calibri Bold", 13),
                                        bg="snow")
                        tot_qun.place(x=110, y=ym3)

                        gst1 = (sub_total * 5) / 100
                        ym3 = ym3 + 30
                        gst = Label(mycanvas, text="  GST 5% : " + str(gst1) + " ", font=("calibri Bold", 13),
                                    bg="snow")
                        gst.place(x=355, y=ym3)

                        net1 = int(sub_total) + gst1

                        net = Label(mycanvas, text="Net Amount : " + str(net1) + " ", font=("calibri Bold", 13),
                                    bg="snow")
                        net.place(x=325, y=ym3 + 30)


                        def done():

                            d1
                            a# custome name
                            name_list# products name
                            tot_qunt
                            sub_total

                            pro_names=""

                            for i in range (name_list.__len__()):

                                pro_names=pro_names+","+name_list[i]

                            print(pro_names)



                            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018",
                                                           database="ice_creame")

                            cursor = mydb.cursor()

                            sql = "insert into bill_records (bill_date,customer_name,pro_name,pro_quantity,sub_total) values (%s,%s,%s,%s,%s)"
                            var = (str(d1),str(a),pro_names,tot_qunt,sub_total)
                            cursor.execute(sql, var)
                            mydb.commit()









                        done=Button(mycanvas,text="DONE",font=("calibri Bold", 13),command=done)
                        done.place(x=150, y=700)




                        bill.mainloop()



                checkout = Button(bill_frame, text="CHECK OUT", font=("Times New Roman", 16), command=check)
                checkout.place(x=50, y=500, width=150, height=30)


            else:
                messagebox.showerror("MAXIMUM ITEMS", "ONE BILL PAGE HAS CAPACITY OF MAXIMUM 15 ITEMS")




        b1=Button(my_frame, text="ADD",font=("Times New Roman", 16),command=add)
        b1.place(x=170, y=300, width=150, height=30)



















class customer:

    def __init__(self,win):

        my_frame=Frame(win,bg="lemonchiffon")
        my_frame.place(x=0, y=150, width=1536, height=650)

        l = Label(my_frame, text="Customer Name:", font=("Times New Roman", 16))
        l.place(x=100, y=50)
        cus_tf = Entry(my_frame)
        cus_tf.place(x=300, y=50, width=150, height=30)

        l1 = Label(my_frame, text="Customer phone no:", font=("Times New Roman", 16))
        l1.place(x=500, y=50)
        cus_no = Entry(my_frame)
        cus_no.place(x=700, y=50, width=150, height=30)


        def addcos():

            name=cus_tf.get()
            ph=cus_no.get()

            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")

            cursor = mydb.cursor()

            sql = "insert into customer (name,ph_no) values (%s,%s)"
            var = (name,str(ph))
            cursor.execute(sql, var)
            mydb.commit()
            print("yo")


        addcus=Button(my_frame, text="ADD",font=("Times New Roman", 16),command=addcos)
        addcus.place(x=900, y=50, width=150, height=30)

        def dele():

            name=str(cus_tf.get())

            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")
            cursor = mydb.cursor()

            cursor.execute("delete from customer where name= '" + name + "' ")
            mydb.commit()
            messagebox.showinfo("REQUIRED FIELD", "DELETED")





        delcus = Button(my_frame, text="DELETE", font=("Times New Roman", 16),command=dele)
        delcus.place(x=1200, y=50, width=150, height=30)

        table= Frame(my_frame, bg="black", bd=5, relief=GROOVE)
        table.place(x=300, y=150, width=836, height=470)

        name = Label(table, text="NAME",bg="black",fg="white", font=("Times New Roman", 16))
        name.place(x=120, y=70)

        name = Label(table, text="phone number",bg="black",fg="white", font=("Times New Roman", 16))
        name.place(x=300, y=70)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Meezan#2018", database="ice_creame")

        cursor = mydb.cursor()
        cursor.execute("select name from customer")
        name = cursor.fetchall()


        cursor.execute("select ph_no from customer")
        ph = cursor.fetchall()

        cursor.execute("select * from customer")
        all= cursor.fetchall()

        ym1 = 100
        for m in range(0, name.__len__()):
            label = Label(table, bg="black",fg="white", text=name[m], font=("calibri Bold", 15))
            ym1 = ym1 + 30
            label.place(x=120, y=ym1)

        ym1 = 100
        for n in range(0, name.__len__()):
            label = Label(table, bg="black",fg="white", text=ph[n], font=("calibri Bold", 15))
            ym1 = ym1 + 30
            label.place(x=300, y=ym1)














