def comprobar_numero(cadena: str) -> bool:
    """
    Comprueba si la cadena de caracteres es un número positivo entero.
    """
    return cadena.isdigit()


def introducir_numero(msj: str) -> int:
    # -1 Si es fin / int positivo si es int / None Entrada inválida
    valor = input(msj).strip()
    
    if comprobar_numero(valor) == True:
        return int(valor)
    elif valor.lower() == "fin":
        return -1
    else:
        return -2
    


   
def main():
    
    cantidad = 0
    suma = 0
    media = 0
    salir = False
    
    
    while not salir:
        num = introducir_numero("Introduzca un número: ")
        
        if num == -1:
            # fin
            salir = True
        elif num == -2:
            print("Entrada inválida.")
        else:            
            cantidad += 1
            suma += num

    if cantidad != 0:
        media = suma / cantidad
        
        
    print(f"{suma} {cantidad} {media}")
    
if __name__ == "__main__":
    main()