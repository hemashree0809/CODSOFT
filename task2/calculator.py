
    
def show():
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
def main():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        show()
        choice = input("Enter your choice (1/2/3/4): ")


        if choice == '1':
            result = num1 + num2
            print(f"The result of addition is: {result}")
            print()
        elif choice == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
            print()
        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
            print()
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
                print()
            else:
                print("Error: Division by zero is not allowed.") 
                print()
        elif choice=='5':
            print("Exiting!!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")
            print()

if __name__ == "__main__":
    main()

