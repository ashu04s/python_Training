s1 = set(map(int, input("Enter first set values: ").split()))
s2 = set(map(int, input("Enter second set values: ").split()))

print("Union =", s1 | s2)
print("Intersection =", s1 & s2)
print("Difference =", s1 - s2)
print("Difference s2 - s1 =", s2 - s1)
print("Symmetric difference =", s1 ^ s2)

print("s1 subset of s2:", s1.issubset(s2))
print("s1 superset of s2:", s1.issuperset(s2))
print("Disjoint:", s1.isdisjoint(s2))