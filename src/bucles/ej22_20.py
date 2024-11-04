def comprobar_letra(letra: str) -> bool:
    if (len(letra)) > 1 or letra.isdigit():
        return False
    
    return True


def buscar_letra(frase: str, letra: str):
    posicion = 0
    
    for caracter in frase:
        
        if caracter == " ":
            posicion += 1
        
        elif letra != caracter:
            posicion += 1
            print(f"\nLa {letra} no coincide en el puesto {posicion} de la frase, ya que es una {caracter}.")
            
        elif letra == caracter:
            posicion += 1
            print(f"\nLa {letra} coincide en el puesto {posicion} de la frase, ya que es una {caracter} igual.")
    
    return posicion
        


def main():
    frase = input("Escriba lo primero que se le venga a la cabeza: ")
    letra = input("Escriba una letra cualquiera: ")
    
    while not comprobar_letra(letra):
        letra = input("Escriba solo una letra, no números ni nada...: ")
    
    buscar_letra(frase, letra)
    
    
if __name__ == "__main__":
    main()