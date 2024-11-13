#Use the secant method on p(x) = x^5 + x^3 + 3 with x0 
import math

# Secant Method for p(x) = x^5 + x^3 + 3
# Function: p(x) = x^5 + x^3 + 3

# max = 1000
# a = -1
# b = 1
# tol = 10**(-8)

# def f(x):
#     return x**(5) + x**(3) + 3


# fa = f(a)
# fb = f(b)

# for i in range (2,max):
#     d = (b-a)/(fb-fa)
#     d = d*fa
#     c = a - d

#     print (i, ":",c)
#     if abs(d) < tol:
#         print('convergence')
#         break

#     b = a
#     fb = fa
#     a = c
#     fa = f(a)


# -------------------------------------------------------

# Secant Method for f(x) = e^x - 3x^2
# Function: f(x) = e^x - 3 * x^2
# max = 1000
# a = 3.5
# b = 4.5

# def f(x):
#     return math.exp(x) - 3*(x**2)

# fa = f(a)
# fb = f(b)
# tol = 10**(-8)

# for i in range (2,1000):
#     d = (b-a) / (fb - fa)
#     d = d*f(a)
#     c = a - d
#     print(c)

#     if (d < tol):
#         print ("Convergence")
#         break

#     b = a
#     fb = fa 
#     a = c
#     fc = f(a)




