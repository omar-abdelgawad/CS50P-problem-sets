greeting = input("Greeting: ").lower().strip()
#first condition 0 dollars.
if greeting.startswith("hello"):
    print('$0')
#second condition 20 dollars
elif greeting[0]=='h':
    print('$20')
else:
    print('$100')
#third condition 100 dollars
