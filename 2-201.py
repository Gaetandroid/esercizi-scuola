'''Data la parabola y = ax² + bx + c, definisci due funzioni per calcolarne i punti significativi: vertice e fuoco.
Le due funzioni ricevono come parametri a, b, c e restituiscono il valore calcolato'''
 
def fuoco(a, b, c):
    delta = b**2 - 4*a*c
    x_fuoco = -b/2*a
    y_fuoco = (1-delta)/4*a
    return x_fuoco, y_fuoco

def vertice(a, b, c):
    delta = b**2 - 4*a*c
    x_vertice = -b/2*a
    y_vertice = -delta/4*a
    return x_vertice, y_vertice

def main():
    a = int(input("Definisci il valore di a: "))
    b = int(input("Definisci il valore di b: "))
    c = int(input("Definisci il valore di c: "))
    risposta_fuoco = fuoco(a, b, c)
    risposta_vertice = vertice(a, b, c)
    print("Le coordinate del fuoco della parabola sono: ", risposta_fuoco,"\nMentre quelle del vertice della parabola sono: ", risposta_vertice)

main()