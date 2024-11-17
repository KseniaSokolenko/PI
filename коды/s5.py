class InvalidOperationError(Exception):

    def __init__(self, message="Недопустимая операция"):
        super().__init__(message)

def divide_numbers(a, b):
    if b == 0:
        raise InvalidOperationError("Деление на ноль недопустимо")
    return a / b

# Пример использования функции
try:
    result = divide_numbers(10, 0)
except InvalidOperationError as e:
    print(f"Произошла ошибка: {e}")
else:
    print(result)