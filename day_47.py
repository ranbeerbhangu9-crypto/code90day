#Rotate list right by one position

l = []

n = int(input("Enter a number of element you want in list: "))

for i in range(1,n+1):
    l2 = int(input(f"Enter element {i}: "))
    i+=1
    l.append(l2)

print("the list is:-\n",l)

last = l[-1]

l.pop()
l.insert(0,last)

print("after rotating:-\n",l)