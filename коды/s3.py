def sum():
    while True:
        user_input = input("Введите число: ")

        # Проверка ввода с помощью try/except
        try:
            number = float(user_input)
        except ValueError as e:
            print(f"Неподходящий тип данных. Ожидалось число. {e}")
            continue

        result = 2 + number
        print(f"Результат сложения: ", result)

if __name__ == '__main__':
    sum()

