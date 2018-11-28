## activity 1 by: farah husna L200183094
d = {"NIM":"L200183094", "Name":"Farah  Husna Paramadina", "Address":"ceper,klaten", "Post_Code":"57465", "City":"klaten", "Province":"Jawa Tengah", "Nasionality":"indonesia"}
def b():
    print('''Pilihan yang tersedia:
    b will show this help
    N will show NIM
    a will show Name
    L will show Address
    o will show Post Code
    C will show City
    P will show Province
    W will show Nasionality
    k will show exit ''')

b()

repeat = True
while repeat:
    v= input('Your Choice:')
    if v == 'b':
        b()
    elif v == 'N':
        print("NIM :", d["NIM"])
    elif v == 'a':
        print("Name :", d["Name"])
    elif v == 'L':
        print("Address :", d["Address"])
    elif v == 'o':
        print("Post Code :", d["Post_Code"])
    elif v == 'C':
        print("City :", d["city"])
    elif v == 'P':
        print("Province :", d["Province"])
    elif v == 'W':
        print("Nasionality :", d["Nasionality"])
    elif v == 'k':
        repeat = False
        print("exit")