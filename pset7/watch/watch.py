import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    reg_exp = r'src="https?://(?:www.)?youtube.com/embed/(.*?)"'
    match = re.search(reg_exp, s)
    if not match:
        return None
    unique_id = match.group(1)
    return "https://youtu.be/" + unique_id


if __name__ == "__main__":
    main()
