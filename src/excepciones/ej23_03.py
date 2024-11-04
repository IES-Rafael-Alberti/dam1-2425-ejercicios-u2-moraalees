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

def cuenta_atras(numero: int):
    cont = numero
    while cont > 0:
        
        for i in range(0, numero):
            print(f"{cont}, ", end ="")
            cont = cont - 1
            
    print(f"0.")
    


def main():
    numero = pedir_numero()
    
    print(f"La cuenta atrás desde {numero} es la siguiente: ")
    cuenta_atras(numero)
    
    
if __name__ == "__main__":
    main()