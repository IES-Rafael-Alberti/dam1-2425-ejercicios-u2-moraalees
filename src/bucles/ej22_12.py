def comprobar_letra(letra: str) -> bool:
    if (len(letra)) > 1 or letra.isdigit():
        return False
    
    return True



def letra_en_frase(frase: str, letra: str):
    cont = 0
    for cantidad in frase:
        if cantidad == letra:
            cont += 1
    print(f"La {letra} aparece en la frase {cont} veces.")
    
    return cont



def main():
    frase = input("Escriba algo, una frase si eso: ").lower()
    letra = input("Ahora cualquier letra: ").lower()
    
    while not comprobar_letra(letra):
        letra = input("Escribe solo una letra por favor: ")
        
    letra_en_frase(frase, letra)

    
    
if __name__ == "__main__":
    main()