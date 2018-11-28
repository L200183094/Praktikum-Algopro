def konversiSuhu(C = 0,F = 0):
    f = int((C*9/5)+32)
    c = int(5/9*(F-32))
    if C != 0:
        print(C, "celcius is same with", f, "fahrenheit")
    elif F != 0:
        print(F, "fahrenheit is same with", c, "celcius")
    else:
        print(C, "celcius is same with", f, "fahrenheit")