inp = input("Input: ")
for c in inp:
    if c.lower() not in ['a','e','i','o','u']:
        print(c,end="")
print()