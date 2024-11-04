def comprobar_entero(numero: str) -> bool:
    if numero[1:].isdigit() or (len(numero) == 1 and numero.isdigit()):
        return True
    
    return False



def sumatorio_numeros(numero: int):
    sumatorio = 0
    
    while numero != 0:
        sumatorio = sumatorio + numero
        numero = int(input("Siga escribiendo (Si desea parar la suma escriba 0): "))
        
    print(f"La suma de todo lo que has puesto es de {sumatorio}")


def main():
    numero = input("Escriba un número entero: ")
    
    while not comprobar_entero(numero):
        numero = input("Un número entero, no eso, por favor: ")
        
    numero = int(numero)
    
    sumatorio_numeros(numero)
    
    
if __name__ == "__main__":
    main()