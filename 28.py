#Es. 28
ripeti = True
p = 0
r = 0
l1 = []
l2 = []
while ripeti == True:
    p += 1
    r += 1
    print("Immetti nome partecipante ", p)
    nome = input()
    l1.append(nome)
    print("Immetti valore partecipante", p)
    lancio = int(input())
    l2.append(lancio)
    if r == 1:
        stop = input("Premi 0 se hai finito, premi qualsiasi altro tasto per continuare ")
        if stop == "0":
            ripeti = False
        else:
            r = 0

lancio_max = max(l2)
i = l2.index(lancio_max)
i2 = l1[i]
print(l1)
print(l2)
print("Ha vinto", i2, "con", lancio_max, "punti")