def tablas():
    numero = 1
    for i in range(1, 11):
        multiplicacion = f"{numero * 1}, {numero * 2}, {numero * 3}, {numero * 4}, {numero * 5}, {numero * 6}, {numero * 7}, {numero * 8}, {numero * 9}, {numero * 10}."
        print(f"Tabla del {numero}: {multiplicacion}")
        numero += 1

def main():
    tablas()
    
if __name__ == "__main__":
    main()