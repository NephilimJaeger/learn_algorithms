votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print(f"{nome} não pode mais votar!")
    else:
        votaram[nome] = True
        print(f"{nome} pode votar!")
        
verifica_eleitor("Nila")
verifica_eleitor("Jimmy")
verifica_eleitor("Nila")
verifica_eleitor("Jimmy")