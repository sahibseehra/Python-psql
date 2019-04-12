from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql as psql
import re
def close_window():
    win.close()
'''def close_win(reg_win):'''
     
    
def register_window():
    
    def register_click():
        n=username.get()
        p=password.get()
        con=psql.connect("localhost","root","","sahib")
        '''qry="create table  Login_data(name char,password varchar)"'''
        qry="insert into Login_data values("+n+","+p+")"
        cr=con.cursor()
        result=cr.execute(qry)
        if(result>0):
           messagebox.showinfo("DONE!!","Records has been updated")
        else:
           messagebox.showinfo("SORRY","please check your input")
    win.iconify()
    reg_win=Tk()
    reg_win.state('zoomed')
    reg_win.config(bg='#9999ff')
    lbl=Label(reg_win,text="Create Username:",fg="black",bg="white",font=('arial',10))
    lbl.place(x=420,y=240)
    lbl=Label(reg_win,text="Create Password",fg="red",bg="white",font=('arial',10))
    lbl.place(x=430,y=280)
    username=Entry(reg_win,width=50,bg="#99bbff")
    username.place(x=590,y=240)
    password=Entry(reg_win,width=50,bg="#99bbff",show="*")
    password.place(x=590,y=280)
    btn4=Button(reg_win,text="Register",bg="blue",fg="white",command=register_click) 
    btn4.place(x=625,y=350)
    '''btn5=Button(reg_win,text="cancel",bg="blue",fg="white",command=close_win)
    btn5.place(x=685,y=350)'''
    reg_win.mainloop()
    
win=Tk()

win.state('zoomed')
win.config(bg='#9999ff')
win.title('python REgister window')
canv=Canvas(win,height=1080,width=1920)

canv.place(x=0,y=0)

img=ImageTk.PhotoImage(Image.open("login_bg.jpg"))
canv.create_image(960,540,image=img)
canv2=Canvas(canv,height=200,width=600,bg="white")
canv2.place(x=395,y=200)

btn1=Button(win,text="Login",bg="blue",fg="white") 
btn1.place(x=625,y=350)
btn2=Button(win,text="cancel",bg="blue",fg="white",command=close_window)
btn2.place(x=755,y=350)
btn3=Button(win,text="Register",bg="blue",fg="white",command=register_window)
btn3.place(x=685,y=350)
lbl=Label(win,text="Enter Username:",fg="black",bg="white",font=('arial',10))
lbl.place(x=420,y=240)
lbl=Label(win,text="Password",fg="red",bg="white",font=('arial',10))
lbl.place(x=430,y=280)
tbname1=Entry(win,width=50,bg="#99bbff")
tbname1.place(x=590,y=240)
tbname2=Entry(win,width=50,bg="#99bbff",show="*")
tbname2.place(x=590,y=280)
win.mainloop()
