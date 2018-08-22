import cs50
import sys
from cs50 import get_int
from cs50 import get_string

def main():
    while True:
        k = int(sys.argv[1])
        if k != 0:
            break

    print("plaintext: ", end="")
    plain = get_string()

    print("ciphertext: ", end="")

    for i in range(len(plain)):
        if str.islower(plain[i]):
            mess = plain[i] + k
            base = mess - 97
            modulo = base % 26
            cipher = modulo + 97
            lower = cipher
            print(chr(lower), end="")

        elif str.isupper(plain[i]):
            mess = plain[i] + k
            base = mess - 65
            modulo = base % 26
            cipher = modulo + 65
            upper = cipher
            print(chr(upper), end="")

        else:
            print("{}".format(plain[i]), end="")

    print()

if __name__ == "__main__":
    main()