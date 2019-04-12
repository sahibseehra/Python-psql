import pymysql as psql
from tkinter import *
import re
from tkinter import messagebox
from display_table import *
from delete_sql import *

def button1_click():
    r=tbnamer.get()
    n=tbnamen.get()
    m=tbnamem.get()
    con=psql.connect("localhost","root","","sahib")

    qry="insert into student values("+r+",'"+n+"',"+m+")"

    cr=con.cursor()

    result=cr.execute(qry)
    if(result>0):
        messagebox.showinfo("DONE!!","Records has been updated")
    else:
        messagebox.showinfo("SORRY","please check your input")
        
def button2_click():
    load_display_table(win)
def button3_click():
    load_delete_row(win)
win=Tk()

win.state("zoomed")

win.config(bg='#9999ff')

lbl=Label(win,text="Roll Number:",bg="#9999ff",fg="red",font=('arial',15))#or use config function
lbl.place(x=320,y=195)
lbl=Label(win,text="Name",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=330,y=225)
lbl=Label(win,text="Marks",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=330,y=255)
lbl=Label(win,text="DELETE an ENTRY:",bg="#9999ff",fg="red",font=('arial',15))
lbl.place(x=630,y=455)
tbnamer=Entry(win,width=80)
tbnamer.place(x=500,y=200)
tbnamen=Entry(win,width=80)
tbnamen.place(x=500,y=230)
tbnamem=Entry(win,width=80)
tbnamem.place(x=500,y=260)

btn1=Button(win,text="INSERT",bg="blue",fg="white",command=button1_click)
btn1.place(x=550,y=300)
btn2=Button(win,text="View table",bg="blue",fg="white",command=button2_click) 
btn2.place(x=650,y=300)
btn3=Button(win,text="click to DELETE",bg="blue",fg="white",command=button3_click) 
btn3.place(x=650,y=500)
win.mainloop()






win.mainloop()
