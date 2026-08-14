a = int(input("enter first no"));
b =int(input("enter secoond no"));
print(f"after swapping {a} and {b}")
temp =a;
a= b;
b= temp;
print(f"after swapping {a} and {b}")

print("without using third varible")
print(f"before swapping {a} and {b}")
a = a+b; 
b =a-b; 
a = a-b ;
print(f"after swapping {a} and {b}")