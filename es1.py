import random

'''

Scrivete un programma che inizializzi una lista con dieci numeri interi casuali e, poi,
visualizzi quattro righe di informazioni, contenenti:
a. Tutti gli elementi di indice pari.
b. Tutti gli elementi di valore pari.
c. Tutti gli elementi in ordine inverso.
d. Il primo e l’ultimo elemento.

'''


def main():
    list = []
    for i in range(10):
        list.append(random.randint(0, 99))

    while True:

        print(f"La lista è {list}")
        print(f"I valori negli indici pari sono {evenIndex(list)}")
        print(f"I valori pari sono {even(list)}")
        print(f"La lista al contrario è {reverse(list)}")
        print(f"Il primo elemento è {list[0]}, l'ultimo è {list[-1]}")

        c = int(input("Continuare? [0 == NO] > "))
        if not c:
            break;


def evenIndex(list):
    result = []
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    return result


def even(list):
    result = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            result.append(list[i])
    return result


def reverse(list):
    result = []
    for i in range(1, len(list)+1):
        result.append(list[-i])
    return result


main()
