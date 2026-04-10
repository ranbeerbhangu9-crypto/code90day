#sorting dictionary by keys

d = {"b":2,"c":3,"a":1,"d":4}

print("Dictionary:",d)
print("After sorting")

for key in sorted(d):
    print(key,":",d[key])