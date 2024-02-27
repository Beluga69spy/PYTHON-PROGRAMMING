# Modify the tuple
tup1 = (1, 2, 3, 4, 5)
tup_to_list = list(tup1)
tup_to_list[2] = 99
list_to_tup = tuple(tup_to_list)
print(list_to_tup)