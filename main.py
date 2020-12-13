# This is a sample Python script.

import argparse

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from src.secret_santa import SecretSanta

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--names",
        help="<Required> Comma separated list of names",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-l",
        "--lang",
        help="<Optional> language (en|fi)",
        required=False,
        type=str,
        default="en",
    )
    args = parser.parse_args()
    names = args.names.split(",")
    if len(names) == 1:
        print("You need some friends...")
    else:
        SecretSanta(names=names).perform(args.lang)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
