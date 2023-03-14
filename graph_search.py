from collections import deque

grafo = {}
grafo["voce"] = ["alice","bob","claire"]
grafo["bob"] = ["anuj","peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom","jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def pessoa_e_vendedor(pessoa):
    return pessoa[-1] == 'm' 

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    print(fila_de_pesquisa)
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

print(pesquisa("voce"))