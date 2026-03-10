#Remove duplicate from list
l = []

n = int(input("Enter how many element you want in list: "))

for i in range(1,n+1):
    l2 = int(input(f"Enter element {i}: "))
    i+=1
    l.append(l2)
    
print("the list is:\n",l)

unique = []

for n in l:
    if n not in unique:
        unique.append(n)
print("After removing duplicates")
print(unique)