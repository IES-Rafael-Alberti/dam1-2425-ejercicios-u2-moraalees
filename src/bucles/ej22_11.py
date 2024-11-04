def ensenar_letras(palabra: str):
    for i in palabra:
        print(i)
    
    return palabra


def main():
    palabra = input("Escriba una palabra: ")
    palabra = palabra[::-1]
    
    ensenar_letras(palabra)
    
    
if __name__ == "__main__":
    main()