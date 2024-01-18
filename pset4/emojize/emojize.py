import emoji
def main():
    s = input("Input: ")
    if emoji.emojize(s)!=s:
        print("Output:",emoji.emojize(s))
    else:
        print("Output:",emoji.emojize(s,language='alias'))


main()