# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def select_recipient_for(name, names):
    selected = name
    while(selected == name):
        r = random.randrange(0, len(names)-1)
        selected = names[r]
    return selected


def secretsanta():
    names = ["Antti","Katja","Aada","Helmi","Aune","Harri","Anni","Ilona"]
    for name in names:
        recipient = select_recipient_for(name, names)
        print(f'{name} --> {recipient}')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secretsanta()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
