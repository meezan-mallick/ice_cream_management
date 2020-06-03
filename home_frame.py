from tkinter import *
import product_frame
import bill_main
import bill_records
import pygame
import playsound
#from win32com.client import Dispatch

window =Tk()
window.title("LOG-IN")

window.state("zoomed")
w,h=window.winfo_screenwidth(),window.winfo_screenheight()
print(w,h)
window.minsize(1536,864)


class home_frame:
    def __init__(self,win,w,h):

        #palevioletred

        self.my_frame=Frame(win,bg="lightpink",bd=5,relief=GROOVE)
        self.my_frame.place(x=0,y=0,width=w,height=h)

        """self.p = PhotoImage(file="image.png")
        label_1 = Button(self.my_frame, image=self.p, height=1536, width=864)
        label_1.pack()
        print("Datata")"""

        def button_bg(button):
            self.product.config(bg="lightgray",fg="black")
            self.customer.config(bg="lightgray",fg="black")
            self.sold_products.config(bg="lightgray",fg="black")
            self.billing.config(bg="lightgray",fg="black")

            button.config(bg="black",fg="white")

        def pro():
            miz = product_frame.product_frame(self.my_frame)
            button_bg(self.product)


        l = Label(self.my_frame, text="HAVMOR", font=("calibri Bold",23), bg="lightpink",fg="white")
        l.place(x=700, y=20)


        def close():

            speak=Dispatch(("SAPI.SpVoice"))
            speak.Speak("dear customers the shop is going to close in 15 minutes ")



        close=Button(self.my_frame,text="Close",font=("calibri Bold",13),command=close).place(x=1400, y=80)




        self.product= Button(self.my_frame, bg="lightgray", text="Product",font=("Times New Roman Bold",15),command=pro)
        self.product.place(x=200, y=80,width=200,height=50)



        def customer():
            miz = bill_main.customer(self.my_frame)
            button_bg(self.customer)



        self.customer = Button(self.my_frame ,bg="lightgray", text="Customer",font=("Times New Roman Bold",15),command=customer)
        self.customer.place(x=500, y=80,width=200,height=50)



        def sold_products():
            miz = bill_records.bill_entry(self.my_frame)
            button_bg(self.sold_products)


        self.sold_products = Button(self.my_frame,  bg="lightgray",text="Bill Records",font=("Times New Roman Bold",15),command=sold_products)
        self.sold_products.place(x=800, y=80,width=200,height=50)

        def bill():
            miz = bill_main.bill_frame(self.my_frame)
            button_bg(self.billing)

        self.billing = Button(self.my_frame, bg="lightgray", text="Billing",font=("Times New Roman Bold",15),command=bill)
        self.billing.place(x=1100, y=80,width=200,height=50)

        pro()


a1=home_frame(window,w,h)
window.mainloop()


