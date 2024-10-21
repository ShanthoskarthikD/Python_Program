def factor_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  
    return result
number = int(input("Enter a number: "))
fac = factor_iter(number)
print(f"Factorial")