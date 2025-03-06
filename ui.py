from tkinter import *
import backend
win = Tk()
win.geometry("540x350+430+200")
win.resizable(0,0)
win.config(bg="light blue")
#==================================
student = backend.Exam("E:/python3/Exam_1/db1.db")
student.create_table()
#==================================
def updateall():
    _lst = student.update_all()
    for i in _lst:
        lst.insert(END,i)
def insert():
    student.insert(ent_name.get(),ent_lname.get(),ent_pass.get(),ent_name_dore.get())
    updateall()
def delete():
    student.delete(lst.curselection())
    updateall()
#==================================
lbl_name = Label(text="Name :",font=20,bg="light blue")
lbl_name.place(x=20,y=20)

lbl_lname = Label(text="Family :",font=20,bg="light blue")
lbl_lname.place(x=310,y=20)

lbl_pass = Label(text="Pass :",font=20,bg="light blue")
lbl_pass.place(x=25,y=80)

lbl_name_dore = Label(text="Name dore :",font=20,bg="light blue")
lbl_name_dore.place(x=280,y=80)

lbl_pass2 = Label(text="Pass :",font=20,bg="light blue")
lbl_pass2.place(x=20,y=320)

lbl_star = Label(text="*",fg="red",bg="light blue",font=15)
lbl_star.place(x=10,y=20)

lbl_star1 = Label(text="*",fg="red",bg="light blue",font=15)
lbl_star1.place(x=300,y=20)

lbl_star2 = Label(text="*",fg="red",bg="light blue",font=15)
lbl_star2.place(x=10,y=80)
#================================================
ent_name =Entry(win)
ent_name.place(x=80,y=20)

ent_lname =Entry(win)
ent_lname.place(x=380,y=20)

ent_pass =Entry(win,show="*")
ent_pass.place(x=80,y=80)

ent_name_dore =Entry(win)
ent_name_dore.place(x=380,y=80)

ent_pass2 =Entry(win)
ent_pass2.place(x=70,y=320,width=250)
#==================================================
btn_show = Button(win,text="show all",width=16,height=1,command=updateall)
btn_show.place(x=380,y=120)

btn_add = Button(win,text="insert",width=16,height=1,command=insert)
btn_add.place(x=380,y=160)

btn_clear= Button(win,text="clear",width=16,height=1)
btn_clear.place(x=380,y=200)

btn_delet= Button(win,text="delet",width=16,height=1)
btn_delet.place(x=380,y=240)

btn_exit= Button(win,text="exit",width=16,height=1)
btn_exit.place(x=380,y=280)

btn_login= Button(win,text="login",width=16,height=1)
btn_login.place(x=380,y=320)

#==================================
lst = Listbox(win)
lst.place(x=20,y=120,width=300,height=180)





win.mainloop()