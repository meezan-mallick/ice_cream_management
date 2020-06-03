from tkinter import *
from product_dir import new_pro
from product_dir import veiw_products
from product_dir import *

class product_frame:
    def __init__(self,win):

        side_nav = Frame(win,bd=5,relief=GROOVE, bg="lightyellow")
        side_nav.place(x=0, y=150, width=299, height=650)

        l = Label(side_nav, text="PRODUCT", font=("Times New Roman Bold",18), bg="lightyellow",fg="black")
        l.place(x=70, y=50)



        def button_bg(button):
            self.add.config(bg="lightgray",fg="black")
            self.view.config(bg="lightgray",fg="black")
            self.update.config(bg="lightgray",fg="black")
            self.delete.config(bg="lightgray",fg="black")

            button.config(bg="black",fg="white")




        def add_pro():
            add_frame=new_pro.add_pro(win)
            button_bg(self.add)



        self.add= Button(side_nav,bg="lightgray", text="ADD", font=("Times New Roman Bold", 16),command=add_pro)
        self.add.place(x=30, y=100, width=200, height=50)

        def veiw_pro():
            add_frame=veiw_products.view_pro(win)
            button_bg(self.view)






        self.view= Button(side_nav, bg="lightgray", text="VIEW", font=("Times New Roman Bold", 16),command=veiw_pro)
        self.view.place(x=30, y=200, width=200, height=50)


        def update_pro():
            add_frame=veiw_products.update_product(win)
            button_bg(self.update)

        self.update = Button(side_nav, bg="lightgray", text="UPDATE", font=("Times New Roman Bold", 16),command=update_pro)
        self.update.place(x=30, y=300, width=200, height=50)

        def delete_pro():
            delete_frame=veiw_products.delete(win)
            button_bg(self.delete)

        self.delete= Button(side_nav, bg="lightgray",text="DELETE", font=("Times New Roman Bold", 16),command=delete_pro)
        self.delete.place(x=30, y=400, width=200, height=50)

        add_pro()