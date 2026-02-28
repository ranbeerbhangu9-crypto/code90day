#factorial using while loop

n = int(input("Enter a number: "))
i = 0
fact = 1

while i < n:
    i += 1
    fact *= i
print(f"the factorial of {n} is {fact}") 