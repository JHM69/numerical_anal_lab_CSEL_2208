import math

def f(x):
    return x*x*x + x*x -1
# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1/math.sqrt(1+x)
# 1st Derivative of f(x)
def f1(x):
    return 3*x*x + 2*x*x

def bysection(a, b, tol, N):
    false_position
    c = (a+b)/2
    step = 1
    while abs(f(c)) > tol and step<=N:
        c = (a+b)/2
        print('Iteration: %d , c: %6f , f(c):  %6f ' % (step,c,f(c)))
        step = step + 1
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
    print('Root is : %8f' % c)


def false_position(a, b, tol, N):
    print('\n\n*** False Position ***')
    c = ( a * f(b) - b * f(a) ) / ( f(b) - f(a) )
    step = 1
    while abs(f(c)) > tol and step<=N:
        c = ( a * f(b) - b * f(a) ) / ( f(b) - f(a) )
        print('Iteration: %d , c: %6f , f(c):  %6f ' % (step,c,f(c)))
        step = step + 1
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
    print('Root is : %8f' % c)

    
def fixed_point_iteration(x0, tol, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    x1 = g(x0)
    while abs(f(x1)) > tol:
        x1 = g(x0)
        print('Iteration-%d , x1 = %0.6f , f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        if step > N:
            flag=0
            break
        
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


def neuton_rafsan(x0, tol, N):
    print('\n\n*** Neuton Rafsan ITERATION ***')
    step = 1
    flag = 1
    x1 = g(x0)
    while abs(f(x1)) > tol:
        x1 =  x0 - f(x0)/f1(x0)
        print('Iteration: %d , x1: %0.6f , f(x1): %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        if step > N:
            flag=0
            break
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

a = -3
b = 4
tol = 1e-2
step = 50
if f(a) * f(b) > 0:
    print('Wrong Guess')
else:
    bysection(a, b, tol, step)   
    false_position(a, b, tol, step)     
fixed_point_iteration(2, 0.00001, step)
neuton_rafsan(2, 0.00001, step)