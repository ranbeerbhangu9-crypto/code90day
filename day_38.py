#sum of digits of a number

n = int(input("Enter a number: "))

i = 0

while n > 0:
    dig = n % 10
    i = i + dig
    n = n // 10
print("Sum of digits =", i)