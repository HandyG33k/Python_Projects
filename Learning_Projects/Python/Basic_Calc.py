# 11/26/2024
# Challenge: "Build a Basic Calculator"
# Objective: Create a Python program that acts as a simple calculator. It should take two numbers and perform an operation (addition, subtraction, multiplication, or division) based on user input.



num1 = int(input("What is the first number you would like to us? \n"))
num2 = int(input("What is the second number you would like to us? \n"))
operation = input("What operation would you like to perform on these numbers? \n + will add the numbers \n - will subtract the numbers \n * will multiply the numbers \n / will divide the numbers \n")

if operation == "+":
    Result = num1 + num2
elif operation == "-":
    Result = num1 - num2
elif operation == "*":
    Result = num1 * num2
elif operation == "/":
    Result = num1 / num2

print(f"Your result is {Result} \n")
