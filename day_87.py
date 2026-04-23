#maximum of three number using def

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def maximum(a,b,c):
    return max(a,b,c)

print("Maximum number is:",maximum(a,b,c))
