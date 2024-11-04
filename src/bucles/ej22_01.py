def repetir_palabra(palabra: str):
    for i in range(0, 10):
        print(palabra)


def main():
    palabra = input("Escriba lo primero que se le venga a la mente: ")
    
    repetir_palabra(palabra)
        
    
if __name__ == "__main__":
    main()