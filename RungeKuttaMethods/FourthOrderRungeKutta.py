import math

#rumus theta = fungsi (x,y)
#rumus untuk k1
def f(xi,yi):
    result = -2*pow(xi,3)+12*pow(xi,2)-20*xi+8.5
    return result

#rumus analitik
def yexact(xi,yi):
    result = -1/2*pow(xi,4)+4*pow(xi,3)-10*pow(xi,2)+8.5*xi+1
    return result

#rumus k2
def k2(xi,yi,h):
    k1 = f(xi,yi)
    result = f(xi + h/2, yi + k1*h/2)
    return result

def k3(xi,yi,h):
    k1 = f(xi,yi)
    result = f(xi + h/2, yi + k1*h + k2(xi,yi,h)*h/2)
    return result

def k4(xi,yi,h):
    result = f(xi + h, yi + k3(xi,yi,h)*h)
    return result

#rumus yi+1 untuk Fourth Order Runge Kutta
def yiPlusOne(xi,yi,h):
    k1 = f(xi,yi)
    result = yi + 1/6*(k1+2*k2(xi,yi,h)+2*k3(xi,yi,h)+k4(xi,yi,h))*h
    return result

def FourthOrderRungeKutta(xi,xEnd,yi,h):
    print('='*34)
    print(f"|{'xi':^10}|{'yi':^10}|{'ytrue':^10}|")
    print('='*34)
    yNew = 1

    while xi <= xEnd:
        print(f"|{xi:^10.7f}|{yNew:^10.7f}|{yexact(xi,yi):^10.7f}|")
        yi = yNew
        yNew = yiPlusOne(xi,yi,h)
        xi = xi + h
    print('='*34)
    
xi=float(input("Please input the starting value of x: "))
xEnd=float(input("Please input the ending value of x: "))
h=float(input("Please input the step size: "))
yi=float(input("Please input the initial condition at xi, yi: "))
print("\n Fourth Order Runge Kutta Methods")
FourthOrderRungeKutta(xi,xEnd,yi,h)