'''

Scrivete la funzione sumWithoutSmallest che calcoli, con un unico ciclo, la somma
di tutti i valori di una lista, escludendo il valore minimo. Nel ciclo, aggiornate la
somma e il valore minimo; al termine, si stampi a terminale la differenza tra questi
due valori

'''


def sumWithoutSmallest(list):
    list.sort()
    sum = 0
    for i in list:
        sum += i
    sum = sum - list[0]
    return sum, list[0]


list = [1, 4, 9, 16, 9, 7, 4, 9, 11]

a, b = sumWithoutSmallest(list)
print(a - b)
