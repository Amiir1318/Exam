from tkinter import *
from tkinter import messagebox
import backend
win = Tk()
win.geometry("540x350+430+200")
win.resizable(0,0)
win.config(bg="light blue")
#==================================
student = backend.Exam("F:/python3/Exam_1/db1.db")
student.create_table()
#==================================
def clear():
    ent_lname.delete(0,END)
    ent_name.delete(0,END)
    ent_pass.delete(0,END)
    ent_name_dore.delete(0,END)
def updateall():
    lst.delete(0,END)
    _lst = student.update_all()
    for i in _lst:
        lst.insert(END,i)
def insert():
    if len(ent_name.get()) > 0 and len(ent_lname.get()) > 0 and len(ent_pass.get()) > 0:
        lst.delete(0,END)
        student.insert(ent_name.get(),ent_lname.get(),ent_pass.get(),ent_name_dore.get())
        updateall()
        clear()
    else:
        messagebox.showerror("I Can't","Please fill force entry")
def delete():
    resualt = messagebox.askyesno("Delete","Are you sure?")
    if resualt == True:
        s = f"{lst.get(lst.curselection()[0])}".split("-")[0]
        student.delete(s)
        lst.delete(0,END)
        updateall()
def exit():
    resualt = messagebox.askyesno("Exit","Are you sure?")
    if resualt == True:
        win.destroy()
def login():
    resualt = student.login(ent_pass2.get())
    if resualt == True:
        import ui2
    else:
        messagebox.showinfo("Not found","Not found this password")
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

btn_clear= Button(win,text="clear",width=16,height=1,command=clear)
btn_clear.place(x=380,y=200)

btn_delet= Button(win,text="delete",width=16,height=1,command=delete)
btn_delet.place(x=380,y=240)

btn_exit= Button(win,text="exit",width=16,height=1,command=exit)
btn_exit.place(x=380,y=280)

btn_login= Button(win,text="login",width=16,height=1,command=login)
btn_login.place(x=380,y=320)

#==================================
lst = Listbox(win)
lst.place(x=20,y=120,width=300,height=180)





win.mainloop()
