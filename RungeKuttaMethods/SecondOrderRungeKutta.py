import math

#rumus theta = fungsi (x,y)
#rumus untuk k1
def f(xi,yi):
    result = (1+2*xi)* math.sqrt(yi)
    return result

#rumus analitik
def yexact(xi,yi):
    result = math.sqrt(yi) * xi + math.sqrt(yi) * math.pow(xi,2) + 1
    return result

#rumus k2
def k2(xi,yi,h):
    k1 = f(xi,yi)
    result = f(xi + h/2, yi + k1*h/2)
    return result


#rumus Midpoint /yi+1 untuk Second Order Runge Kutta
def yiPlusOne(xi,yi,h):
    result = yi + k2(xi,yi,h)*h
    return result

def SecondOrderRungeKutta(xi,xEnd,yi,h):
    print('='*34)
    print(f"|{'xi':^10}|{'ymidpoint':^10}|{'ytrue':^10}|")
    print('='*34)
    ymidpoint = 1

    while xi <= xEnd:
        print(f"|{xi:^10.7f}|{ymidpoint:^10.7f}|{yexact(xi,yi):^10.7f}|")
        yi = ymidpoint
        ymidpoint = yiPlusOne(xi,yi,h)
        xi = xi + h
    print('='*34)
    
xi=float(input("Please input the starting value of x: "))
xEnd=float(input("Please input the ending value of x: "))
h=float(input("Please input the step size: "))
yi=float(input("Please input the initial condition at xi, yi: "))
print("\nThird Order Runge Kutta Methods (Midpoint Method)")
SecondOrderRungeKutta(xi,xEnd,yi,h)