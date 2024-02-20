# Write a program to demonstrate the factorial using recursion.
def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
