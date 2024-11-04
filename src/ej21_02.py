def intro_contraseña(contrasena: str):
    password = "contrasena"
    if password == contrasena.lower():
        return True
    else:
        return False


def main():
    contrasena = input("Escriba la contrasena: ")
    if intro_contraseña(contrasena) == True:
        print("Increible que hayas acertado la contrasena! (Era muy rebuscada eeeh).")
        
    elif intro_contraseña(contrasena) == False:
        print("Que va, esa no es la contrasena...")
    
if __name__ == "__main__":
    main()