def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            frac = round(x/y * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x <= y:
                break
    if frac < 2:
        print("E")
    elif frac>98:
        print("F")
    else:
        print(f"{frac}%")


main()