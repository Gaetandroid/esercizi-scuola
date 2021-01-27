'''Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista
(nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste),
visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,
segnalando con un messaggio di errore il caso in cui la nazione rihiesta non sia compresa nell'elenco
'''

Nazioni = ["Spagna", "Portogallo", "Francia", "Germania", "Italia", "Olanda", "Belgio", "Svizzera", "Danimarca", "Austria"]
Capitali = ["Madrid", "Lisbona", "Parigi", "Berlino", "Roma", "Amsterdam", "Bruxelles", "Berna", "Copenaghen", "Vienna"]
while True:
    naz = input("Digitare il nome di una nazione per sapere la sua capitale: ")
    naz = naz.capitalize()
    if naz in Nazioni:
        i = Nazioni.index(naz)
        print(Capitali[i])
        print("Per smettere di controllare le nazioni premere 0, per continuare digitare qualsiasi altro tasto: ")
        ripetitore = input()
        if ripetitore == "0":
            break
    else:
        print(naz, "Non è nell'elenco delle nazioni registrate. Per smettere di controllare le nazioni premere 0, per ricominciare digitare qualsiasi altro tasto: ")
        ripetitore2 = input()
        if ripetitore2 == "0":
            break
