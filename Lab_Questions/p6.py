# Write a program to remove duplicate elements from a list.
my_list = [1, 2, 3, 2, 4, 5, 6, 5]
new_list = []

for num in my_list:
    if num not in new_list:
       new_list.append(num)
print("Original List:", my_list)
print("List after duplicates removed:", new_list)