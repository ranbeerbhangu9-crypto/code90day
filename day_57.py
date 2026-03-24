t = ()

n = int(input("Enter number of element you want in tuple: "))
for i in range(1,n+1):
    n = int(input(f"Enter elemnt{i}: "))
    i+=1
    t = t + (n,)

print("The tuple is:-\n",t)

lst = list(t)
lst.remove(max(lst))

print("Second largest number :",max(lst))