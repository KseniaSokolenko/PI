def remover(tup, value):
    if value in tup:
        return tuple(i for i in tup if i != value)
    else:
        return tup

print(remover((1, 2, 3), 1))
print(remover((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remover((2, 4, 6, 6, 4, 2), 9))
