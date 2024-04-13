#1. Write a Python program to divide two numbers.

def divide_number(num1,num2):
  try:
    result=num1 / num2
    return result
  except ZeroDivisionError:
    return ("Error: cant divide by zero")

num1 = int(input("enter value for num1: "))
num2 = int(input("enter value for num2: "))

print(f"The result of {num1} / {num2} is: {divide_number(num1, num2)}")
