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

x0 = float(input("Enter the initial guess: "))
es = float(input("Enter the approximate error: "))
maxIter = int(input("Enter the maximum iteration: "))
NewtonRaphsonMethod(x0,es,maxIter)
