''' A un concorso pubblico hanno partecipato due candidati di cui si conoscono i nomi e i punteggi conseguiti.
Visualizza l'elenco dei due candidati prima in ordine alfabetico e poi in ordine decrescente di punteggio'''

print("Inserire i voti e il nome del primo candidato")
v1 = int(input())
n1 = input()
print("Inserire i voti e il nome del secondo candidato")
v2 = int(input())
n2 = input()
lista1 = [n1, n2]
lista2 = [v1, v2]
lista1.sort()
lista2.sort(reverse=True)
print(lista1)
print(lista2)