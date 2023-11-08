import calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = float(input("Enter in first number: "))
second_input = float(input("Enter in second number: "))
operation = input("Would you like to add/subtract/multiple/divide: ")


if operation == "add":
    result = calculator.add(first_input,second_input)
    print(f"Result: {result}")
elif operation == "subtract":
    result = calculator.subtract(first_input,second_input)
    print(f"Result: {result}")
elif operation == "multiply":
    result = calculator.multiply(first_input,second_input)
    print(f"Result: {result}")
elif operation == "divide":
    result = calculator.divide(first_input,second_input)
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")
