import csv
from tabulate import tabulate
import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    file_path = sys.argv[1]
    try:
        with open(file_path) as file:
            if not file_path.endswith(".csv"):
                sys.exit("Not a CSV file")
            print(tabulate(csv.DictReader(file),headers="keys",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exit")


if __name__ == "__main__":
    main()
