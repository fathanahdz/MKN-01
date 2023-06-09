import math

#rumus theta = fungsi (x,y)
def f(xi,yi):
    return -2*pow(xi,3)+12*pow(xi,2)-20*xi+8.5

#rumus analitik
def yexact(xi,yi):
    return -1/2*pow(xi,4)+4*pow(xi,3)-10*pow(xi,2)+8.5*xi+1

#rumus euler / yi+1 First Order Runge Kutta
def yiPlusOne(xi,yi,h):
    return yi + f(xi,yi)*h

def FirstOrderRungeKutta(xi,xEnd,yi,h):
    print('='*34)
    print(f"|{'xi':^10}|{'yeuler':^10}|{'ytrue':^10}|")
    print('='*34)
    yeuler = 1

    while xi <= xEnd:
        print(f"|{xi:^10.7f}|{yeuler:^10.7f}|{yexact(xi,yi):^10.7f}|")
        yi = yeuler
        yeuler = yiPlusOne(xi,yi,h)
        xi = xi + h
    print('='*34)
    
xi=float(input("Please input the starting value of x: "))
xEnd=float(input("Please input the ending value of x: "))
h=float(input("Please input the step size: "))
yi=float(input("Please input the initial condition at xi, yi: "))
print("\nFirst Order Runge Kutta Methods (Euler's Method)")
FirstOrderRungeKutta(xi,xEnd,yi,h)