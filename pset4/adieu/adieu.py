import inflect
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            s = input("Name: ")
        except EOFError:
            print()
            break
        else:
            names.append(s)
    print(f'Adieu, adieu, to {p.join(names)}')


if __name__=='__main__':
    main()