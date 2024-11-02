def dividir_sumar_numero_par():
    contador_pares = 0

    while True:
        numero = input("Escriba un número entero positivo (Si desea salir del programa escriba -1): ")

        if numero == "-1":
            break


        if not numero.isdigit():
            print("Te dije que solo se podían escribir números enteros positivos...")
            continue

        sumatorio = sum(int(digito) for digito in numero)
        print(f"La suma de todos los números en {numero} es {sumatorio}.")


        if int(numero) % 2 == 0:
            contador_pares += 1


    print(f"Escribiste {contador_pares} número/s par/es.")



def main():
    dividir_sumar_numero_par()


if __name__ == "__main__":
    main()
