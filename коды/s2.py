def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            if not data:
                raise ValueError("Файл пустой")
            return data
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(e)

# Проверим оба файла
print("Проверка empty.txt:")
result = read_file('empty.txt')
if result is not None:
    print(result)

print("\nПроверка not_empty.txt:")
result = read_file('not_empty.txt')
if result is not None:
    print(result)