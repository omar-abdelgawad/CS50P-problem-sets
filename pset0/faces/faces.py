def convert(s):
    return s.replace(':(','🙁').replace(':)','🙂')
def main():
    inp = input('please write input: ')
    print(convert(inp))
main()