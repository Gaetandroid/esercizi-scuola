'''
#Es. 1
print("Inserire i voti del primo candidato")
v1 = int(input())
print("Inserire i voti del secondo candidato")
v2 = int(input())
t = v1 + v2
p1 = (v1*100)/t
p2 = 100-p1
print("Il primo candidato ha preso", v1, "voti. Per una percentuale del", p1, "%" )
print("Il primo candidato ha preso", v2, "voti. Per una percentuale del", p2, "%" )
if p1 > p2:
    print("Ha vinto il primo candidato!")
elif p1 < p2:
    print("Ha vinto il secondo candidato!")
elif p1 == p2:
    print("Le elezioni sono finite in parità! Rifare le elezioni")



#Es. 2
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
'''

#Es. 3
lista_stip = []
count = True
persona = 0
ripetizioni = 0
somma = 0
while count == True:
    persona += 1
    ripetizioni += 1
    print("Stipendio persona", persona,"? ")
    stipendi_p = int(input())
    lista_stip.append(stipendi_p)

    if ripetizioni == 3:
        q = int(input("Vuoi uscire? Per uscire scrivi -1, se no premi 0 "))
        ripetizioni = 0
        if q == -1:
            count = False
        else:
            pass
for i in lista_stip:
    somma += i
l = len(lista_stip)
print(lista_stip)
mediastip = somma/l
print(mediastip)