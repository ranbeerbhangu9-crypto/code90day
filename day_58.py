#flatten nested tuple

t = ((1,2),(3,4),(5,6),(7,8))

print("The nested tuple is:-\n",t)

f = ()

for sub in t:
    f += sub

print("After flatten:-\n",f)