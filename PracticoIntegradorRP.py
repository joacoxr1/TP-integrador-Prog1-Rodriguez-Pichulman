# Importar modulo random para generar numeros aleatorios y time para medir el tiempo de la ejecucion
import random
import time 

#funciones
# Por burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Busqueda lineal
def busqueda_lineal(lista, elemento):
    inicio = time.time()  # Iniciar medicion del tiempo
    for i in range(len(lista)):
        if lista[i] == elemento:
            fin_tiempo = time.time()
            tiempo = (fin_tiempo - inicio) * 1000  # Tiempo en milisegundos
            return i, tiempo
    fin_tiempo = time.time()
    tiempo = (fin_tiempo - inicio) * 1000  
    return -1, tiempo

# Busqueda binaria
def busqueda_binaria(lista, elemento):
    inicio = time.time()  # Iniciar medicion del tiempo
    indice = 0
    fin = len(lista) - 1

    while indice <= fin:
        medio = (indice + fin) // 2
        if lista[medio] == elemento:
            fin_tiempo = time.time()
            tiempo = (fin_tiempo - inicio) * 1000  # Tiempo en milisegundos
            return medio, tiempo
        elif lista[medio] < elemento:
            indice = medio + 1
        else:
            fin = medio - 1
    fin_tiempo = time.time()
    tiempo = (fin_tiempo - inicio) * 1000  
    return -1, tiempo

#PROGRAMA PRINCIPAL
# Lista de productos (codigos numericos generados aleatoriamente por random)
inventario = [random.randint(100, 999) for i in range(500)]

print("Inventario antes de ordenar:", inventario)
burbuja(inventario) #llama a la funcion burbuja para ordenar el inventario
print("Inventario ordenado:", inventario)

# Menu
while True:
    print("\n=== Busqueda de Productos ===")
    producto_a_buscar = int(input("Ingrese el codigo del producto a buscar (0 para salir): "))
    
    if producto_a_buscar == 0:
        print("Saliendo del programa...")
        break
    
    # Ejecutar busqueda binaria
    indice_binaria, tiempo_binaria = busqueda_binaria(inventario, producto_a_buscar)
    if indice_binaria != -1:
        print(f"El producto con codigo {producto_a_buscar} esta en la posicion {indice_binaria} y se demoro {tiempo_binaria:.5f} ms usando busqueda binaria.")
    else:
        print(f"El producto con codigo {producto_a_buscar} no fue encontrado y se demoro {tiempo_binaria:.5f} ms usando busqueda binaria.")
    
    # Ejecutar busqueda lineal
    indice_lineal, tiempo_lineal = busqueda_lineal(inventario, producto_a_buscar)
    if indice_lineal != -1:
        print(f"El producto con codigo {producto_a_buscar} esta en la posicion {indice_lineal} y se demoro {tiempo_lineal:.5f} ms usando busqueda lineal.")
    else:
        print(f"El producto con codigo {producto_a_buscar} no fue encontrado y se demoro {tiempo_lineal:.5f} ms usando busqueda lineal.")