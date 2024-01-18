import sys
import requests
import json


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) != 2:
        sys.exit("Too many command-line arguments")
    try:
        num_coin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()
    cur_price = o["bpi"]["USD"]["rate_float"]
    amount = cur_price * num_coin
    print(f"${amount:,.4f}", end="")


if __name__ == "__main__":
    main()
