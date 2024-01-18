def main():
    while True:
        inp = input("Fraction: ")
        try:
            frac = convert(inp)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(frac))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    frac = round(x / y * 100)
    return frac


def gauge(percentage):
    if percentage < 2:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
        