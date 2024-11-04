def algoritmo(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    a = [8, 3, 1, 19, 14]
    sorted_a = algoritmo(a)
    
    print(f"Lista ordenada: {sorted_a}")
    
    
    
if __name__ == "__main__":
    main()
