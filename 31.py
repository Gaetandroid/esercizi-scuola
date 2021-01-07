'''Fornisci la rappresentazione in binario di un numero decimale.
Dopo aver acquisito il valore del Numero da trasformare, si esegue la divisione del numero per 2 e si calcola quoziente e resto.
Il resto è la prima cifra della rappresentazione binaria. Si ripete il procedimento assegnando il quoziente ottenuto a Numero e ricalcolando la divisione per 2;
la ripetizione prosegue mentre il quoziente ottenuto si mantiene diverso da zero.
La rappresentazione binaria del numero decimale è costituita dalle cifre binarie ottenute come resti, lette in ordine inverso.
Confronta poi il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero decimale in binario. '''

def transformbin(dec):
    binario = ""
    while dec > 0:
        if dec%2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        dec = int(dec/2)
    print(binario)

print("Inserisci il numero decimale: ")
decimale = int(input())
transformbin(decimale)