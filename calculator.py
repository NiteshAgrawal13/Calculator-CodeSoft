#BASIC CALCULATOR USING ARITHMATIC OPERATION
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def main():
  operation_choices = {
      '+': add,
      '-': subtract,
      '*': multiply,
      '/': divide,
  }

  print("Please input two numbers: ")
  num1 = float(input("Enter First number: "))
  num2 = float(input("Enter Second number: "))

  print("Please choose an operation: ")
  for operation in operation_choices:
      print(f"{operation}: {operation_choices[operation].__name__}")

  operation = input("Operation: ")

  while operation not in operation_choices:
      print("Invalid operation selected. Please choose a valid operation: ")
      operation = input("Operation: ")

  print(f"Result: {operation_choices[operation](num1, num2)}")

if __name__ == "__main__":
  main()