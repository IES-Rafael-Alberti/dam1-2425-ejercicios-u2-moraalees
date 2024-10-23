def comprobar_mayor_cero(numero: float) -> bool:
    if numero >= 0:
        return True
    
    return False


def comprobar_entero(numero: str) -> bool:
    if numero.isdigit():
        return True
    
    return False


def formula_capital(cantidad: float, interes: float) -> float:
    cantidad *= (1 + interes / 100)
    return print(cantidad)

def main():
    amount = float(input("Introduzca una cantidad a invertir: "))
    
    while not comprobar_mayor_cero(amount):
        amount = float(input("No puede ser negativa una inversión, escriba otra: "))
        
        
    interest = float(input("Introduzca su interés anual en medida de porcentaje: "))
    
    while not comprobar_mayor_cero(interest):
        interest = float(input("No puede ser un número negativo, escriba otro interés: "))
        
        
    num_anios = input("Por último, escriba un número de años: ")
    
    while not comprobar_entero(num_anios):
        num_anios = input("No creo que esté bien su respuesta, escríbala de nuevo: ")
    
    num_anios = int(num_anios)
    
    
    for i in range(0, num_anios):
        formula_capital(amount, interest)
    
    
    
    
    
    
if __name__ == "__main__":
    main()