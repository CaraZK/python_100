import sys
import random


def main1():
    f = [x for x in range(1, 10)]
    print(f)
    g = [x + y for x in 'ABCDEF' for y in '1234567']
    print(g)
    h = [x ** 2 for x in range(1, 100)]
    print(sys.getsizeof(h))


# exercise1 跑马灯

import os
import time


def main2():
    content = '我有一只小毛驴，我从来也不骑'
    while True:
        # os.system('cls')
        time.sleep(0.2)
        print(content)
        content = content[1:] + content[0]


def main3():
    list = [0, 1, 2, 3, 4]
    print(list[-5])


def main4():
    #  tuple=(1,2,3,e,r)
    codes = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lenth = len(codes) - 1
    codenew = ''
    for _ in range(6):
        num = random.randint(0, lenth)
        codenew += codes[num]
    return codenew


print(main4())


def main5():
    people = [True] * 30
  #  print(people)
    counter = 0
    index = 0
    num = 0
    while counter < 15:
        if people[index]:
            num += 1
        if num == 9:
            people[index] = False
            counter += 1
            num = 0
        index += 1
        index %= 30
    print(people)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)



if __name__ == '__main__':
    main5()
