import os

def borrar_programa():
    os.system("cls")


def pedir_numero() -> int:
    n = int(input("Introduzca el número: "))
    
    try:
        if n < 0:
            raise ValueError("El número no puede ser menor que 0.")
        elif n > 20:
            raise ValueError("El número no puede ser mayor que 20.")

    except ValueError as e:
        if n is None:
            print("***ERROR*** - Ese dato es inválido.")
        else:
            print(f"***ERROR*** inesperado, {e}")
                    
    return n


def crear_piramide(n):
    for i in range(n, -1, -1):
        print(f"{i} => {n}")
        

def main():
    borrar_programa()
    n = pedir_numero()
    serie = ""
    for i in range(n, -1, -1):
        serie += f"{i} => "
        total = 0
        for j in range(0, i + 1, 1):
            serie += f"{j} + "
            total += j
            
        serie = serie[:-2] + f"= {total}\n"
    
    print(serie)
    
if __name__ == "__main__":
    main()