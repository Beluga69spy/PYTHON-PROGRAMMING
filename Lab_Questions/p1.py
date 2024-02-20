def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("ENTER OPERATION:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

while True:
    choice = input("ENTER CHOICE (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        n1 = float(input("ENTER NUM 1: "))
        n2 = float(input("ENTER NUM 2: "))

        if choice == '1':
            print(n1, '+', n2, '=', add(n1, n2))
        elif choice == '2':
            print(n1, '-', n2, '=', subtract(n1, n2))
        elif choice == '3':
            print(n1, 'X', n2, '=', multiply(n1, n2))
        elif choice == '4':
            print(n1, '/', n2, '=', divide(n1, n2))
        break
    else:
        print("INVALID !")
