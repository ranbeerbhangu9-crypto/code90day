#prime number using for loop

n = int(input("Enter number: "))

flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
if flag and n > 1:
    print("The number is prime")
else:
    print("The number is not prime")
