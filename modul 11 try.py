####TRY
##from Tkinter import Tk
##my_app = Tk()
##my_app.mainloop()
##
####TRY 2
####window eith edit box and label
##from Tkinter import Tk, Label, Entry
##from Tkinter import LEFT, RIGHT
##my_app = Tk(className = 'Aplikation with label')
##
##L1 = Label(my_app, text="Nama Mahasiswa")
##L1.pack(side=LEFT)
##E1 = Entry(my_app)
##E1.pack(side = RIGHT)
##
##my_app.mainloop()
##
## try 3
####window with button, some edit box and label
##from Tkinter import Tk, Label, Entry, Button
##from tkMessageBox import showinfo
##
##my_app = Tk(className = 'Aplication with some widget')
##L1 = Label(my_app, text = "Nama Mahasiswa")
##L1.grid(row= 0, column = 0)
##E1 = Entry(my_app)
##E1.grid(row= 0, column = 1)
##L2 = Label(my_app, text ='NIM')
##L2.grid(row= 1, column = 0)
##E2 = Entry(my_app)
##E2.grid(row= 1, column = 1)
##
##def tampil_pesan():
##    showinfo("pesan", "hello world")
##
##B = Button(my_app, text = "Hello", command = tampil_pesan)
##B.grid(row = 2, column=1)
##my_app.mainloop()

##===========================================================
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Access to widget properti')
L1 = Label(my_app, text = "Nama Mahasiswa")
L1.grid(row= 0, column = 0)
str1 = StringVar()
E1 = Entry(my_app, textvariable = str1)
E1.grid(row= 0, column = 1)
L2 = Label(my_app, text = "umur")
L2.grid(row= 1, column = 0)
str2 = StringVar(value = 0)
E2 = Entry(my_app, textvariable = str2)
E2.grid(row= 1, column = 1)

def info():
    """Take data in Entry E1 anf E2, and show with messagebox"""
    _info = str1.get() + "berumur" + str2.get() + "tahun"
    showinfo("pesan", _info)

def hapus():
    "Erase teks in entry E1 and E2"
    str1.set("")
    str2.set("0")

B1 = Button(my_app, text = "informasi", command=info)
B1.grid(row= 2, column = 1)
B2 =  Button(my_app, text = "clear", command=hapus)
B2.grid(row= 2, column = 0)

my_app.mainloop()
