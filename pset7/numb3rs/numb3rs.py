import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number_range_re = r"(?:([1-9]?\d)|(1\d{2})|(2[0-4]\d)|(25[0-5]))"
    ip_regular_exp = (
        rf"^{number_range_re}\.{number_range_re}\.{number_range_re}\.{number_range_re}$"
    )
    if mathches := re.search(ip_regular_exp, ip):
        print(mathches.groups())
        return True
    return False


if __name__ == "__main__":
    main()
