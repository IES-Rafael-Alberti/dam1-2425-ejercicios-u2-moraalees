def intro_contraseña(password: str, contraseña: str):
    if password == contraseña.lower():
        return print("¡Increíble que hayas acertado la contraseña! (Era muy rebuscada eeeh)")
    else:
        return print("Qué va, esa no es la contraseña...")


def main():
    password = "contraseña"
    contraseña = input("Escriba la contraseña: ")
    intro_contraseña(password, contraseña)
    
    
if __name__ == "__main__":
    main()