# esto es un comentario del profe
def bsort(arreglo): 
    n=len(arreglo)

#print(f'Tamaño de la lista: {n}')
    for i in range(0,n-1):
        for j in range(0, n-1):
           if  arreglo[j] > arreglo[j+1]:
            temp = arreglo[j]
            arreglo[j]= arreglo[j+1]
            arreglo[j+1]=temp
     
    return arreglo   

listaDesordenada =[8,7,6,5,4,3,2,1]

print(listaDesordenada)

listaOrdenada=bsort(listaDesordenada)

print(listaOrdenada)
