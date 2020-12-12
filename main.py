# This is a sample Python script.

import argparse
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def select_recipient_for(name, names):
    selected = name
    while (selected == name):
        r = random.randrange(0, len(names) - 1)
        selected = names[r]
    return selected


def secretsanta(names):
    for name in names:
        recipient = select_recipient_for(name, names)
        print(f'{name} --> {recipient}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--names', help='<Required> Comma separated list of names', required=True, type=str)
    args = parser.parse_args()
    names = args.names.split(",")
    if len(names) == 1:
        print("You need some friends...")
    else:
        secretsanta(names)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
