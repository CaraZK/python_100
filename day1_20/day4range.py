from math import sqrt
import random

sum = 0
for x in range(1, 100, 3):
    # print("the %d bu: %d" % (int((x - 1) / 3), x))
    sum += x
print("sum is:%d" % sum)

# guess number
answer = 43
counter = 0
small = 1;
big = 100;
while True:
    counter += 1
    num = random.randint(small, big)
    print(num)
    if num == answer:
        print("you used %d times to guess the number %d" % (counter, num))
        break
    elif num > answer:
        big = num
    else:
        small = num

    # Is it a su number?
    num = int(input("please input a number:"))
    end = int(sqrt(num))
    is_Prime = False
    for x in (2, end + 1):
        if (num % x == 0):
            is_Prime = True
            break
    if (is_Prime and num != 1):
        print("not prime")
    else:
        print("is Prime")
