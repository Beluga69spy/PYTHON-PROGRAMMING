# Write a program to demonstrate square of every alternate list elements and append it to another list using for loop.
list1 = [1, 2, 3, 4, 5]
result = []

for i in range(len(list1)):
    if i % 2 == 1:
        result.append(list1[i] ** 2)

print("Square of every alternate element:", result)
