#frequency of element
t = (1,1,1,1,2,2,2,3,3,3,3,3,4,4,5,5,5,5)
s = ()

for i in t:
    if i not in s:
        print(i,":",t.count(i))
        s = s + (i,)