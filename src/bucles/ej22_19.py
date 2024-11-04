def mostrar_menu():
    print("\nMenú del programa:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")


def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Programa comenzado.")
        
    elif opcion == 2:
        print("Listado:")
        
    elif opcion == 3:
        print("Bye, bye.")
        
    else:
        print("Opción incorrecta. Por favor, elija una opción válida.")



def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1, 2 o 3): "))
            
            if opcion == 3:
                ejecutar_opcion(opcion)
                break
            ejecutar_opcion(opcion)
            
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")



if __name__ == "__main__":
    main()
