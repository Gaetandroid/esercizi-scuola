from random import randint
ciclo = True
città = []
ltmax = []
ltmin = []
n = 0
escursione_max = randint(1, 100)
while ciclo == True:
    n += 1
    print("Digita nome della città numero", n)
    nomec = input()
    città.append(nomec)
    print("Digita il valore massimo dell'escursione termica giornaliera di", nomec)
    vtmax = int(input())
    ltmax.append(vtmax)
    print("Digita il valore minimo dell'escursione termica giornaliera di", nomec)
    vtmin = int(input())
    ltmin.append(vtmin)
    stop2 = input("Premi 0 se hai finito le città, premi qualsiasi altro tasto per continuare ")
    if stop2 == "0":
        ciclo = False
    else:
        pass

ciclo2 = True
while ciclo2 == True:
    print("\nPremi 'c' per vedere una lista delle città inserite. \nPremi 'max' per vedere una lista dei valori massimi dell'escursione termica inseriti. \nPremi 'min' per vedere una lista dei valori minimi dell'escursione termica inseriti. \nPremi 'q' per uscire. \nPremi qualsiasi altro tasto per vedere il limite del contatore e le città che NON lo rispettano")
    output = input()
    if output == "c":
        print("\n", città)
    elif output == "max":
        print("\nValori massimi escursione termica: ", ltmax)
    elif output == "min":
        print("\nValori minimi escursione termica: ", ltmin)
    elif output == "q":
        ciclo2 = False
    else:
        ciclo3 = True
        while ciclo3 == True:
            print("Scegli un indice esistente nelle 3 liste per selezionare una città e la sua escursione termica")
            indicef = int(input())
            escursione_termica = ltmax[indicef] - ltmin[indicef]
            diffesc = escursione_max - escursione_termica
            print("\nValore massimo del contatore: ", escursione_max)
            if diffesc > 0:
                print("\nL'escursione termica di", città[indicef],"è di", escursione_termica,"gradi. Rientra nel range prefissato per", diffesc,"gradi")
                ciclo3 = False
            else:
                print("\nL'escursione termica di", città[indicef],"è di", escursione_termica,"gradi. Non rientra nel range prefissato per", diffesc,"gradi")
                ciclo4 = True
                while ciclo4 == True:
                    print("\nSto alzando il range del contatore per far entrare l'escursione termica di", città[indicef])
                    diffesc += 1
                    if diffesc > 0:
                        print("\nOra i valori sono stabilizzati! Premi 't' per tornare al menù principale, premi qualsiasi altro tasto per chiudere.")
                        finale = input()
                        if finale == "t":
                            ciclo3 = False
                            ciclo4 = False
                        else:
                            ciclo2 = False
                            ciclo3 = False
                            ciclo4 = False
                    else:
                        pass
