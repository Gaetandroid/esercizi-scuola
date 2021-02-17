'''Risolvi la seguente variante del problema della Gestione delle lavorazioni del Coding di pag. 144.
Scrivi il programma per una macchina che accetti lavorazioni con un codice identificativo di tipo stringa:
al momento dell'inserimento di un nuovo codice occorre specificare anche la priorità della lavorazione
che può essere uguale a 0 (urgente), 1 (priorità alta) e 2 (priorità bassa), Ci sono due code di attesa: una
per l'alta priorità e una per la bassa priorità. Se la priorità è 0 il codice della lavorazione viene inserito
all'inizio della coda ad alta priorità, se la priorità è 1 il codice della lavorazione è inserito alla fine della
coda ad alta priorità e, infine, se la priorità è 2, il codice è inserito alla fine della coda a bassa priorità.
Quando la macchina termina una lavorazione, manda in esecuzione la lavorazione che si trova intesta a
una coda ottenuta dall'accodamento della coda a bassa priorità di seguito a quella di priorità alta. (GC)
'''
coda_alta_priorita = []
coda_bassa_priorita = []
lista_operazioni = [1, 2, 3, 4]
def menu():
    print("--------------------------")
    print("1. Accomodamento nuova lavorazione")
    print("2. Esecuzione di una lavorazione")
    print("3. Visualizza coda lavorazioni")
    print("4. Fine lavoro")
    print("--------------------------")

def scegli_OP():
    while True:
        scelta_OP = int(input("Inserisci la tua scelta: "))
        while scelta_OP not in lista_operazioni:
            print("Valore non ammesso, inserire un valore da 1 a 4.")
            scelta_OP = input()
        break
    return scelta_OP

def accoda():
    while True:
        codlav = input("Inserire codice della lavorazione: ")
        indice_priorita = int(input("Definire l'indice di priorità: 0, 1, 2. "))
        if indice_priorita == 0:
            coda_alta_priorita.insert(0, codlav)
            break
        elif indice_priorita == 1:
            coda_alta_priorita.insert(-1, codlav)
            break
        elif indice_priorita == 2:
            coda_bassa_priorita.append(codlav)
            break
        else:
            print("Indice di priorità non compatibile, inserire un valore da 0 a 2.")

def esegui():
    if len(coda_alta_priorita) == 0 and len(coda_bassa_priorita) == 0:
        print("Code lavorazioni vuote")
    else:
        while len(coda_alta_priorita) != 0:
            lavoro_AP = coda_alta_priorita.pop(0)
            print("Avvio lavorazione:", lavoro_AP)
        print("Coda di lavori ad alta priorità: libera. Avvio lavorazioni della coda di bassa priorità...")
        while len(coda_bassa_priorita) != 0:
            lavoro_BP = coda_bassa_priorita.pop(0)
            print("Avvio lavorazione: ", lavoro_BP)

def visualizza():
    for i in range(len(coda_alta_priorita)):
        codlav_AP = coda_alta_priorita[i]
        print("Codice lavorazione ad alta priorità: ", codlav_AP)
    for e in range(len(coda_bassa_priorita)):
        codlav_BP = coda_bassa_priorita[e]
        print("Codice lavorazione a bassa priorità: ", codlav_BP)

def main():
    while True:
        menu()
        scelta = scegli_OP()
        if scelta == 1:
            accoda()
        elif scelta == 2:
            esegui()
        elif scelta == 3:
            visualizza()
        else:
            print("Fine lavoro")
            break

main()