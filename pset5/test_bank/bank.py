def main():
    greeting = input("Greeting: ").lower().strip()
    print(value(greeting))


def value(greeting):
    #first condition 0 dollars.
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    #second condition 20 dollars
    elif greeting[0]=='h':
        return 20
    #third condition 100 dollars
    else:
        return 100



if __name__ == "__main__":
    main()