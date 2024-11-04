def comprobar_entero(edad: str) -> bool:
    if edad.isdigit():
        return True
    
    return False


def comprobar_edad(edad: str):
    edad = input("Introduzca su edad por favor: ")
    
    while not comprobar_entero(edad):
        print("Esa no puede ser tu edad mentiroso/a, escribe la de verdad...")
        edad = input("Introduzca su edad por favor: ")
        
    edad = int(edad)
        
    if edad > 18:
        si_mayor_de_edad = edad - 18
        return print(f"Eres mayor de edad porque tienes {edad} años, lo fuiste desde hace {si_mayor_de_edad} años.")
    
    elif edad == 18:
        return print(f"Sí eres mayor de edad, de hecho cumpliste 18 años este mismo año.")
    
    else:
        no_mayor_de_edad = 18 - edad
        return print(f"No eres mayor de edad, tienes {edad} años y te faltan {no_mayor_de_edad} años por cumplir, sigues siendo un niño...")
    

def main():
    edad = 0
    (comprobar_edad(edad))
    
    
if __name__ == "__main__":
    main()