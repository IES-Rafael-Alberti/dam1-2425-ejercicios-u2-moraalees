def mostrar_menu():
    print("¡BIENVENIDO AL PROGRAMA!")
    print("Escriba 1 para comenzar el programa.")
    print("Escriba 2 para imprimir el listado.")
    print("Escriba 3 para finalizar el programa.")
   
   
def comprobar_numero(numero: str):
    while numero != "1" and numero != "2" and numero != "3":
        print("*ERROR* - No puedes introducir eso, el número debe ser bien 1, 2 o 3.")
        numero = input("")
        
    return numero


def comenzar_programa():
    # NO SE
    
    
def imprimir_listado():
    # NO SE
    

def finalizar_programa():
    print("¡Un placer!")



def jugar(numero: str):
    if numero == "1":
        comenzar_programa()
        
    if numero == "2":
        imprimir_listado()
        
    if numero == "3":
        finalizar_programa()
    


def main():
    mostrar_menu()
    
    numero = input("")
    
    comprobar_numero(numero)
    
    jugar(numero)
    
    
if __name__ == "__main__":
    main()