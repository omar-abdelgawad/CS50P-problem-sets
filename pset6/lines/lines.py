import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

file_path = sys.argv[1]
line_count = 0
try:
    with open(file_path) as file:
        if not file_path.endswith(".py"):
            sys.exit("Not a Python file")
        for line in file:
            if line.strip() and line.strip()[0] != "#":
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exit")

else:
    print(line_count)