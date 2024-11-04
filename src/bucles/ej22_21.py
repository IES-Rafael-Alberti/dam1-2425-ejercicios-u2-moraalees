def pedir_montos():
    total = 0
    
    while True:
        montos = float(input("Vaya ingresando sus montos de la compra (Si desea parar escriba 0): "))

        if montos < 0:
            print("No puede ingresar valores negativos...")
        
        if montos == 0:
            break
        
        if montos != 0:
            total += montos
    
    
    if total >= 1000:
        total2 = total - total/10
        print(f"Su venta total ha alcanzado los $1000 ({total}), por tanto se le aplica un 10% de descuento: ${total2}")
    else:
        print(f"Su total de ventas es de ${total}")
    
    

def main():
    pedir_montos()
    
    
    
if __name__ == "__main__":
    main()