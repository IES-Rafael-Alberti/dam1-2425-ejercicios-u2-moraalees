def comprobar_puntuacion(puntuacion: float) -> bool:
    if puntuacion == 0.0 or puntuacion == 0.4 or puntuacion >= 0.6:
        return True
    
    return False


def nivel_rendimiento(puntuacion: float):
    if puntuacion == 0.0:
        return print(f"Lamento decirte que tu nivel actual es inaceptable. Por esto mismo su premio será de {puntuacion * 2400} eurazos, intenta esforzarte más.")
    elif puntuacion == 0.4:
        return print(f"Tu nivel es aceptable, aunque podrías conseguir uno mayor todavía. Por ahora, tu premio es de {puntuacion * 2400}€.")
    elif puntuacion >= 0.6:
        return print(f"¡Tu nivel es meritorio, se nota tu esfuerzo! Por esto mismo tu recaudo es de {puntuacion * 2400}€.")
        


def main():
    puntuacion = float(input("Introduzca su puntuación en la empresa (0.0, 0.4 o 0.6-...): "))
    
    while not comprobar_puntuacion(puntuacion):
        print("Eso no puede ser una puntuación campeón/na.")
        puntuacion = float(input("Introduzca su puntuación en la empresa (0.0, 0.4 o 0.6-... ¿Sabes leer?): "))
        
    nivel_rendimiento(puntuacion)
    
    
    
if __name__ == "__main__":
    main()