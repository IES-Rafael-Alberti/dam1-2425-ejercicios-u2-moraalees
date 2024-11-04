def pedir_numero() -> int:
    numero_incorrecto = True
    
    while numero_incorrecto:
        try:
            numero = int(input("Introduzca un número entero positivo: "))
            
            if numero < 0:
                raise ValueError("*ERROR* - El número debe ser mayor que 0")
            
            if numero == 0:
                raise ValueError("*ERROR* - El número no puede ser 0")
        
            numero_incorrecto = False
        except ValueError as e:
            print(f"{e}. Inténtelo de nuevo.")
            
        except Exception as e:
            print(f"*ERROR* - {e} Inténtalo de nuevo.")

    return numero


def secuencia_impares(numero: int):
    cont = 1
    while cont < numero:
            
        for i in range(1, numero, 2):
            print(f"{cont}, ", end ="")
            cont = cont + 2
                
    print(f"{numero}.")
    


def main():
    numero = pedir_numero()
    
    print(f"La secuencia de números impares desde 1 hasta {numero} es la siguiente: ")
    secuencia_impares(numero)


if __name__ == "__main__":
    main()