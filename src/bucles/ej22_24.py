def es_primo(numero):
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        
    return True



def pedir_numeros():
    contador_primos = 0
    
    while True:
        numero = input("Introduzca un número: ")
        
        if numero == "0":
            break
        
        if not numero[1:].isdigit() and not len(numero) == 1:
            print("Escribe solo números enteros mayores que 1")
            continue
        
        if numero.startswith("-"):
            print("Escribe solo números enteros mayores que 1")
            continue
        
        if numero == "1":
            print("Escribe solo números enteros mayores que 1")
            continue
        
        else:
            numero = int(numero)
            if es_primo(numero):
                contador_primos += 1
            numero = str(numero)
            
            
    print(f"En total has escrito {contador_primos} número/s primo/s.")



def main():
    pedir_numeros()

    
if __name__ == "__main__":
    main()