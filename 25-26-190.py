''' 
25.
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario
che ha per chiave la matricola, mentre il valore associato è il voto. Elenca i risultati in ordine crescente di voto
e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali. (GC)

26.
Con riferimento al dizionario del problema precedente, elenca i numeri di matricola degli studenti che hanno ottenuto
una votazione superiore alla media di tutte le votazioni
'''
import statistics
matricola = 0

l_matricole = []
l_voti = []
l_voti_diversi = []
mat_sopra_la_media = []

diz_finale = {}

for i in range(30):
    matricola += 1
    print("Inserire voto del", matricola, "in registro: ")
    voto = int(input())

    l_matricole.append(matricola)
    l_voti.append(voto)

for e in range(len(l_matricole)):
    l_voti.sort()
    diz_finale[l_matricole[e]] = l_voti[e]

for o in range(len(l_matricole)):
    controllo = True
    if l_voti[o] in l_voti_diversi:
        controllo = False
    if controllo:
        l_voti_diversi.append(l_voti[o])

def controllo_media(contatore_mat = 0):
    media_voti = statistics.mean(l_voti)
    for i in range(len(l_matricole)):
        contatore_mat += 1
        if l_voti[i] > media_voti:
            mat_sopra_la_media.append(l_matricole[contatore_mat])
    print("La media dei voti è: ", media_voti)
    return mat_sopra_la_media

l_voti_diversi.sort(reverse=True)
print("Dizionario in ordine di voto: ", diz_finale)
print("Diversi voti usciti in verifica: ", l_voti_diversi)
print("Le matricole sopra la media sono: ", controllo_media())