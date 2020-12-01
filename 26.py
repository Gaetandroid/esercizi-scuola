#Es. 26
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
        q = int(input("Vuoi uscire? Per uscire scrivi -1, se no premi 0 : "))
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