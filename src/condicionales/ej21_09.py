def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False


def comprobar_edad(edad: int):
    if edad < 4:
        return print(f"Ains, que tienes {edad} años... Entras gratis chiquitín.")
    elif 4 <= edad <= 18:
        return print(f"Como tienes {edad} años, tienes que pagar 5€. ¡Pásalo bien!")
    else:
        print(f"A ver, como tienes {edad} años tienes que pagar 10€, lo siento mucho.")



def main():
    edad = input("Introduzca su edad antes de entrar: ")
    while not comprobar_entero(edad):
        edad = input("Pero qué dices, escriba su edad bien anda: ")
        
    edad = int(edad)
    comprobar_edad(edad)
    
if __name__ == "__main__":
    main()