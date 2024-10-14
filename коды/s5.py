def list(lst):
    negative, zero, positive = [], [], []
    for x in lst:
        if x > 0:
            positive.append(x)
        elif x < 0:
            negative.append(x)
        else:
            zero.append(x)
    return negative + zero + positive


def main():

    lst = list(map(int, input("Введите список чисел через пробел: ").split()))

    result = list(lst)

    cortesh = tuple(result)
    print(cortesh)


if __name__ == "__main__":
    main()
