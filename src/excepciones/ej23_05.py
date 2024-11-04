def pedir_contrasena(contrasena_correcta: str):
    while True:
        try:
            contrasena = input("Verifique su contrasena: ")
            
            if contrasena != contrasena_correcta:
                raise NameError("Incorrect Password!!")
                
            break
            
        except NameError as e:
            print(e)
    
    print("Muy bien, se acuerda de su contrasena.")



def main():
    contrasena = "contrasena"
    
    pedir_contrasena(contrasena)
    
    
if __name__ == "__main__":
    main()