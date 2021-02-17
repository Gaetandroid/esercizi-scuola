'''In un laboratorio di analisi i pazienti sono sottoposti a un esame specialistico
secondo l'ordine di arrivo, scrivi il programma che consenta di registrare i nomi
dei pazienti man mano che arrivano. Visualizza poi il nome del paziente che deve
essere sottoposto all'esame perchè è il primo della coda in attesa.
(Utilizzare una struttura di coda)'''

def registra_coda(coda = [], stop = False):
    while stop == False:
        r = input("Registrare i nomi dei pazienti nella coda. Scrivere stop per finire di registrarli: ")
        r = r.capitalize()
        if r == "Stop":
            stop = True
        else:
            coda.append(r)
    return coda

def uscita_dalla_coda(stop2 = False):
    global l_coda
    print("Il primo della coda, ", l_coda[0], ", si può sottoporre all'esame. Entri pure.")
    while stop2 == False:        
        print("Il paziente", l_coda[0], ", ha finito!")
        l_coda.pop(0)
        if len(l_coda) == 0:
            print("...")
            print("Questo era l'ultimo, non c'è più coda.")
            stop2 = True
        else:
            print("Ora tocca a...", l_coda[0], ". Entri pure.")

l_coda = registra_coda()
print("La coda è formata da:", l_coda)
uscita_dalla_coda()