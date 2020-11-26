#Es. 4
lista_v = []
count = True
ng = 0
ripetizioni = 0
somma = 0
while count == True:
    ng += 1
    ripetizioni += 1
    print("Quanti veicoli sono entrati il giorno", ng,"? ")
    veicoli = int(input())
    lista_v.append(veicoli)

    if ripetizioni == 3:
        q = int(input("Vuoi uscire? Per uscire scrivi 0, se no premi 1 : "))
        ripetizioni = 0
        if q == 0:
            count = False
        else:
            pass
for i in lista_v:
    somma += i
print("In", ng,"giorni, sono transitati", somma, "veicoli")
