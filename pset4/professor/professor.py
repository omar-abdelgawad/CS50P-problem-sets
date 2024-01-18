import random


def main():
    level = get_level()
    right = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for trial in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != x + y:
                    raise ValueError
            except ValueError:
                print("EEE")
            else:
                right += 1
                break
        else:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {right}")

def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if lev > 3 or lev < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            return lev


def generate_integer(level):
    #doesn't support zero for single digit output unfortunately
    if level not in range(1,4):
        raise ValueError
    if level == 1:
        return random.randint(0,9)
    return random.randint(10**(level-1),10**(level)-1)



if __name__ == "__main__":
    main()