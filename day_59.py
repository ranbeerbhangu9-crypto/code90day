#finding pair whose sum is equal to 6

t = (1,2,3,4,5)
print("The tuple is:-\n",t)

target = 6
print("the pairs whose sum is equal to 6:- ")
for i in range(len(t)):
    for j in range(i+1, len(t)):
        if t[i] + t[j] == target:
            print(t[i],t[j])