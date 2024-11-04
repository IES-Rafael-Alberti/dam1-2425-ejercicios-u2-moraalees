def comprobar_cero(divisor: float) -> bool:
    if divisor == 0:
        return False
    else:
        return True
    

def dividir_numeros(dividendo: float, divisor: float) -> float:
    return dividendo / divisor
    
    
def main():
    dividendo = float(input("Escriba un número como dividendo: "))
    divisor = float(input("Ahora escriba un número como divisor: "))
    
    while comprobar_cero(divisor) == False:
        print("*ERROR* - El divisor no puede ser 0...")
        divisor = float(input("Escriba un nuevo número como divisor: "))
        
        
    print(f"La división de {dividendo} entre {divisor} es de {dividir_numeros(dividendo, divisor):.2f}")
    
    
if __name__ == "__main__":
    main()