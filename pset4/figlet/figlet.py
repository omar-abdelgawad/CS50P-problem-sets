import sys
import random
from pyfiglet import Figlet

###if you run this file without any extra command line arguments it applies a random font

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid Uge")
    if len(sys.argv)==3 and sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Invalid Usage")
    fig = Figlet()
    choices = fig.getFonts()
    if len(sys.argv)==1:
        s = input("Input: ")
        font = random.choice(choices)
        fig.setFont(font=font)
        print(fig.renderText(s))
    else:
        if sys.argv[2] not in choices:
            sys.exit("Invalid Usage")
        s = input("Input: ")
        font = sys.argv[2]
        fig.setFont(font=font)
        print(fig.renderText(s))

if __name__ == '__main__':
    main()