def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False


def crear_triangulo(numero: int):
    for i in range(1, numero + 1, 2):
        fila = ""
        for j in range(i, 0, -2):
            fila += str(j) + " " 
        print(fila.strip())


def main():
    numero = input("Introduce un número entero positivo: ")
    
    while not comprobar_entero(numero):
        numero = input("Escribe un número entero positivo por favor, cosa que lo que has puesto no es: ")

    numero = int(numero)
    crear_triangulo(numero)

    
if __name__ == "__main__":
    main()