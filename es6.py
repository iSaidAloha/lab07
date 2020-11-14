'''

Scrivete una funzione che inverta la sequenza degli elementi di una lista. Ad
esempio, se la funzione viene invocata con la lista 1 4 9 16 9 7 4 9 11, deve
modificarne il contenuto in modo che diventi 11 9 4 7 9 16 9 4 1

'''
import random

def reverse(list):
    result = []
    for i in range(1, len(list)+1):
        result.append(list[-i])
    return result

list = []
for i in range(9):
    list.append(random.randint(0, 99))
reversed  = reverse(list)
print(list, reversed, sep='\n')
