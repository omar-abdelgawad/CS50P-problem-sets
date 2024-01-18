from datetime import date
import inflect
import sys


def main():
    inp_date = input("date: ")
    try:
        birth_day = get_date(inp_date)
    except ValueError:
        sys.exit("Invalid date")
    min_words = get_minutes_str(date.today(),birth_day)
    print(min_words)


def get_date(s:str)->date:
    year, month, day = map(int,s.split('-'))
    return date(year,month,day)

def get_minutes_str(new_date:date, old_date:date)->str:
    time_days = (new_date - old_date).days
    time_min = time_days * 24 * 60
    time_min_words = inflect.engine().number_to_words(time_min)
    time_min_words = time_min_words.replace("and ",'').capitalize()
    return f"{time_min_words} minutes"

if __name__ == "__main__":
    main()