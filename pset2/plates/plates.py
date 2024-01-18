def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str)->bool:
    if s[:2].isalpha() == False:
        return False
    if len(s)>6 or len(s)<2:
        return False
    check = True
    for i in range(len(s)-1):
        if (s[i].isalpha()):
            continue
        if s[i].isalpha()==False and s[i].isnumeric()==False:
            return False
        if check and s[i]=='0':
            return False
        else:
            check = False
        if s[i].isnumeric() and s[i+1].isalpha():
            return False
    return True


main()