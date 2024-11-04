def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True

    return False



def dividir_sumar_numero(numero: str) -> int:
    sumatorio = 0
    
    for caracter in numero:
        caracter = int(caracter)
        sumatorio = caracter + sumatorio
        caracter = str(caracter)
    
    print(f"La suma de todos los números escritos en {numero} es {sumatorio}")

    return sumatorio



def main():
    numero = input("Escriba un número entero positivo: ")
    
    while not comprobar_entero(numero):
        numero = input("Te dije un número positivo entero, inténtelo de nuevo: ")
    
    dividir_sumar_numero(numero)
    
    
    
if __name__ == "__main__":
    main()