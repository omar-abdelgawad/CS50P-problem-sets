from random import randint
from sys import exit
def main():
    level = get_pos_int("Level: ")
    x = randint(1,level)
    while True:
        guess = get_pos_int("Guess: ")
        if guess == x:
            exit("Just Right!")
        elif guess > x:
            print("Too Large!")
        else:
            print("Too Small!")

def get_pos_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            pass
        else:
            if n <= 0:
                continue
            return n

if __name__ == "__main__":
    main()