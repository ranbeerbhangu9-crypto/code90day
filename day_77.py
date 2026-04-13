#reverse dictionary
d = {}

n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Dictionar:",d)

rev = {}

for k, v in d.items():
    rev[v] = k

print("Reverse dictionary:",rev)