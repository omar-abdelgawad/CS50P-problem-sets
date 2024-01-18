def main():
    inp = input("word: ")
    print(shorten(inp))


def shorten(word):
    new_word = ""
    for c in word:
        if c.lower() not in ['a','e','i','o','u']+[',','.']+['1']:
            new_word += c
    return new_word


if __name__ == "__main__":
    main()