#Flatten a Nested list

n = [[1,2],[3,4],[5,6]]
print("Original list:-\n",n)

f = []

for s in n:
    for num in s:
        f.append(num)

print("After flatten:-\n",f)


