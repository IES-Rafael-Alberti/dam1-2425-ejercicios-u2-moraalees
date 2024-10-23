def comprobar_edad(edad: str) -> bool:
    if edad.isdigit():
        return True
    
    return False


def main():
    edad = input("¿Cuántos años tienes?: ")
    
    while not comprobar_edad(edad):
        edad = input("No creo que eso sea tu edad, escríbala bien: ")
    
    edad = int(edad)
    
    cont = 0
    while cont < edad:
        
        for i in range(1, edad + 1):
            print(f"{cont}, ", end = "")
            cont += 1
            
    print(f"{edad}.")
        
    
if __name__ == "__main__":
    main()