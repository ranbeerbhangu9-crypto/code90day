#Even odd tuple & even odd count

t = ()

n = int(input("Enter number of element you want in tuple: "))
for i in range(1,n+1):
    n = int(input(f"Enter elemnt{i}: "))
    i+=1
    t = t + (n,)

print("The tuple is:-\n",t)
even_no = odd_no = 0
even = ()
odd = ()

for i in t:
    if i % 2 == 0:
        even = even + (i,)
        even_no += 1
    else:
        odd = odd + (i,)
        odd_no += 1

print("The even tuple is:-\n",even)
print("The even count in tuple is:-\n",even_no)
print("The odd tuple is:-\n",odd)
print("The odd count in tuple is:-\n",odd_no)