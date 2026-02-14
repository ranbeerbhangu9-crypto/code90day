#pyramid pattern 
n = int(input("Enter number: "))

for i in range(n+1):
    print(" "*(n-i) + "*"*(2*i-1))
