def buscaMenor(arr):
    menor = arr[0]
    menor_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_idx = i
    return menor_idx

def ordPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordPorSelecao([3,1,4,9,2,8]))