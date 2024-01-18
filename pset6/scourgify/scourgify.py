import csv
import sys


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    read_file_path = sys.argv[1]
    write_file_path = sys.argv[2]
    students = []
    try:
        with open(read_file_path) as read_file:
            for student in csv.DictReader(read_file):
                last, first = student["name"].split(",")
                student["first"] = first.strip()
                student["last"] = last.strip()
                del student["name"]
                students.append(student)
    except FileNotFoundError:
        sys.exit(f"Could not read {read_file_path}")

    with open(write_file_path, "w") as write_file:
        writer = csv.DictWriter(write_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)
            print(student)


if __name__ == "__main__":
    main()
