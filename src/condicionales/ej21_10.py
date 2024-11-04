def comprobar_pizza(pizza: str) -> bool:
    if pizza == "vegetariana" or pizza == "no":
        return True
    
    return False


def pizza_vegetariana(pizza: str):
    if pizza == "vegetariana":
        print("Perfecto. Sus ingredientes para añadir a la pizza son Pimiento o Tofu, sólo uno. El tomate y queso ya están incluidos.")
        
        
def ingrediente_vegetariana(ingredientes: str) -> bool:
    if ingredientes == "pimiento" or ingredientes == "tofu":
        return True
    
    return False

def final_vegetariana(pizza: str, ingredientes: str):
    print(f"Perfecto, entonces su pizza es {pizza} y el ingrediente que lleva es {ingredientes}, tomate y queso. ¡Gracias!")
    
    
def pizza_no_vegetariana(pizza: str):
    if pizza == "no":
        print("Perfecto. Sus ingredientes para añadir a la pizza son Peperoni, Jamón o Salmón, sólo uno. El tomate y queso ya están incluidos.")


def ingredientes_no_vegetariana(ingredientes: str) -> bool:
    if ingredientes == "jamón" or ingredientes == "salmón" or ingredientes == "peperoni":
        return True
    
    return False


def final_no_vegetariana(pizza: str, ingredientes: str):
    print(f"Perfecto, entonces su pizza no es vegetariana y el ingrediente que lleva es {ingredientes}, tomate y queso. ¡Gracias!")
    

def main():
    pizza = input("Bienvenido a Bella Napoli. Para empezar me gustaría preguntarle como quiere la pizza. ¿Vegetariana o no?: ").lower()
    
    while not comprobar_pizza(pizza):
        pizza = input("Por favor conteste con la palabra vegetariana o escriba no si es que no la quiere vegetariana: ").lower()
      
    if pizza == "vegetariana":
        pizza_vegetariana(pizza)
        ingredientes = input("Escriba qué ingrediente quiere: ").lower()
        ingredientes = ingredientes.strip()
        
        while not ingrediente_vegetariana(ingredientes):
            ingredientes = input("Los ingredientes solo son pimiento o tofu, no los dos: ").lower()
            ingredientes = ingredientes.strip()
            
        final_vegetariana(pizza, ingredientes)
    
    elif pizza == "no":
        pizza_no_vegetariana(pizza)
        ingredientes = input("Escriba qué ingredientes quiere: ").lower()
        ingredientes = ingredientes.strip()
        
        while not ingredientes_no_vegetariana(ingredientes):
            ingredientes = input("Los ingredientes solo son jamón o peperoni o salmón, no más de uno (Las tildes importan): ").lower()
            ingredientes = ingredientes.strip()
            
        final_no_vegetariana(pizza, ingredientes)
        
    
if __name__ == "__main__":
    main()