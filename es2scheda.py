lista_A = []
lista_B = []
ciclo = True
while ciclo == True:
    print("Scrivi le parole da aggiungere nella lista A, premi 0 per uscire")
    parola_A = input()
    if parola_A == "0":
        ciclo = False
    else:
        lista_A.append(parola_A)
ntot = len(lista_A)
for i in range(ntot):
    num_B = len(lista_A[i])
    lista_B.append(num_B)
print(lista_B)