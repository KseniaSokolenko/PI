import time
# Декоратор для измерения времени выполнения функции
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {total_time:.4f} секунд")
        return result
    return wrapper

@timer
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib1, fib2 + fib2
        print(fib2, end=' ')

if __name__ == "__main__":
    fibonacci()