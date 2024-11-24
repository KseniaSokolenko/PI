def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_numbers = list(fib(200))

print(f"200-е число Фибоначчи: {fibonacci_numbers[-1]}")