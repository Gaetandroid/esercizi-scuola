'''Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è 0)'''

num_inserito = int(input("Inserisci un qualsiasi numero intero per verificare se è pari o dispari. Il numero è: "))
if num_inserito%2 == 0:
    print("Il numero che hai inserito, (", num_inserito, "), è pari")
else:
    print("Il numero che hai inserito, (", num_inserito, "), è dispari")