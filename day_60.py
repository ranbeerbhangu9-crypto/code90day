#Split tuple into two halves

t = ()

n = int(input("Enter number of element you want in tuple: "))
for i in range(1,n+1):
    n = int(input(f"Enter elemnt{i}: "))
    i+=1
    t = t + (n,)

print("The tuple is:-\n",t)


mid = len(t) // 2

first = t[:mid]
second = t[mid:]

print("First half:-\n",first)
print("Second half:-\n",second)