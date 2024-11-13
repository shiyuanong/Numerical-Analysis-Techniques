## Lab code

import math

# a = 1
# b = 2
# max = 1000
# tol = 10**(-8)
# 
# def f(x):
#     return x**2 - 2
# 
# error = b - a
# 
# fa=f(a)
# fb=f(b)
# 
# for n in range (1,max):
#     error = error / 2
#     c = (a+b)/2
#     fc = f(c)
# 
#     if error < tol:
#         print('convergence')
#         break
# 
#     #write the conditionals for checking the intervals
#     if fa*fc < 0:
#         b = c
#     else:
#         a = c
# 
# 
# print(c)

## Question 1

# a = 1
# b = 5
# max = 1000
# tol = 10**(-8)
# 
# error = b - a
# 
# 
# 
# def f(x):
#     return x**3 - x**2 - (2*x) +1
# 
# fa = f(a)
# fb = f(b)
# 
# for n in range (1,max):
#     error = error / 2
#     c = (a+b)/2
#     fc = f(c)
# 
#     if error < tol:
#         print("convergence")
#         break
# 
#     if fa*fc < 0:
#         b = c
#     else:
#         a = c
# 
# 
# print(c)


##Question 2 

# a = 0
# b = 1
# max = 1000
# tol = 10**(-8)
# 
# error = b - a
# 
# def f(x):
#     return (9 * (x**4)) +(18 * (x**3)) + (38 *(x**2)) - (57 * x) + 14
# 
# fa = f(a)
# fb = f(b)
# 
# for n in range (1,max):
#     error = error / 2
#     c = (a+b)/2
#     fc = f(c)
# 
#     if error < tol:
#         print('convergence')
#         break
# 
#     if fa*fc < 0:
#         b = c
#     else:
#         a = c
#
# print(c)


##Question 3

# a = 4
# b = 5
# max = 1000
# tol = 10**(-8)
# 
# error = b - a
# 
# def f(x):
#     return math.tan(x) - x
# 
# fa = f(a)
# fb = f(b)
# 
# for n in range (1,max):
#     error = error / 2
#     c = (a+b)/2
#     fc = f(c)
# 
#     if error < tol:
#         print('convergence')
#         break
# 
#     if fa*fc < 0:
#         b = c
#     else:
#         a = c
# 
# print(c)
# 
# 
## on interval [1,2]

# a = 1
# b = 2
# max = 1000
# tol = 10**(-8)
# 
# error = b - a
# 
# fa = f(a)
# fb = f(b)
# 
# for n in range (1,max):
#     error = error / 2
#     c = (a+b)/2
#     fc = f(c)
# 
#     if error < tol:
#         print('convergence')
#         break
# 
#     if fa*fc < 0:
#         b = c
#     else:
#         a = c
# 
# print(c)


#Question 4
a = 4
b = 5
max = 1000
tol = 10**(-4)

error = b - a

def f(x):
    return math.tan(x)-x

fa = f(a)
fb = f(b)

for n in range (1,max):
    error = error / 2
    c = (a+b)/2
    fc = f(c)

    if error < tol:
        print('convergence')
        break

    if fa*fc < 0:
        b = c
    else:
        a = c

print(c)


