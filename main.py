# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
import math


def calcGen(g, n):
    counter = 2
    while not math.pow(g, counter) % n == g:
        print(int(math.pow(g, counter) % n))
        counter = counter+1
    print("--------------")
    return counter -1


if __name__ == '__main__':
    g = input("Generaror:")
    n = input("Modulo:")
    print(calcGen(int(g), int(n)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
