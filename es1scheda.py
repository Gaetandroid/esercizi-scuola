print("Inserire una parola, ")
nome_p = input()
if nome_p == nome_p[::-1]:
    print("La parola è palindroma")
else:
    print("La parola non è palindroma")