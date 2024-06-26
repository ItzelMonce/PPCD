def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
 
# Example usage
#arr = [1, 7, 4, 1, 10, 9, -2]
arr = [i for i in range(100,0,-1)]
sorted_arr = quicksort(arr)
print("Arreglo desordenado: ", arr)
print("Arreglo ordenado de forma: ", sorted_arr)




