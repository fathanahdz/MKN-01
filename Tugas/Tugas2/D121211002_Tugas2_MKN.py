# Nurunnisa Fathanah Dz. S. B.
# D121211002
# Kelas A

import math

#Untuk menghitung nilai dari fungsi             
def f(m, vt, g, c, t):                          
    value = ((g*m)/c)*(1-math.exp(-c/m*t))-vt
    return value

#Menu Awal mengenai apa yang ingin dihitung
def Menu1():
    print("\nParachutist Case")
    print("\nPlease choose what you want to calculate: ")
    print("1. Mass (m)")
    print("2. Drag Coefficient (c)")
    print("3. Velocity (vt)")
    print("4. Time (t)")
    print("5. Exit")
    while True:
        menu1 = int(input("\nYour choice: \n"))
        if menu1 not in [1, 2, 3, 4, 5]:
            print("Incorrect input.")
        else:
            break
    return menu1

#Menu kedua mengenai metode apa yang ingin digunakan
def Menu2():
    print("\nPlease choose what method you want to use: ")
    print("1. Bisection Method")
    print("2. False-Position Method")
    print("3. Bisection and False-Position Method")
    while True:
        menu2 = int(input("\nYour choice: \n"))
        if menu2 not in [1, 2, 3]:
            print("Incorrect input.")
        else:
            break
    return menu2

#Untuk menghitung nilai dari metode Bisection
def BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, m, vt,c):
    print('='*89)
    print(f"|{'Iteration':^11}|{'xl':^10}|{'fxl':^10}|{'xu':^10}|{'fxu':^10}|{'xr':^10}|{'fxr':^10}|{'ea':^10}|")
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
            ea = round(ea,3)
        if menu1 == 1:                              #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari mass
            fxl = f(xl, vt, g, c, t)
            fxu = f(xu, vt, g, c, t)
            fxr = f(xr, vt, g, c, t)
        elif menu1 == 2:                            #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari drag coefficient
            fxl = f(m, vt, g, xl, t)
            fxu = f(m, vt, g, xu, t)
            fxr = f(m, vt, g, xr, t)
        elif menu1 == 3:                            #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari velocity
            fxl = f(m, xl, g, c, t)
            fxu = f(m, xu, g, c, t)
            fxr = f(m, xr, g, c, t)
        elif menu1 == 4:                            #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari velocity
            fxl = f(m, vt, g, c, xl)
            fxu = f(m, vt, g, c, xu)
            fxr = f(m, vt, g, c, xr)
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

def FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, m, vt,c):
    print('='*89)
    print(f"|{'Iteration':^11}|{'xl':^10}|{'fxl':^10}|{'xu':^10}|{'fxu':^10}|{'xr':^10}|{'fxr':^10}|{'ea':^10}|")
    print('='*89)
    xr = xu - ((fxu*(xl-xu)))/(fxl-fxu)             #Menghitung ilai xr
    iter = 0
    while True:
        if menu1 == 1:                              #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari mass
            fxl = f(xl, vt, g, c, t)
            fxu = f(xu, vt, g, c, t)
            fxr = f(xr, vt, g, c, t)
        elif menu1 == 2:                            #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari drag coefficient
            fxl = f(m, vt, g, xl, t)
            fxu = f(m, vt, g, xu, t)
            fxr = f(m, vt, g, xr, t)
        elif menu1 == 3:                            #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari velocity
            fxl = f(m, xl, g, c, t)
            fxu = f(m, xu, g, c, t)
            fxr = f(m, xr, g, c, t)
        elif menu1 == 4:                            #Menghitung nilai dari fxl, fxu, dan fxr untuk mencari velocity
            fxl = f(m, vt, g, c, xl)
            fxu = f(m, vt, g, c, xu)
            fxr = f(m, vt, g, c, xr)
        xrold = xr
        xr = xu - (fxu*(xl-xu))/(fxl-fxu)         #Menghitung ilai xr
        iter = iter + 1
        if iter == 1:
            ea = ""
        elif xr != 0:
            ea = abs((xr-xrold)/xr)*100
            ea = round(ea,3)
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
#Main Program
while True:
    menu1 = Menu1()
    g = 9.8

    #Jika user memilih untuk menghitung massa
    if menu1 == 1:
        vt  = float(input("\nPlease input the velocity (vt): "))
        t   = float(input("\nPlease input the time (t): "))
        c   = float(input("\nPlease input the drag coefficient (c): "))
        es  = float(input("\nPlease input the approximate error (es): "))
        while True:
            xl  = float(input("\nPlease input the lower bound (xl): "))
            xu  = float(input("\nPlease input the upper bound (xu): "))
            fxl = f(xl, vt, g, c, t) 
            fxu = f(xu, vt, g, c, t)
            if fxl*fxu > 0:
                print("Given guess values do not bracket the root.")
            else:
                break
        
    #Jika user memilih untuk menghitung drag coefficient
    elif menu1 == 2:
        m   = float(input("\nPlease input the mass (m): "))
        vt  = float(input("\nPlease input the velocity (vt): "))
        t   = float(input("\nPlease input the time (t): "))
        es  = float(input("\nPlease input the approximate error (es): "))
        while True:
            xl  = float(input("\nPlease input the lower bound (xl): "))
            xu  = float(input("\nPlease input the upper bound (xu): "))
            fxl = f(m, vt, g, xl, t) 
            fxu = f(m, vt, g, xu, t)
            if fxl*fxu > 0:
                print("Given guess values do not bracket the root.")
            else:
                break   
                
    #Jika user memilih untuk menghitung velocity    
    elif menu1 == 3:
        m   = float(input("\nPlease input the mass (m): "))
        t   = float(input("\nPlease input the time (t): "))
        c   = float(input("\nPlease input the drag coefficient (c): "))
        es  = float(input("\nPlease input the approximate error (es): "))
        xl  = float(input("\nPlease input the lower bound (xl): "))
        xu  = float(input("\nPlease input the upper bound (xu): "))
        while True:
            xl  = float(input("\nPlease input the lower bound (xl): "))
            xu  = float(input("\nPlease input the upper bound (xu): "))
            fxl = f(m, xl, g, c, t) 
            fxu = f(m, xu, g, c, t)
            if fxl*fxu > 0:
                print("Given guess values do not bracket the root.")
            else:
                break

    #Jika user memilih untuk menghitung time    
    elif menu1 == 4:
        m   = float(input("\nPlease input the mass (m): "))
        vt  = float(input("\nPlease input the velocity (vt): "))
        c   = float(input("\nPlease input the drag coefficient (c): "))
        es  = float(input("\nPlease input the approximate error (es): "))
        xl  = float(input("\nPlease input the lower bound (xl): "))
        xu  = float(input("\nPlease input the upper bound (xu): "))
        while True:
            xl  = float(input("\nPlease input the lower bound (xl): "))
            xu  = float(input("\nPlease input the upper bound (xu): "))
            fxl = f(m, vt, g, c, xl) 
            fxu = f(m, vt, g, c, xu)
            if fxl*fxu > 0:
                print("Given guess values do not bracket the root.")
            else:
                break
    #Jika user memilih untuk keluar
    elif menu1 == 5:
        break

    menu2 = Menu2()
    if menu2 == 1 and menu1 == 1:
        print("\nCompute Mass with Bisection Method")
        m = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, 0, vt,c)
        print(f'So, mass of parachutist is {m:.3f}')
    elif menu2 == 1 and menu1 == 2:
        print("\nCompute Drag Coefficient with Bisection Method")
        c = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, m, vt, 0)
        print(f'So, drag coefficient is {c:.3f}')
    elif menu2 == 1 and menu1 == 3:
        print("\nCompute Velocity with Bisection Method")
        vt = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, m, 0, c)
        print(f'So, the velocity is {vt:.3f}')
    elif menu2 == 1 and menu1 == 4:
        print("\nCompute Time with Bisection Method")
        t = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, 0, m, vt, c)
        print(f'So, the time is {t}')

    elif menu2 == 2 and menu1 == 1:
        print("\nCompute Mass with False-Position Method")
        FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, 0, vt,c)
        m = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, 0, vt,c)
        print(f'So, mass of parachutist is {m:.3f}')
    elif menu2 == 2 and menu1 == 2:
        print("\nCompute Drag Coefficient with False-Position Method")
        c = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, m, vt, 0)
        print(f'So, drag coefficient is {c:.3f}')
    elif menu2 == 2 and menu1 == 3:
        print("\nCompute Velocity with False-Position Method")    
        vt = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, m, 0, c)
        print(f'So, the velocity {vt:.3f}')
    elif menu2 == 2 and menu1 == 4:
        print("\nCompute Time with Bisection Method")
        t = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, 0, m, vt, c)
        print(f'So, the time is {t}')


    elif menu2 == 3 and menu1 == 1:
        print("\nCompute Mass with Bisection Method")
        m = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, 0, vt,c)
        print(f'So, mass of parachutist is {m:.3f}')        
        print("\nCompute Mass with False-Position Method")
        m = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, 0, vt,c)
        print(f'So, mass of parachutist is {m:.3f}')
    elif menu2 == 3 and menu1 == 2:
        print("\nCompute Drag Coefficient with Bisection Method")  
        c = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, m, vt,0)
        print(f'So, drag coefficient is {c:.3f}')
        print("\nCompute Drag Coefficient with False-Position Method")
        c = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, m, vt, 0)
        print(f'So, drag coefficient is {c:.3f}')
    elif menu2 == 3 and menu1 == 3:
        print("\nCompute Velocity with Bisection Method")
        vt = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, t, m, 0,c)
        print(f'So, mass of parachutist is {vt:.3f}')
        print("\nCompute Velocity with False-Position Method")
        vt = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, t, m, 0, c)
        print(f'So, mass of parachutist is {vt:.3f}')
    elif menu2 == 1 and menu1 == 4:
        print("\nCompute Time with Bisection Method")
        t = BisectionMethod(xl, xu, es, fxl, fxu, menu1, g, 0, m, vt, c)
        print(f'So, the time is {t}')
        print("\nCompute Time with Bisection Method")
        t = FalsePosition(xl, xu, es, fxl, fxu, menu1, g, 0, m, vt, c)
        print(f'So, the time is {t}')
    print("\n")

    while True:
        rep = input("Want to calculate again? (y/n): ")
        if rep != 'y' and rep !='Y' and rep!='n' and rep !='N':
            print("Error Input, Please input y/n.")
        else:
            break
    if rep == 'Y' or rep == 'y':
        pass
    elif rep == 'N' or rep == 'n':
        break
print("End of Program\n")