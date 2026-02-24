#sum of even or odd from 1 to 100

even = 0
odd = 0

for i in range(1,101):
    if i % 2 == 0:
        even +=i
    elif i % 2 !=0 :
        odd+=i
print(f"the even sum from 1 to 100 is {even}")
print(f"the odd sum from 1 to 100 is {odd}")
