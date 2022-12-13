# This program performs arithmetic operations

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the requested operation
print("Choose the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
  result = num1 + num2
  print(num1, "+", num2, "=", result)
elif choice == 2:
  result = num1 - num2
  print(num1, "-", num2, "=", result)
elif choice == 3:
  result = num1 * num2
  print(num1, "*", num2, "=", result)
elif choice == 4:
  result = num1 / num2
  print(num1, "/", num2, "=", result)
else:
  print("Invalid input")
