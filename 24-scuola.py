'''Alla fine della giornata di elezioni per il ballottaggio tra due candidati, si acquisiscono i voti ottenuti dai due candidati.
Scrivi il programma che calcoli le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore'''

print("Inserire i voti del primo candidato")
v1 = int(input())
print("Inserire i voti del secondo candidato")
v2 = int(input())
t = v1 + v2
p1 = (v1*100)/t
p2 = 100-p1
print("Il primo candidato ha preso", v1, "voti. Per una percentuale del", p1, "%" )
print("Il primo candidato ha preso", v2, "voti. Per una percentuale del", p2, "%" )
if p1 > p2:
    print("Ha vinto il primo candidato!")
elif p1 < p2:
    print("Ha vinto il secondo candidato!")
elif p1 == p2:
    print("Le elezioni sono finite in parità! Rifare le elezioni")
