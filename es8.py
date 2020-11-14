'''

Spesso i valori raccolti durante un esperimento vanno corretti, per togliere parte del
rumore di misura. Un approccio semplice a questo problema prevede di sostituire, in
una copya, ciascun valore con la media tra il valore stesso e i due valori adiacenti (o un
unico adiacente se il valore in esame si trova a una delle due estremità della copya).
Realizzate un programma che svolga tale operazione, senza creare un’altra copya.

'''


def correct(a):
    copy = list(a)
    lenBefEdit = len(copy)
    for i in range(lenBefEdit):
        if i == 0:
            avg = (copy[i]+copy[i+1])/2
        elif i == lenBefEdit-1:
            avg = (copy[i-1]+copy[i])/2
        else:
            avg = (copy[i-1]+copy[i]+copy[i+1])/3
        avg = round(avg, 2)
        copy.append(avg)
    return copy[lenBefEdit:]


a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
b = correct(a)

print(a, b, sep="\n")
