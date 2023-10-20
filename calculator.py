def multiplication(x, y):
    # function body
    return x * y

def division(x, y):
    # function body
    return x / y

def subtraction(x, y):
    # function body
    return x - y

def addition(x, y):
    # function body
    return x + y



calculatorRunning = True

while calculatorRunning:
    # code to be executed while calculatorRunning is True
    print("\nWelcome to the calculator!\n")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit\n")
   
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input")
            continue
        match choice:
            case '1':
                print("Addition")
                print(num1, "+", num2, "=", addition(num1, num2))
            case '2':
                print("Subtraction")
                print(num1, "-", num2, "=", subtraction(num1, num2))
            case '3':
                print("Multiplication")
                print(num1, "*", num2, "=", multiplication(num1, num2))
            case '4':
                print("You have chosen Division")
                print(num1, "/", num2, "=", division(num1, num2))
            case '5':
                calculatorRunning = False
                
exit()