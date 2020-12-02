def transformbin(dec):
    binario = ""
    while dec > 0:
        if dec%2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        dec = int(dec/2)
    print(binario)

print("Inserisci il numero decimale: ")
decimale = int(input())
transformbin(decimale)