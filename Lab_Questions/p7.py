# Write a program to find the number of occurrence of an element in a numeric only list and find the sum of that element and store it in another list.
my_list = [1, 2, 3, 4, 5, 3, 2, 1]
element = 3
occurrences = my_list.count(element)
sum_list = [element * occurrences]

print("Number of occurrences of", element, ":", occurrences)
print("Sum of occurrences of", element, ":", sum_list)