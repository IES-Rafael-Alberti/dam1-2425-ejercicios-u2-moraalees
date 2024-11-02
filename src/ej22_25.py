def contador(frase: str):
    palabras = frase.split()

    palabra_mas_larga = ""
    
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
            
    cantidad_palabras = len(palabras)

    print(f"La palabra más larga es {palabra_mas_larga}.")
    print(f"Has escrito {cantidad_palabras} palabra/s.")


def main():
    frase = input("Por favor, ingresa una frase: ")

    contador(frase)

    
if __name__ == "__main__":
    main()