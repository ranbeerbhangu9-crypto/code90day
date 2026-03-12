# Reverse a list manually
l = [1, 2, 3, 4, 5]
rev = []

for i in range(len(l)-1, -1, -1):
    rev.append(l[i])

print("Original:", l)
print("Reversed:", rev)
