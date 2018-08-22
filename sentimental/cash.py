import cs50
from cs50 import get_int
from cs50 import get_string
from cs50 import get_float

def main():

    while True:
        print("Changed owed?")
        n = get_float
        if n < 0:
            break

        change = n * 100
        coin = 0;

        while change >= 25:
            coin += 1
            change = change - 25

        while change >= 10:
            coin += 1
            change = change - 10

        while change >= 5:
            coin += 1
            change = change - 5

        while change >= 1:
            coin += 1
            change = change - 1

    print("{} change".format(coin + change))

if __name__ == "__main__":
    main()
