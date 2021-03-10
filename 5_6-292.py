'''Elenca proprietà e metodi della classe prodotto.
Definisci il metodo assegna_prezzo della classe prodotto (GC)
'''

class Prodotto():
    def __init__(self, quantita, materiale, oggetto):
        self.quantita = quantita
        self.materiale = materiale
        self.oggetto = oggetto
    def assegna_prezzo(self):
        diz_obj = {
            1: "Assi",
            2: "Lastre",
            3: "Oggetti",
            4: "Gioielli"
        }  

        diz_mat = {
            1: "Legno",
            2: "Ferro",
            3: "Pietre preziose"
        }

        try:
            obj = list(diz_obj.values())[self.oggetto-1]
            inc_prezzo = 0
            
            if obj in diz_obj.values():
                if obj == "Assi":
                    inc_prezzo += 5
                elif obj == "Lastre":
                    inc_prezzo += 10
                elif obj == "Oggetti":
                    inc_prezzo += 15
                else:
                    inc_prezzo += 20
            
                inc_prezzo *= self.quantita
                mat = list(diz_mat.values())[self.materiale-1]

                try:
                    if mat in diz_mat.values():
                        if obj == "Legno":
                            inc_prezzo += 5
                        elif obj == "Ferro":
                            inc_prezzo += 10
                        else:
                            inc_prezzo += 20
                except:
                    print("Il prodotto scelto non esiste, ci scusiamo per l'inconveniente.")
            
                return inc_prezzo
        except:
            print("Il prodotto scelto non esiste, ci scusiamo per l'inconveniente.")

        
def main():
    print("\n|------------------|\nBenvenuto nel supermercato, cosa vuoi comprare? \nScrivere il numero del prodotto. ")
    print("------------------\n1: Assi\
        \n2: Lastre\
        \n3: Oggetti\
        \n4: Gioielli\n------------------")

    prodotto_da_comprare = int(input())
    numero_di_prodotti = int(input("------------------\nQuanti ne vuoi?\n------------------\n"))

    print("------------------\nLista materiali:\
        \n1: Legno\
        \n2: Ferro\
        \n3: Pietre preziose\n------------------")
    
    materiale = int(input("Di che materiale vuoi l'oggetto? \nScrivere il numero del prodotto.\n------------------\n"))

    prodotto1 = Prodotto(numero_di_prodotti, materiale, prodotto_da_comprare)
    conto = prodotto1.assegna_prezzo()

    if conto != None:
        print("Costo totale del prodotto:", conto, "Euro")
        print("|------------------|")
    else:
        print("|------------------|")


main()