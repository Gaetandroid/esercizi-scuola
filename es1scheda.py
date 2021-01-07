'''Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un
palindromo (parole che si leggono uguali anche al contrario) oppure meno.'''

print("Inserire una parola, ")
nome_p = input()
if nome_p == nome_p[::-1]:
    print("La parola è palindroma")
else:
    print("La parola non è palindroma")