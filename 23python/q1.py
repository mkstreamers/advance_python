#1. Write a program that takes two integers, computes their sum, difference, product, and division, checks if they’re even/odd, and converts one to a float.
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num1_float = float(num1)

print("\n--- Results ---")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)

print(f"{num1} is", check_even_odd(num1))
print(f"{num2} is", check_even_odd(num2))

print("Float conversion of first number:", num1_float)