#Maximum difference

l = []

n = int(input("Enter a number of element you want in list: "))

for i in range(1,n+1):
    l2 = int(input(f"Enter element {i}: "))
    i+=1
    l.append(l2)

print("the list is:-\n",l)

md = max(l) - min(l)

print("Maximum difference:",md)