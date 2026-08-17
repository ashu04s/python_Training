# Creation 

set = {1, 3, 7, 5}
print(set)

# Empty dictionary
set2 = {}
print(type(set2))

# Empty set
# a = set()
# print(type(a))

# Cannot access set using index
# print(my_set[0])  # TypeError

# Access items using loop
for i in set:
    print(i)

# Add single item
set.add(6)

print(set)

# to add multiple item
set.update([40, 50, 60])
print(set)