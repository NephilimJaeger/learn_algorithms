def sauda(nome):
    print(f"Olá {nome}!")
    sauda2(nome)
    print("preparando para dizer tchau")
    tchau()
    
def sauda2(nome):
    print(f"Como vai {nome}?")
    
def tchau():
    print("ok, tchau!")
    
sauda("Maggie")