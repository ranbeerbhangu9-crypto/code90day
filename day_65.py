#user input set

s = set()

n = int(input("Enter number of element: "))

for i in range(1,n+1):
    num = int(input(f"Enter elemen{i}: "))
    i+=1
    s.add(num)

print("Your set:",s)