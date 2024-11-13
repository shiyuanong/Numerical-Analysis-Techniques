#Question 1
import math

# x = [8]
# tol = 10**(-10)
# nmax = 10000
# error = []
# 
# 
# def f(x):
#     return math.tan(x) - x
# 
# def fp(x):
#     return (1 / math.cos(x))**2 - 1
# 
# for i in range (0,nmax):
#     fx = f(x[i])
#     fpx = fp(x[i])
#     d = fx/fpx
#     x.append(x[i]-d)
# 
#     error.append(d)
# 
#     print (f(x[i]))
#     if abs(d) < tol:
#         print("Convergence")
#         print (x)
#         break

# nmax = 10000
# tol = 10**(-10)
# x = [2]
# error = []

# def f(x):
#     return math.exp(x) - math.sqrt((x+9))

# def fp(x):
#     return math.exp(x) - (0.5 * (1/math.sqrt(x+9)))

# for i in range(nmax):
#     fx = f(x[i])
#     fpx = fp(x[i])
#     d = fx / fpx
#     x.append(x[i]-d)
#     error.append(d)

#     print(f(x[i]))

#     if abs(d) < tol:
#         print("Convergence")
#         print(x)
#         break


##Question 4

# x = [0.6]
# tol = 10**(-11)
# max = 1000

# def f(x):
#     return (2*x - 2*(x**3) + 2*(x**2))*math.log(x) - x**2 + 1

# def fp(x):
#     return -2*(x-1)*((3*x + 1)*math.log(x) +x + 1)

# for i in range(max):
#     fa = f(x[i])
#     fpa = fp(x[i])
#     d = fa/fpa
#     x.append(x[i]-d)
    
#     print(x[i])

#     if abs(d) < tol:
#         print('convergence')
#         break





##Question 8
# x = [1.8]
# max = 1000
# tol = 10**(-11)

# def f(x) :
#     return x**3-x**2-x-1

# def fp(x):
#     return 3*(x**2) - 2*(x)-1

# for i in range(max):
#     fx = f(x[i])
#     fpx = fp(x[i])
#     d = fx/fpx
#     x.append(x[i] - d)

#     print(x[i])

#     if abs(d) < tol:
#         print('convergence')
#         break


##Question 9 
# x = [0.5]  
# tol = 10**(-10)
# nmax = 1000

# def f(x):
#     return 5 * (3 * x**4 - 6 * x**2 + 1) - 2 * (3 * x**5 - 5 * x**3)

# def fp(x):
#     return 5 * (12 * x**3 - 12 * x) - 2 * (15 * x**4 - 15 * x**2)

# for i in range(nmax):
#     fx = f(x[i])
#     fpx = fp(x[i])
#     d = fx / fpx
#     x.append(x[i] - d)

#     print(x[i])

#     if abs(d) < tol:
#         print('Convergence')
#         print(x)
#         break


##Questoin 14 

