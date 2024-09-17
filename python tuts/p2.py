def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# Get inputs from the user and convert them to numbers
a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
choice = input("Please enter 1 for +, 2 for -, 3 for *, 4 for / : ")

# Perform the chosen operation
if choice == "1":
    result = add(a, b)
    print("Sum:", result)

elif choice == "2":
    result = sub(a, b)
    print("Difference:", result)

elif choice == "3":
    result = mul(a, b)
    print("Product:", result)

elif choice == "4":
    if b != 0:  # Check to avoid division by zero
        result = div(a, b)
        print("Quotient:", result)
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid choice.")
