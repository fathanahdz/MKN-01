import math

def f(x):
    return 5-(5*x)-math.exp(0.5*x) 

def FalsePositionMethod(xl, xu, es, fxl, fxu,):
    print('='*89)
    print(f"|{'Iteration':^11}|{'xl':^10}|{'fxl':^10}|{'xu':^10}|{'fxu':^10}|{'xr':^10}|{'fxr':^10}|{'ea (%)':^10}|")
    print('='*89)
    xr = xu - ((fxu*(xl-xu)))/(fxl-fxu)             #Menghitung ilai xr
    iter = 0
    while True:
        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)
        xrold = xr
        xr = xu - (fxu*(xl-xu))/(fxl-fxu)         #Menghitung ilai xr
        iter = iter + 1
        if iter == 1:
            ea = ""
        elif xr != 0:
            ea = abs((xr-xrold)/xr)*100
            ea = round(ea,7)
        print(f"|{iter:^11}|{xl:^10.3f}|{fxl:^10.3f}|{xu:^10.3f}|{fxu:^10.3f}|{xr:^10.3f}|{fxr:^10.3f}|{ea:^10}|")
        test = fxl*fxr
        if test < 0:
            xu = xr
        elif test > 0:
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
FalsePositionMethod(xl,xu,es,fxl,fxu)