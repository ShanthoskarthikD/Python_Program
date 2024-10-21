def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input())
for i in range(n):
    print(fibonacci_recursive(i), end=" ")