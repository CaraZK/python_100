def factorial(num):
    result = 1
    for x in range(1, num + 1):  # not in
        result = result * x
    return result

m = 7  # int(input("m:"))
n = 3  # int(input("n:"))
print(factorial(m) // factorial(n) // factorial(m - n))

import random

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += random.randint(1, 7)
    return total

def add(a=0, b=0, c=0):
    return a + b +2* c

print(roll_dice(8))
print(add(c=3))

print("**********************************************")
from module1 import foo
from module2 import foo

import module2 as mo2
import module1 as mo1
mo1.foo()
mo2.foo()
