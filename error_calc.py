def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Cannot divide by zero!")
    else:
        return x / y

print("Simple Calculator")
print()
print("For Addition, Press 1")
print("For Subtraction, Press 2")
print("For Multiplication, Press 3")
print("For Division, Press 4")
print()
choice = input("Select operation (1/2/3/4): ")

if choice not in ["1", "2", "3", "4"]:
    print("Invalid input")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print()

    if choice == "1":
        result = add(num1, num2)
        # print("Result: " + result)
        print(f"Result: {result}") # String concatenation
    elif choice == "2":
        result = subtract(num1, num2)
        # print("Result: " + result)
        print(f"Result: {result}") # String concatenation
    elif choice == "3":
        result = multiply(num1, num2)
        # print("Result: " + result)
        print(f"Result: {result}") # String concatenation
    elif choice == "4":
        result = divide(num1, num2)
        # print("Result: " + result)
        print(f"Result: {result}") # String concatenation
