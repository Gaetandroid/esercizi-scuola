numero = []
print("Inserisci la lunghezza del numero binario")
lunghezza = int(input())
ripetizione = 0
for i in range(lunghezza):
    ripetizione += 1
    print("A partire da destra, inserisci la cifra n", ripetizione)
    cif = int(input())
    numero.append(cif)
numero.reverse()
print("\nNumero binario registrato diviso in cifre da 1: ",numero)
somma = 0
potenza = 0
for i in range(lunghezza):
    finale = numero[lunghezza-1]
    if finale == 0:
        somma += 0
    elif finale == 1:
        somma += 2**potenza
    lunghezza -= 1
    potenza += 1
print("\nNumero decimale ottenuto: ",somma)