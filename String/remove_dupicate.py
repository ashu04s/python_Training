string ="asbsfdfjfjkd"
sp =" ".join(string)
print(sp)
list = sp.split()
print(list)
list2 =[]
for i in list:
    if i in list2:
        pass
    else:
      list2.append(i)
print(list2)    
new = "".join(list2)
print(new)        



# 1. string
#    ↓
# "asbsfdfjfjkd"

# 2. " ".join(string)
#    ↓
# "a s b s f d f j f j k d"

# 3. split()
#    ↓
# ['a','s','b','s','f','d','f','j','f','j','k','d']

# 4. Loop through list
#    ↓
# Check: i already exists in list2?

# 5. If exists → skip
#    If not exists → append()

# 6. Unique list:
# ['a','s','b','f','d','j','k']

# 7. "".join(list2)
#    ↓
# "asbfdjk"