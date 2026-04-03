#Intersection of two set
s1 = set()

n = int(input("Enter number of element of set 1: "))

for i in range(1,n+1):
    num = int(input(f"Enter elemen{i}: "))
    i+=1
    s1.add(num)

print("Your set:",s1)
s2 = set()

n = int(input("Enter number of element of set 2: "))

for i in range(1,n+1):
    num = int(input(f"Enter elemen{i}: "))
    i+=1
    s2.add(num)

print("Your set:",s2)

print("Intersection:", s1 & s2)


