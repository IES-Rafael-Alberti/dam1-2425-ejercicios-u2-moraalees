def comprobar_renta(renta: float) -> bool:
    if renta < 0:
        return False
    
    return True



def tipo_impositivo(renta: float):
    if renta < 10000:
        print(f"Tu tipo impositivo es del 5%, ya que tu renta anual es de {renta}€.")
        
    elif 10000 <= renta < 20000:
        print(f"Tu ripo impositivo es del 15%, ya que tu renta anual es de {renta}€.")
        
    elif 20000 <= renta < 35000:
        print(f"Tu ripo impositivo es del 20%, ya que tu renta anual es de {renta}€.")
        
    elif 35000 <= renta < 60000:
        print(f"Tu ripo impositivo es del 30%, ya que tu renta anual es de {renta}€.")
        
    elif renta >= 60000:
        print(f"Tu ripo impositivo es del 45%, ya que tu renta anual es de {renta}€.")
    
    

def main():
    renta = float(input("Introduzca su renta anual: "))
    
    while not comprobar_renta(renta):
        renta = float(input("No puedes tener renta negativa. Introduzca su renta anual de verdad: "))
    
    tipo_impositivo(renta)
    
if __name__ == "__main__":
    main()