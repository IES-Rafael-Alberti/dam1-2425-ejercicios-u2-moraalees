def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False


def comprobar_numero(numero: int):
    if numero % 2 == 0:
        return True
    else:
        return False



def main():
    numero = input("Escriba un número para comprobarte si es par o impar: ")
    
    while not comprobar_entero(numero):
        numero = input("Escriba un número entero de verdad: ")
    
    numero = int(numero)
    
    if comprobar_numero(numero) == True:
        print("¡Ese número es par, espero que lo hayas adivinado!")
        
    elif comprobar_numero(numero) == False:
        print("¡Ese número es impar, espero que lo hayas adivinado!")
    
if __name__ == "__main__":
    main()