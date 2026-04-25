#fibonacci series def function 

n = int(input("Enter a number: "))
def fibonacci(n):
    a , b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

print(f"Fibonacci series of {n}:-")
fibonacci(n)