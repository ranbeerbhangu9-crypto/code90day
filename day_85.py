#even odd using def 

n = int(input("Enter a number: "))
def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check(n))