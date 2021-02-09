'''Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un 
messaggio nel caso la persona non sia presente nella rubrica (GC)
'''
l_numeri = []
l_nomi = []

d_nomi_num = {}

while True:
    nome = input("Inserire il nome della persona: ")
    print("inserire il numero telefonico di", nome, ":")
    numero = input()
    
    l_nomi.append(nome)
    l_numeri.append(numero)

    print("Premere 1 per continuare a inserire persone con il loro numero. Premere 0 per terminare e visualizzare la rubrica. ")
    stop = int(input())
    if stop == 0:
        break

for i in range(len(l_nomi)):
    d_nomi_num[l_nomi[i]] = l_numeri[i]

print(d_nomi_num)

while True:
    print("Digitare il nome di una persona per cercare il suo numero nella rubrica: ")
    ricerca = input()
    if ricerca in d_nomi_num.keys():
        print(d_nomi_num.get(ricerca))
    else:
        print(ricerca, "non è nella rubrica.")
    print("Premere 1 per continuare la ricerca dei contatti nella rubrica. Premere 0 per terminare. ")
    stop2 = int(input())
    if stop2 == 0:
        break
