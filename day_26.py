print("The numbers divisible by 5 from 1 to 100 are :-")
count = 0
for i in range(1,101):
    if (i % 5 == 0):
        print(i)
        count = count + 1
print(f"total '{count}' numbers are divisible by '5' from (1 to 100 )")