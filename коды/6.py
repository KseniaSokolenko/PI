with open('input.txt', 'a+') as f:
    f.write('\nA quote from a book')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)