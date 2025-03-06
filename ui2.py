from tkinter import *
window = Tk()
window .geometry("300x50")
window .title("Welcome")
lbl_welcome = Label(window,text="Welcome",font="arial 30")
lbl_welcome.pack()
def destory():
    window .destroy()
def run():
    window .after(1,run)
    window .mainloop()
