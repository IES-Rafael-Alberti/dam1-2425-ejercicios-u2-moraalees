def comprobar_contraseña(contrasena: str, contrasena2):
    while contrasena != contrasena2:
        contrasena = input("Vaya, no has escrito bien la contraseña... Inténtalo otra vez: ")
        
    return print("OLEEE. La has adivinado, siéntete un genio.")


def main():
    contrasena_prede = "contraseña"
    contrasena = input("Escriba la CONTRASEÑA, <-- EJEM: ")
    
    comprobar_contraseña(contrasena, contrasena_prede)
    
    
    
    
if __name__ == "__main__":
    main()