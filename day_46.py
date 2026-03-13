#common element bteween two list

l1 = [1,2,3,4,5,6]
l2 = [2,4,6,8,9,7]

print("First list:-\n",l1)
print("Second list:-\n",l2)
c = []

for n in l1:
    if n in l2:
        c.append(n)
print("common element:-\n",c)