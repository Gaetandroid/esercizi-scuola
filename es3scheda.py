'''In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto
"rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni
consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".
Scrivi una programma in grado di tradurre una parola o frase passata tramite input in
"rövarspråket".
Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende
tradume un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una
nuova parola da parte dell'utente. '''

ciclo = True
while ciclo == True:
    print("Scrivi il testo che vuoi tradurre in rovarspraket: ")
    parola = input()
    parola = parola.lower()
    vocali = ["a", "e", "i", "o", "u", "à", "è", "ì", "ò", "ù", " ", ".", ",", ";", ":", "?", "!"]
    p_trad = ""
    for i in range(len(parola)):
        if parola[i] not in vocali:
            p_trad += parola[i]+"o"+parola[i]
        else:
            p_trad += parola[i]
    print(p_trad)
    print("Vuoi tradurne un altra? Digita Si per continuare, digita No per smettere")
    risp = input()
    risp = risp.lower
    if risp == "si":
        pass
    else:
        ciclo = False
