def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open('fib.txt', 'w') as f:
    fibonacci_numbers = fib(200)
    f.writelines(f"{num}\n" for num in fibonacci_numbers)