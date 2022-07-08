def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

Fib= list(range(10))
for n in range(1,11):
    Fib[n-1]=fibonacci(n)

print(Fib)