def pedir_libro():
    contador_digitos = 0
    contador_lineas = 0
    
    while True:
        libro = input("Libro: ")
        
        if libro == "*":
            break
        
        if libro == "/":
            print(f"Línea completa. Aparecen {contador_digitos} dígitos numéricos.")
            contador_digitos = 0
            contador_lineas += 1
        
        for caracter in libro:
            if caracter.isdigit():
                contador_digitos += 1

    print(f"Fin. Se leyeron {contador_lineas} líneas completas.")


def main():
    pedir_libro()
    
    
if __name__ == "__main__":
    main()