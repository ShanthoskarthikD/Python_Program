
def sum_of_digits(number):
    sum = 0
    while number != 0:
        sum += number % 10  
        number //= 10      
    return sum
number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
