from Tkinter import Tk, Label, Entry, Button, StringVar

my_app = Tk(className = 'Figure Of Square')

L1 = Label(my_app, text = 'Figure Of Square', font=('Arial', 24))
L1.grid(row=0, column=0)

L2 = Label(my_app, text = 'square, dimension two, example: books,paper')
L2.grid(row=1, column = 0)

L3 = Label(my_app, text = 'Side')
L3.grid(row=2, column = 0)
str3 = StringVar()
E3 = Entry(my_app, textvariable = str3)
E3.grid(row=2, column = 1)

L4 = Label(my_app, text = 'result')
L4.grid(row=3, column = 0)

L5 = Label(my_app, text='0')
L5.grid(row=3, column = 1)

def area():
    s = float(str3.get())
    result = s*s
    L5.config(text=result)

B1 = Button(my_app, text = 'calculate area', command = area)
B1.grid(row=3,column=0)

my_app.mainloop()
