def binary_search(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo+alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio  
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1                    
        
    
test = [1,3,4,2,7,9,12]
print(binary_search(test,12))