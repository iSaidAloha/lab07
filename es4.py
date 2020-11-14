'''

Scrivete la funzione def sameSet(a, b) che verifichi se due liste contengono gli stessi
elementi, indipendentemente dall’ordine e ignorando la presenza di duplicati. Ad
esempio, le due liste 1 4 9 16 9 7 4 9 11 e 11 11 7 9 16 4 1 devono essere considerate
uguali. Probabilmente vi sarà utile progettare funzioni ausiliarie.

'''


def sameSet(a, b):
    isDiff = True

    for i in a:
        if i not in b:
            isDiff = False
    for i in b:
        if i not in a:
            isDiff = False

    return isDiff


list1 = [1, 4, 9, 16, 7, 9, 4, 9, 11]
list2 = [11, 11, 7, 9, 16, 4, 1]

print(sameSet(list1, list2))
