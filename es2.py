import random

'''

Scrivete un programma che calcoli la somma alternata degli elementi di una lista. Ad
esempio, se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e
visualizzare 1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = –2

'''


def main():
    list = []
    for i in range(10):
        list.append(random.randint(0, 12))

    while True:

        print(f"La lista è {list}")
        print(f"La somma alternata è {sommaAlternata(list)}")

        c = int(input("Continuare? [0 == NO] > "))
        if not c:
            break;


def sommaAlternata(list):
    result  = 0
    for i in range(len(list)):
        value = list[i]
        if not i % 2 == 0:
            value = -value
        result = result + value
    return result

main()
