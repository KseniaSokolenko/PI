with open('s5.txt', 'r') as file:
    lines = file.readlines()

content = ' '.join(lines)
words = content.split()

first_word = words[0]
last_word = words[-1]

print(first_word)
print(last_word)