# Check if all items in the tuple are the same

tup1 = (1, 1, 1, 1, 1)
tup2 = []
for i in tup1:
    tup2.append( i == tup1[0] )

same = all(tup2)
print(same)