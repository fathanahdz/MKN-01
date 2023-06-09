import math

def f(x):
    return 5-(5*x)-math.exp(0.5*x) 
def g(x):
    return (5-math.exp(0.5*x))/5

def SimpleFixedPointIteration(x0, es, maxIter):
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
        x1 = g(x0)
        iter +=1
        if iter == 1:
            continue
        if (iter !=0 and iter ==  maxIter+1) or (iter != 0 and ea <= es):
            break
    print('='*35)

x0 = float(input("Enter the initial guess: "))
es = float(input("Enter the approximate error: "))
maxIter = int(input("Enter the maximum iteration: "))
SimpleFixedPointIteration(x0,es,maxIter)
