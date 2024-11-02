def listado():
    contador_impar = 0
    contador_par = 0
    
    while True:
        numero = input("Introduzca un número entero positivo: ")
        
        if numero == "0":
            break
        
        if numero.startswith("-"):
            print("Escribe solo números positivos enteros...: ")
            continue
            
        if not numero[1:].isdigit() and not len(numero) == 1:
            print("Escribe solo números positivos enteros...: ")
            continue
        
        for caracter in numero:
            caracter = int(caracter)
            if caracter % 2 == 0:
                contador_par += 1
                print(f"{caracter} es par")
            if caracter % 2 != 0:
                contador_impar += 1
                print(f"{caracter} es impar")
                
                
    print(f"En total, has introducido {contador_impar} número/s impar/es y {contador_par} número/s par/es")
        

def main():
    listado()
    
    
if __name__ == "__main__":
    main()