import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    reg_ex = r"((?:[1-9])|(?:1[0-2]))(:[0-5]\d)? (A|P)M to ((?:[1-9])|(?:1[0-2]))(:[0-5]\d)? (A|P)M"
    match = re.search(reg_ex, s)
    if not match:
        raise ValueError
    first_hour = int(match.group(1))%12 + (12 if match.group(3)=='P' else 0)
    first_minute = match.group(2) if match.group(2) else ':00'
    second_hour = int(match.group(4))%12 + (12 if match.group(6)=='P' else 0)
    second_minute = match.group(5) if match.group(5) else ':00'
    new_24hour_format = f"{first_hour:02}{first_minute} to {second_hour:02}{second_minute}"
    return new_24hour_format




if __name__ == "__main__":
    main()