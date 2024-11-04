def pedir_numero():
    try:
        numero = int(input("Introduzca un número entero positivo: "))
            
    except ValueError as e:
        print(f"La entrada no es correcta: {e}")
            
    except Exception as e:
        print(f"La entrada no es correcta: {e}")


def main():
    entrada = pedir_numero()
    
    
if __name__ == "__main__":
    main()