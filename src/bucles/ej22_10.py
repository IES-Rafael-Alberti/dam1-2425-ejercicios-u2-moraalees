def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True

    return False


def comprobar_primo(numero: int):
    primo = True
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"{numero} es un número primo.")
        
    else:
        print(f"{numero} no es un número primo.")



def main():
    numero = input("Introduce un número entero positivo: ")
    
    while not comprobar_entero(numero):
        numero = input("Perdone pero eso no es un número entero positivo... Ponga uno: ")
        
    numero = int(numero)

    comprobar_primo(numero)
    
    
if __name__ == "__main__":
    main()