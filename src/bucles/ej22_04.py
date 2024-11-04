def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False


def cuentra_atras(cont: int, numero: int):
    while cont > 0:
        
        for i in range(0, numero):
            print(f"{cont}, ", end ="")
            cont = cont - 1
            
    print(f"0.")
            


def main():
    numero = input("Escriba un número entero positivo: ")
    
    while not comprobar_entero(numero):
        numero = input("Te dije que debía ser un número entero positivo: ")
        
    numero = int(numero)
    cont = numero
    cuentra_atras(cont, numero)
    
if __name__ == "__main__":
    main()