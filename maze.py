import math
def factorial(n):
    if n < 0:
        return "factorial is not defined for negative number"
    elif n==0 or n==1:
        return 1
    else:
        return n* factorial(n - 1)
def gcd(a,b):
    while b:
        a,b = b,a%b
        return a
