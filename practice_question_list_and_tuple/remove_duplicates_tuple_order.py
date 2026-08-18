numbers = (1, 2, 3, 4, 5, 6, 7, 8,2,4,5)
list = list(numbers)
new = []
for i in list:
    if i not in new:
        new.append(i)
tuple=tuple(new) 
print(tuple)       