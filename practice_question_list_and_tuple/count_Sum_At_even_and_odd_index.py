list =[1,2,3,43,23,23]
even =0
odd=0
for i in range(len(list)):
    if i%2==0:
        even =even+list[i]
    else:
        odd=odd+list[i]
print(f"Sum of elements at even index: {even}")
print(f"Sum of elements at odd index: {odd}")