grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 5
grafo["inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["c"] = 4
grafo["a"]["d"] = 2
grafo["b"] = {}
grafo["b"]["a"] = 8
grafo["b"]["d"] = 7
grafo["c"] = {}
grafo["c"]["d"] = 6
grafo["c"]["fim"] = 3
grafo["d"] = {}
grafo["d"]["fim"] = 1
grafo["fim"] = {}

custos = {}
infinito = float("inf")

custos["a"] = 5
custos["b"] = 2
custos["c"] = infinito
custos["d"] = infinito
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["c"] = "a"
pais["d"] = None
pais["fim"] = None

processados = []
print(custos)
print(grafo)

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo=custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo=custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    print(f"Nó mais baixo :{nodo}")
    custo = custos[nodo]
    print(f"custo:{custo}")
    vizinhos = grafo[nodo]
    print(f"vizinhos: {vizinhos}")
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            print(f"novo_custo: {novo_custo}")
            pais[n] = nodo
            print(f"pais: {nodo}")
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)    