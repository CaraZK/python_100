def josephus1():
    peo = [True] * 30
    counter, num, index = 0, 1, 0
    while counter < 15:
        if peo[index]:
            num += 1
            if num == 9:
                peo[index] = False
                num = 1
                counter += 1
        index += 1
        index %= 30
    print(peo)
    peo_index = [0] * 30
    j = 0
    for i in range(30):
        if peo[i]:
            peo_index[j] = i
            j += 1
    print(peo_index)


def josephus2():
    people = [True] * 30
    index, num, counter = 0, 1, 0
    while counter < 15:
        if num < 9:
            if people[index]:
                num += 1
        elif num == 9:
            if people[index]:
                people[index] = False
                num = 1
                counter += 1
        index += 1
        index %= 30
    peo_index = [0] * 30
    j = 0
    for i in range(30):
        if people[i]:
            peo_index[j] = i
            j += 1
    print(peo_index)


if __name__ == '__main__':
    josephus2()
