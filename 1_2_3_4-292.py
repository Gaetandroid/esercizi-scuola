'''Crea una classe Atleta per rappresentare le informazioni su un giocatore. 
La classe deve contenere un attributo booleano chiamato visita_medica.
Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra in cui gioca. (GC)
Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visita_medica uguale a True
Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore.
'''
class Atleta():
    def __init__(self, nome_squadra, visita_medica=False):
        self.nome_squadra = nome_squadra.capitalize()
        self.visita_medica = visita_medica
    def squadra(self):
        print("L'atleta gioca nella squadra:", self.nome_squadra)
    def effettua_visita(self):
        print("L'atleta sta effettuando una visita...\n...\nVisita effettuata con successo!")
        self.visita_medica = True
    def visualizza_dati(self):
        if self.visita_medica:
            print("L'atleta gioca nella squadra:", self.nome_squadra, "\nHa effettuato la visita medica.")
        else:
            print("L'atleta gioca nella squadra:", self.nome_squadra, "\nNon ha ancora effettuato la visita medica.")

def main():
    squadra = input("Inserire squadra atleta: ")
    atleta_1 = Atleta(squadra)
    print("------------------")
    while True:
        print("Premere E, per far effettuare la visita all'atleta.\nPremere V, per visualizzare i dati dell'atleta.\
            \nPremere qualsiasi altro tasto per chiudere il programma.")
        risp = input()
        risp = risp.upper()
        if risp == "E":
            atleta_1.effettua_visita()
        elif risp == "V":
            atleta_1.visualizza_dati()
        else:
            print("------------------")
            break

main()