class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def multiplication(self):
        # function body
        return self.x * self.y

    def division(self):
        # function body
        return self.x / self.y

    def subtraction(self):
        # function body
        return self.x - self.y

    def addition(self):
        # function body
        return self.x + self.y

    @classmethod
    def run(cls):
        calculatorRunning = True
        while calculatorRunning:
            print("\nWelcome to the calculator!\n")
            print("Please select an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit\n")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("\nEnter first number: "))
                    num2 = float(input("Enter second number: "))
                    calc = cls(num1, num2)
                except ValueError:
                    print("Invalid input")
                    continue
                match choice:
                    case '1':
                        print("Addition")
                        print(num1, "+", num2, "=", calc.addition())
                    case '2':
                        print("Subtraction")
                        print(num1, "-", num2, "=", calc.subtraction())
                    case '3':
                        print("Multiplication")
                        print(num1, "*", num2, "=", calc.multiplication())
                    case '4':
                        print("You have chosen Division")
                        print(num1, "/", num2, "=", calc.division())
            elif choice == '5':
                print("Exiting...")
                calculatorRunning = False

if __name__ == "__main__":
    Calculator.run()