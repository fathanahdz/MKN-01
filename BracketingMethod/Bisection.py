import math

def f(x):
    return 5-(5*x)-math.exp(0.5*x) 

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
    return xr

xl = float(input("Enter the lower bound: "))
xu = float(input("Enter the upper bound: "))
es = float(input("Enter the approximate error: "))
fxl = f(xl)
fxu = f(xu)
BisectionMethod(xl,xu,es,fxl,fxu)