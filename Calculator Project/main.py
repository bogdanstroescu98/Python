import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
calculator_is_on = True
def calculator():

    should_accumulate = True
    num1 = int(input("What is the first number?: "))
    while should_accumulate:
        for key in operations:
            print(key)
        operation_key = input("Pick an operation: ")
        num2 = int(input("What is the next number?: "))
        result = operations[operation_key](num1,num2)
        print(f"{num1} {operation_key} {num2} = {result}")
        continue_calculation = input(f"Type 'y' to continue calculating with {result},"
                                        f" or type 'n' to start a new calculation, or type 'x' to turn the calculator off: ").lower()
        if continue_calculation == "y":
            num1 = result
        elif continue_calculation == "n":
            should_accumulate = False
            print("\n" * 50)
            calculator()
        elif continue_calculation == "x":
            print("Turning Off....Thank you for using my calculator!")
            break


calculator()


