# def add(a,b):
#     print("Sum",a+b)
# def sub(a,b):
#     print("Sum",a-b)
# def multiply(a,b):
#     print("Sum",a*b)                            
# def div(a,b):
#     print("Sum",a/b)

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = int(input("Enter your choice: "))
# match choice:
#     case 1:
#         add(a, b)
#     case 2:
#         sub(a, b)
#     case 3:
#         multiply(a, b)
#     case 4:
#         div(a, b)

#lambda function

# square= lambda n : n*n
# print(square(8))

def countdown(n):
    if n==0:
        print("Done")
        return
    print(n)
    countdown(n-1)

countdown(10)  


#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))