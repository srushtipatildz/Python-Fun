def add(a,b):
    print("Sum",a+b)
def sub(a,b):
    print("Sum",a-b)
def multiply(a,b):
    print("Sum",a*b)                            
def div(a,b):
    print("Sum",a/b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))
match choice:
    case 1:
        add(a, b)
    case 2:
        sub(a, b)
    case 3:
        multiply(a, b)
    case 4:
        div(a, b)
    case _:
        print("Invalid choice")
