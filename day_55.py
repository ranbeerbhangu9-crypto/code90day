#Merging two tuple and removing duplicates
t1 = (1,2,3,4,5)
t2 = (3,4,5,6,7,2)
print("First tuple:-",t1)
print("Second tuple:-",t2)

merge = tuple(set(t1 + t2))
print("the merged tuple is:-\n",merge)