def main():
    items = {}
    while True:
        try:
            item = input("").upper()
        except EOFError:
            print()
            break
        else:
            items[item] = items.get(item,0)+1
    for item in sorted(items):
        print(items[item],item)

main()