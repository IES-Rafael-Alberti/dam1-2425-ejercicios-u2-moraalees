def algoritmo(arr):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento de burbuja.
    
    Este método recorre repetidamente la lista, comparando elementos adyacentes y
    cambiándolos de posición si están en el orden incorrecto. Este proceso se repite 
    hasta que la lista esté ordenada.

    Parameters:
    arr (list): Lista de números a ordenar.

    Returns:
    list: La lista ordenada en orden ascendente.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    """
    Función principal que ejecuta el programa de ordenamiento de una lista.
    
    Define una lista de números, la ordena utilizando el algoritmo de burbuja y
    muestra el resultado en la consola.
    """
    a = [8, 3, 1, 19, 14]
    sorted_a = algoritmo(a)
    
    print(f"Lista ordenada: {sorted_a}")
    
    
if __name__ == "__main__":
    main()