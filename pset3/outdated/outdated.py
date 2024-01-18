def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = map(int, date.split("/"))

        except ValueError:
            try:
                month, day, year = date.split(" ")
                month = months.index(month) + 1
                day = int(day[:-1])
                year = int(year)

            except ValueError:
                continue

            else:
                if day > 31 or day < 1 or year < 0:
                    continue
                break
        else:
            if day > 31 or day < 1 or month > 12 or month < 1 or year < 0:
                continue
            break
    print(f"{year:04}-{month:02}-{day:02}")


main()
