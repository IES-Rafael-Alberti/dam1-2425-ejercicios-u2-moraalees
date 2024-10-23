def comprobar_edad(edad: int) -> bool:
    if edad < 0 or edad > 125:
        return False
    
    return True


def comprobar_ingresos(ingresos: float) -> bool:
    if ingresos < 0:
        return False
    
    return True


def tributar_o_no(ingresos: float, edad: int):
    if edad > 16:
        if ingresos >= 1000:
            return print(f"Como tus ingresos son {ingresos}€ y tienes {edad} años te toca tributar.")
        
        else:
            return print(f"Como tus ingresos son {ingresos}€ no te toca tributar, te has librado aunque tengas {edad} años.")
        
    else:
        return print(f"Como no eres mayor de 16 años, ya que tienes {edad}, no tienes que tributar.")
     

def main():
    edad = int(input("Intoduzca su edad: "))
    
    while not comprobar_edad(edad):
        edad = int(input("Intoduzca su edad real: "))
    
    ingresos = float(input("Introduzca sus ingresos: "))
    
    while not comprobar_ingresos(ingresos):
        ingresos = float(input("Eso no pueden ser tus ingresos porque es un número negativo. Introduzca sus ingresos verdaderos: "))

    tributar_o_no(ingresos, edad)


if __name__ == "__main__":
    main()