'''Fornisci la rappresentazione in decimale di un numero binario. 
All'inizio si richiede il numero di cifre di cui è composto il numero binario (lunghezza); 
si esegue poi una ripetizione che richiede le cifre del numero binario una a una a partire da destra e per ciascuna calcola il prodotto della cifra binaria per la potenza di 2 corrispondente alla posizione della cifra binaria e aggiunge il risultato alla somma; 
la ripetizione viene eseguita per il contatore che va dal valore O al valore di lunghezza diminuito di 1. 
Confronta poi il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero binario in decimale.
'''

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
print("\nNumero binario registrato e diviso in cifre singole: ",numero)
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