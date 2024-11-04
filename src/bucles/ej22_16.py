def main():
    numero_mayor = None

    while True:
        numero = int(input("Ingresa un número entero positivo (0 para finalizar): "))

        if numero == 0:
            break

        elif numero > 0:
            if numero_mayor is None or numero > numero_mayor:
                numero_mayor = numero

        else:
            break

    if numero == 0:
        print(f"El mayor número ingresado fue: {numero_mayor}")
    else:
        print("Ingresaste un número inválido (negativo).")


if __name__ == '__main__':
    main()