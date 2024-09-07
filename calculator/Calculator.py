def calculator():
    while True:  
        try:

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))


            print("Select an operation: +, -, *, /")
            operation = input("Enter the operation: ")


            if operation == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operation == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operation == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Invalid operation type.")
            break

        except ValueError:
            print("Invalid input: Please enter numeric values (float or int).")


        except ZeroDivisionError as e:
            print(e)




calculator()

