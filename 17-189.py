'''Costruisci un dizionario ottenuto da quello dell'esercizio precedente invertendo il ruolo di chiave e valore.
Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale
'''
def crea_dict(Nazioni, Capitali, dizionario={}):
    for i in range(len(Nazioni)):
        dizionario[Capitali[i]] = Nazioni[i]
    return dizionario

def main():
    Nazioni = ["Spagna", "Portogallo", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Svizzera", "Danimarca", "Austria"]
    Capitali = ["Madrid", "Lisbona", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Berna", "Copenaghen", "Vienna"]
    d = crea_dict(Nazioni, Capitali)
    while True:
        print("Inserire il nome di una capitale per ricevere il nome della sua nazione: ")
        cap = input()
        cap = cap.capitalize()
        if cap not in d:
            print("Capitale non trovata.\nPremere 0 per chiudere o premere qualsiasi altro tasto per reinserire la capitale: ")
            controllo = input()
            if controllo == "0":
                break
        else:
            naz = d.get(cap)
            print("La nazione è:", naz, "\nPremere 0 per chiudere o premere qualsiasi altro tasto per reinserire la capitale:")
            controllo2 = input()
            if controllo2 == "0":
                break

main()