#List user input

l = []
n = int(input("Enter how many element you want in a list: "))

for i in range(1,n+1):
    l2 = int(input(f"Enter elememt {i}:"))
    i +=1
    l.append(l2)

print("Your list is:-")
print(l)