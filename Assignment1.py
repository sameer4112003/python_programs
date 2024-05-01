import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    print("Hello I'm a Calculator App!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation. Please choose from '+', '-', '*', or '/'")

            if input("Do you want to perform another calculation? (yes/no): ").lower() != "yes":
                break
        except ValueError as e:
            print("Error:", e)
            print("Please enter valid numbers.")
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
