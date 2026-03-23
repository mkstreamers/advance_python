#14. Custom Power Function Create a function that takes base and exponent as input and returns base^exponent using loops (not using pow()).
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

for _ in range(exp):
    result *= base

print("Result:", result)