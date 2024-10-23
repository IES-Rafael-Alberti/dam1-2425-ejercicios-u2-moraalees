def pedir_edad() -> int:
    edad_incorrecta = True
    
    while edad_incorrecta:
        try:
            edad = int(input("Introduzca su edad: "))
            
            if edad < 0:
                raise ValueError("La edad debe ser un número entero positivo")
            if edad == 0:
                raise ValueError("La edad debe ser un número entero positivo mayor que cero")
            if edad > 125:
                raise ValueError("La edad debe ser menor un número inferior a 125")
            
            edad_incorrecta = False
        except ValueError as e:
            print(f"*ERROR* - {e}. Inténtalo de nuevo.")
        except Exception as e:
            print(f"*ERROR* - {e}. Inténtalo de nuevo.")
            
    return edad
    
    
def mostrar_anios_cumplidos(edad: int):
    
    for i in range(1, edad + 1):
        if i == edad:
            print(f"{i}.")
        else:
            print(i, end=", ")
        

def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años:")
    mostrar_anios_cumplidos(edad)
    
    
if __name__ == "__main__":
    main()