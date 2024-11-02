def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False



def sumatorio_numeros(numero: str):
    sumatorio = 0
    
    while numero != "0" and numero.isdigit():
        numero = int(numero)
        sumatorio = sumatorio + numero
        numero = input("Siga escribiendo (Si desea parar la suma escriba 0): ")
        
    if numero == "0":
        print(sumatorio)
    else:
        print("Ya la has cagado, te dije que solo se valían números enteros positivos...")
        


def main():
    numero = input("Escriba un número entero positivo: ")
    
    while not comprobar_entero(numero):
        numero = input("Si escribes un número entero positivo mejor, anda inténtalo: ")
    
    sumatorio_numeros(numero)
    
    
    
    
    
if __name__ == "__main__":
    main()