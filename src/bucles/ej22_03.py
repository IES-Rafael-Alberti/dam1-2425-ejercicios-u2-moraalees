def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False



def contador_numeros(numero: int):
    cont = 1
    while cont < numero:
            
        for i in range(1, numero, 2):
            print(f"{cont}, ", end ="")
            cont = cont + 2
                
    print(f"{numero}.")
    return numero



def main():
    numero = input("Escriba un número entero positivo: ")
        
    while not comprobar_entero(numero) or numero == "0":
        numero = input("Te dije que debía ser un número entero positivo: ")
    
    numero = int(numero)
    
    contador_numeros(numero)
    
    
if __name__ == "__main__":
    main()