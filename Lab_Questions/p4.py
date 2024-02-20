# Write a program to demonstrate multiplication of 2 lists elements using for loop
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = []

for i in range(len(list1)):
    result.append(list1[i] * list2[i])

print("Multiplication is:", result)