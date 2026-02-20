#Sum of numbers, 1 + 2 + 3 + 4+......+n
n = int(input("Enter the number: "))
total = 0
for i in range(1,n+1):
    total = total + i
print(f"sum of numbers from 1 to {n} is:{total}")