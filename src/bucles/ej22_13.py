def eco_palabra():
    cadena = ""
    while cadena != "salir":
        cadena = input().strip().lower()
        if cadena != "salir":
            print(f"Eco: {cadena}")

        

def main():
    print("Escriba lo que quiera: ")
        
    eco_palabra()
    
        
        
if __name__ == "__main__":
    main()