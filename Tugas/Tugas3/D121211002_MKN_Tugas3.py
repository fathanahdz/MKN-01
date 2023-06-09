#Nurunnisa Fathanah Dz. S. B.
#D121211002
#Metode Komputasi Numerik 
#Kelas A
#Tugas 3

#Mengimport modul math untuk menggunakan fungsi exponensialnya
import math                                     

#Fungsi untuk f'(x)
def faksen(f, x):                               
    h = 1e-6  
    return (f(x + h) - f(x)) / h

# Fungsi f(x) = 5 - 5x - e^(0.5*x)
def f(x):
    return 5-(5*x)-math.exp(0.5*x)              

#Newton Raphson x(i+1) = xi - f(x)/f'(x)
def f1(x):
    x1 = x - (f(x))/(faksen(f,x))
    return x1

#Secant Method x(i+1) = xi - f(xi)(xi-1 - xi)/ f(xi-1)-f(xi)
def f2(x0, x1):
    x2 = x1 - (f(x1)*(x0-x1))/(f(x0)-f(x1))
    return x2

#Fungsi Bisection Method
def BisectionMethod(xl, xu, es, fxl, fxu):
    print('='*89)
    print(f"|{'Iteration':^11}|{'xl':^10}|{'fxl':^10}|{'xu':^10}|{'fxu':^10}|{'xr':^10}|{'fxr':^10}|{'ea (%)':^10}|")
    print('='*89)
    xr = (xl+xu)/2
    iter = 0
    while True:
        xrold = xr
        xr = (xl+xu)/2                              #Menghitung nilai xr
        iter = iter + 1
        if iter == 1:
            ea = ""
        elif xr != 0:
            ea = abs((xr-xrold)/xr)*100
            ea = round(ea,7)
        fxl = f(xl)
        fxu = f(xu) 
        fxr = f(xr)                                 #Menghitung nilai fxl
        print(f"|{iter:^11}|{xl:^10.5f}|{fxl:^10.5f}|{xu:^10.5f}|{fxu:^10.5f}|{xr:^10.5f}|{fxr:^10.5f}|{ea:^10}|")
        test = fxl*fxr                              #Untuk menghitung nilai dari fxl apakah positif atau negatif untuk bisa menggantikan xl atau xu
        if test < 0:                                #Jika test < 0 maka xl akan diganti dengan xr
            xu = xr
        elif test > 0:                              #Jika test > 0 maka xu akan diganti dengan xr
            xl = xr
        else:                                       #Jika test = 0 maka error approximate = 0
            ea = 0
        if iter != 1 and ea <= es:
            break
    print('='*89)
    print(f"The root is {xr:7f}\n")    

#Fungsi untuk NewtonRaphsonMethod
def NewtonRaphsonMethod(x0, es):
    print('='*35)
    print(f"|{'i':^5}|{'xi':^11}|{'ea(%)':^15}|")
    print('='*35)
    iter = 0
    x1 = x0
    while True:
        if iter == 0:
            ea = ""
        elif iter != 0:
            ea = abs((x1-x0)/x1)*100
            ea = round(ea,7)
        print(f"|{iter:^5}|{x1:^11.7f}|{ea:^15}|")
        x0 = x1
        x1 = f1(x0)
        iter +=1
        if iter == 1:
            continue
        if iter != 0 and ea <= es:
            break
    print('='*35) 
    print(f"The root is {x1:7f}\n")    


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
    print(f"The root is {x2:7f}\n")    

def Menu():
    while True:
        print("Choose the method you want to use:")
        print("1. Bisection Method")
        print("2. Newton Raphson Method")
        print("3. Secant Method")
        print("4. Exit\n")
        try:
            choice = int(input("Your choice: "))
            if choice == 1:
                xl = float(input("Enter the value of xl (lower bound): "))
                xu = float(input("Enter the value of xu (upper bound): "))
                es = float(input("Enter the approximate error (ea): "))
                fxl = f(xl)
                fxu = f(xu)
                xr = BisectionMethod(xl, xu, es, fxl, fxu)
            elif choice == 2:
                x0 = float(input("Enter the value of xi: "))
                es = float(input("Enter the approximate error (ea): "))
                NewtonRaphsonMethod(x0, es)
            elif choice == 3:
                x0 = float(input("Enter the value of x(i-1): "))
                x1 = float(input("Enter the value of xi: "))
                es = float(input("Enter the approximate error (ea): "))
                SecantMethod(x0, x1, es)
            elif choice == 4:
                print("\n- ^o^ - Thank you for using this program - ^o^ -\n")
                break
            else:
                print("\nInvalid Input. Please enter the right input.\n")
        except ValueError:
            print("\nInvalid Input. Please enter the right input\n")

Menu()