import pymysql as psql
from tkinter import *
import re
from display_table import *
from tkinter import messagebox
def load_delete_row(mwindow):
    mwindow.destroy()
    def button1_click():
        r=tbnamer.get()
        con=psql.connect("localhost","root","","sahib")

        qry="delete from student where Roll_No="+r+""

        cr=con.cursor()

        result=cr.execute(qry)
        if(result>0):
            messagebox.showinfo("DONE!!","Records has been deleted")
        else:
            messagebox.showinfo("SORRY","please check your input")
    def button2_click():
        load_display_table(root)
    root=Tk()
    root.state("zoomed")
    root.config(bg="#9999ff")
    lbl=Label(root,text="Roll Number:",bg="#9999ff",fg="red",font=('arial',15))#or use config function
    lbl.place(x=320,y=195)
    tbnamer=Entry(root,width=80)
    tbnamer.place(x=500,y=200)
    btn1=Button(root,text="DELETE",bg="blue",fg="white",command=button1_click)
    btn1.place(x=550,y=250)
    btn2=Button(root,text="display table",bg="blue",fg="white",command=button2_click)
    btn2.place(x=550,y=290)


    root.mainloop()
