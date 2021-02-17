'''Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado ax + b = 0.
Il processo risolutivo dipende dai valori assunti dai coefficienti a e b secondo la tabella che segue
per a == 0 e b == 0: indeterminata
per a == 0 e b != 0: impossibile
per a != 0 e b == 0: x = 0
per a != 0 e b != 0: x = -b/a'''

a = int(input("Immetti il parametro [a] "))
b = int(input("Immetti il parametro [b] "))
print("L'equazione da risolvere è: ax + b = 0\nL'equazione risulta quindi: x = -b/a")
if a == 0 and b == 0:
    print("L'equazione è indeterminata poichè risulta: x = -( 0 / 0 )")
elif a == 0 and b != 0:
    print("L'equazione è impossibile poichè risulta: x = -(",b,"/ 0 )")
elif a != 0 and b == 0:
    print("L'equazione è determinata poichè risulta: x = 0")
else:
    print("L'equazione è determinata poichè risulta: x =", -(b/a))