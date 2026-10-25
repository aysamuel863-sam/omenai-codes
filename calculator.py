num1 = float(input("Enter first nmuber: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")
def calculate(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "^":
        print(num1 ** num2)

Calculate_again = "Y"
while Calculate_again.capitalize() == "Y":
    calculate(num1, num2, operator)

    
    Calculate_again = input("Calculate again?(Y/N): ").capitalize()
