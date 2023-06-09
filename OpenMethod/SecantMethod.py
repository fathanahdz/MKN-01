#Mengimport modul math untuk menggunakan fungsi exponensialnya
import math                                     

#Fungsi untuk f'(x)
def faksen(f, x):                               
    h = 1e-6  
    return (f(x + h) - f(x)) / h

# Fungsi f(x) = 5 - 5x - e^(0.5*x)
def f(x):
    return 5-(5*x)-math.exp(0.5*x)              

#Secant Method x(i+1) = xi - f(xi)(xi-1 - xi)/ f(xi-1)-f(xi)
def f2(x0, x1):
    x2 = x1 - (f(x1)*(x0-x1))/(f(x0)-f(x1))
    return x2

#Fungsi Untuk Secant Method
def SecantMethod(x0, x1, es):
    print('='*35)
    print(f"|{'i':^5}|{'xi':^11}|{'ea(%)':^15}|")
    print('='*35)
    iter = 0
    while True:
        x2 = f2(x0, x1)
        if iter == 0:
            ea = ""
        elif iter != 0:
            ea = abs((x2-x1)/x2)*100
            ea = round(ea,7)
        print(f"|{iter:^5}|{x2:^11.7f}|{ea:^15}|")
        x0 = x1
        x1 = x2
        iter +=1
        if iter == 1:
            continue
        if iter != 0 and ea <= es:
            break
    print('='*35)   

x0 = float(input("Enter the value of x-1: "))
x1 = float(input("Enter the value of x0: "))
es = float(input("Enter the approximate error (ea): "))
SecantMethod(x0, x1, es)