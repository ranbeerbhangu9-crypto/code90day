#second largest number without using sort method
l = []

n = int(input("Enter how many element you want in list: "))

for i in range(1,n+1):
    l2 = int(input(f"Enter element {i}: "))
    i+=1
    l.append(l2)
    
print("the list is:\n",l)
large = second = -9999

for n in l:
    if n > large:
        second = large
        large = n
    elif n > second and n != large:
        second = n

print("Second largest number:", second)