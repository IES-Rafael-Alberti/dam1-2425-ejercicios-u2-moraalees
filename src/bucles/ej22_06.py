def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False



def contador_veces(numero: int):
    for i in range(1, numero + 1):
        print("*" * i)


def main():
    numero = input("Escriba un número entero positivo: ")
    
    while not comprobar_entero(numero):
        numero = input("El número debe ser entero y positivo por favor: ")
        
    numero = int(numero)
    
    contador_veces(numero)
    
    

if __name__ == "__main__":
    main()