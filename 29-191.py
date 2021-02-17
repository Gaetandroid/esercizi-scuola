'''Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e la
tassazione media. Nell'esempio, per un reddito di 45.000 euro e un imposta di 13.420 euro, la tassazione
media è 13.420/45.000*100=29,82%
Si nota che un reddito di 45000 euro si colloca nella fascia limitata dal valore 55000 e implica un'imposta
di: 6960+(45000-28000)*38/100.
L'osservazione suggerisce di creare opportune strutture dati da utilizzare nel calcolo dell'imposta. Per
esempio si può pensare di creare un dizionario che associa al limite superiore dì ogni fascia dì reddito
una tupla con: limite inferiore della fascia, imposta dovuta per le fasce precedenti, aliquota della fascia.
Per trattare l’ultima fascia si introduce un limite superiore impossibile da raggiungere, come 10**12
(ovvero 1000 miliardi).
Il dizionario si costruisce a programma partendo dagli array:
limiti = {15000, 28000, 55000, 75000, 1000000000000]
aliquota = [23, 27, 38, 41, 43] (GC)
'''
fascia_redditi = {
    15000: 0.23,
    28000: 0.27,
    55000: 0.38,
    75000: 0.41,
    10**12: 0.43,
}

imposta = 0
while True:
    stipendio = int(float(input("A quanto ammonta lo stipendio mensile?\n")))
    if stipendio <= 10**12:
        for i in range(len(fascia_redditi)):
            l_fascia_redditi = list(fascia_redditi)

            if stipendio > l_fascia_redditi[i] - l_fascia_redditi[i-1]:
                if i == 0:
                    imposta += l_fascia_redditi[i] * fascia_redditi.get(l_fascia_redditi[i])
                    stipendio -= l_fascia_redditi[i]

                else:
                    imposta += (l_fascia_redditi[i] - l_fascia_redditi[i-1]) * fascia_redditi.get(l_fascia_redditi[i])
                    stipendio -= l_fascia_redditi[i] - l_fascia_redditi[i-1]

            else:
                imposta += stipendio * fascia_redditi.get(l_fascia_redditi[i])
                stipendio = 0
                
        print(imposta)
    else:
        print("Impossibile definire un'imposta per questo reddito.")
        
    stop = input("Premere 0 per chiudere o qualsiasi altro tasto per continuare. ")
    if stop == "0":
        break