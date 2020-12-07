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
