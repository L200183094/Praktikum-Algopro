##window with button, some edit box and label
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Aplication with some widget')
L1 = Label(my_app, text = "Nama Mahasiswa")
L1.grid(row= 0, column = 0)
str1 = StringVar()
E1 = Entry(my_app, textvariable = str1)
E1.grid(row= 0, column = 1)
L2 = Label(my_app, text ='NIM')
L2.grid(row= 1, column = 0)
str2 = StringVar()
E2 = Entry(my_app, textvariable = str2)
E2.grid(row= 1, column = 1)
L3 = Label(my_app, text ='Favorite book')
L3.grid(row= 2, column = 0)
str3 = StringVar()
E3 = Entry(my_app, textvariable = str3)
E3.grid(row= 2, column = 1)
L4 = Label(my_app, text ='idol')
L4.grid(row= 3, column = 0)
str4 = StringVar()
E4 = Entry(my_app, textvariable = str4)
E4.grid(row= 3, column = 1)
L5 = Label(my_app, text ='Motto')
L5.grid(row= 4, column = 0)
str5 = StringVar()
E5 = Entry(my_app, textvariable = str5)
E5.grid(row= 4, column = 1)

def dataDiri():
    _dataDiri = "Data Diri" +"\n"+" Name : " + str1.get()+"\n"+"NIM : " + str2.get() +"\n"+ " Favorite Book : " + str3.get() +"\n"+ " Idol : " + str4.get()+"\n"+" Motto : " + str5.get()
    
    showinfo("pesan",_dataDiri)

B = Button(my_app, text = "coba", command = dataDiri)
B.grid(row = 5, column=1)

my_app.mainloop()

