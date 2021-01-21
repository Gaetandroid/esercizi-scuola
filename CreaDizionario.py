from googletrans import Translator
translator = Translator()

def settimana_ita():
    listag = []
    d_ita = {}
    for g in range(7):
        print("Giorno", g+1, ":")
        giorni = input()
        listag.append(giorni)
        d_ita["Giorno " + str(g+1)] = listag[g]
    return d_ita

def week_eng(d_ita):
    d_eng = {}
    listag = list(d_ita.values())
    for d in range(len(listag)):
        result = translator.translate(listag[d], src='it', dest='en')
        d_eng[listag[d]] = result.text
    return d_eng

def main():
    settimana = settimana_ita()
    print(settimana)
    week = week_eng(settimana)
    print(week)

main()