def grupo_pertenece(nombre: str, sexo: str):
    
    if nombre[0] < "m" and sexo == "mujer":
        return print(f"Como tu nombre empieza por {nombre[0].upper()}, tu grupo correspondiente es el A.")
    
    elif nombre[0] > "n" and sexo == "hombre":
        return print(f"Como tu nombre empieza por {nombre[0].upper()}, tu grupo correspondiente es el A.")
    
    elif nombre[0] >= "m" and sexo == "mujer":
        return print(f"Como tu nombre empieza por {nombre[0].upper()}, tu grupo correspondiente es el B.")
    
    elif nombre[0] <= "n"  and sexo == "hombre":
        return print(f"Como tu nombre empieza por {nombre[0].upper()}, tu grupo correspondiente es el B.")


def comprobar_nombre(nombre: str) -> bool:
    if nombre.isdigit():
        return False
    
    return True


def comprobar_sexo(sexo: str) -> bool:
    if sexo == "hombre" or sexo == "mujer":
        return True
    
    return False


def main():
    nombre = input("Introduzca su nombre para ver a qué grupo perteneces: ")
    nombre = nombre.lower()
    
    while not comprobar_nombre(nombre):
        nombre = input("Escriba el de verdad por favor: ")
        nombre = nombre.lower()
    
    sexo = input("Introduzca su género (Hombre o mujer, no me vengas con tonterías...): ")
    
    sexo = sexo.lower()
    sexo = sexo.strip()
    # El .lower y .strip lo pongo porque el usuario podría introducir su sexo así: muJeR    . Estas dos cosas hacen que eso se transforme en esto: mujer. Entonces el programa si lee que sexo == "mujer".
    
    while not comprobar_sexo(sexo):
        sexo = input("Te he dicho que no digas tonterías. Escriba o mujer u hombre, como prefieras: ")
        sexo = sexo.lower()
        sexo = sexo.strip()
    
    grupo_pertenece(nombre, sexo)
    
    
    
if __name__ == "__main__":
    main()