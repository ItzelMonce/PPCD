from random import sample

lista = list(range(100))  # tamaño de la lista
arreglomerge = sample(lista, 8)

def MergeSort(arreglo):
    print("El arreglo a ordenar con merge es:", arreglo)

    def merge(arreglo):
        
        def largo(arr):
            largoarr = 0  # Establecemos un contador del largo del arreglo
            for _ in arr:
                largoarr += 1  # Obtenemos el largo del arreglo
            return largoarr

        
        if len(arreglo) > 1:
            medio = len(arreglo) // 2
            izq = arreglo[:medio]
            der = arreglo[medio:]

            # Llamar recursivamente a "merge" para los subarreglos izquierdo y derecho
            print(izq)
            print(der)
            merge(izq)
            merge(der)

            i = j = k = 0

            # Mezclar los subarreglos izquierdo y derecho en el arreglo original
            while i < len(izq) and j < len(der):
                if izq[i] < der[j]:
                    arreglo[k] = izq[i]
                    i += 1
                else:
                    arreglo[k] = der[j]
                    j += 1
                k += 1

            while i < len(izq):
                arreglo[k] = izq[i]
                i += 1
                k += 1

            while j < len(der):
                arreglo[k] = der[j]
                j += 1
                k += 1

    
    merge(arreglo)

    print("El arreglo ordenado con merge es:", arreglo)
MergeSort(arreglomerge)
