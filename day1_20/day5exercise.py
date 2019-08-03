import math
import random

# 水仙花数
for x in range(100, 999):
    s = 0
    temp = x  # 记录没被修改前的数
    while x != 0:
        i = x % 10
        s = i ** 3 + s  # ** //
        x = int(x / 10)
    if s == temp:
        print(temp)
print('*******************************************************')
# 完美数
for x in range(1, 1000):
    sum = 0
    end = int(math.sqrt(x))
    for y in range(2, end + 1):
        if x % y == 0:
            sum = sum + y + int(x / y)  # 写算法步骤，再实现比如，漏掉了思路
    sum = sum + 1
    if sum == x:
        print(x)
print('*******************************************************')
# 100钱 100鸡 5 3 3
for x in range(0, 20):
    for y in range(0, 33):
        z = 3 * (100 - 5 * x - 3 * y)
        # print("x=%d,y=%d,z=%d" % (x, y, z))   忘记range了我靠
        if x + y + z == 100:
            print("x=%d,y=%d,z=%d" % (x, y, z))
print('*******************************************************')
# 斐波那契
temp1 = 1
temp2 = 1
for x in range(1, 10):
    temp = temp1 + temp2
    print(temp)
    temp1 = temp2
    temp2 = temp
print('*******************************************************')
# Craps赌博
first = random.randint(1, 6) + random.randint(1, 6)
print(first)
if first == 7 or first == 11:
    print('win')
elif first == 2 or first == 3 or first == 12:
    print('lose')
else:
    while True:
        temp = random.randint(1, 6) + random.randint(1, 6)
        print('temp:%d' % (temp))
        if temp == 7:
            print('lose')
            break
        elif temp == first:
            print('win')
            break
