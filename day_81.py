#Group word by length
words = ["hi", "hello", "hey", "python"]
print("Dictionary:",words)

d = {}
for w in words:
    d.setdefault(len(w), []).append(w)

print("After:",d)