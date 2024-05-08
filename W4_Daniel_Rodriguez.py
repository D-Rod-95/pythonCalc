# Program name: Wk3_Daniel_Rodriguez.py
# Student Name: DanielRodriguez
# Course: ENTD220
# Instructor: Osama Morad
# Date: March 31, 2024
# Description: This code performs basic math operations (addition, subtraction, multiplication, division) on two numbers within a specified range.

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "Error --> {e}"


def IsInRange(lr, hr, n):
    return lr <= n <= hr


def main():
        #Check if the number is within the specified range.
    while True:
        try:
            lr = float(input("Enter your Lower range ---> "))
            hr = float(input("Enter your Higher range ---> "))
            
            num1 = float(input(f"Enter your First number ({lr} - {hr}) ---> "))
            if not IsInRange(lr, hr, num1):
                print("The input values are outside the input ranges. Please check the numbers and try again.")
                continue
            
            num2 = float(input(f"Enter your Second number ({lr} - {hr}) ---> "))
            if not IsInRange(lr, hr, num2):
                print("The input values are outside the input ranges. Please check the numbers and try again.")
                continue

            
            print(f"The result of {num1} + {num2} = {add(num1, num2)}")
            print(f"The result of {num1} - {num2} = {sub(num1, num2)}")
            print(f"The result of {num1} * {num2} = {mult(num1, num2)}")
            print(f"The result of {num1} / {num2} = {div(num1, num2)}")

    
      # Handling ValueError to catch non-numeric inputs.
        except ValueError as e:
            print("Error --> {e}")  
            continue

        choice = input("Continue Looping Y/N: ").upper()
        if choice != 'Y':
            print("Thank you for using the calculator")
            break
main()

