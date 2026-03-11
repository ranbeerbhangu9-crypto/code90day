#separating Even and odd 

l = []

n = int(input("Enter how many element you want in list: "))

for i in range(1,n+1):
    l2 = int(input(f"Enter element {i}: "))
    i+=1
    l.append(l2)
    
print("the list is:\n",l)

even = []
odd = []

for n in l:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("the even list is:-\n",even)
print("the odd list is:-\n",odd)


