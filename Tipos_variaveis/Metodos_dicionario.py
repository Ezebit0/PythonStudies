pessoa = {"nome": "Eduardo", "idade": "18", "cidade": "Osasco"}
# Exibindo o dicionario completo            
print("Meu dicionario de exemplo:", pessoa)
# Acessando valores por chaves
print("Nome:", pessoa ["nome"])
print("Idade:", pessoa ["idade"])
print("Cidade:", pessoa ["cidade"])

pessoa["sobrenome"] = "Mendes"
print("Sobrenome:", pessoa ["sobrenome"])

pessoa["idade2"] = "15"
print("Idade atualizada:", pessoa["idade2"])

# Removendo um par chave-valor
del pessoa ["sobrenome"]
print("Meu dicionario de exemplo depois de ter removido:", pessoa)

# Metodo: key()
chaves = list(pessoa.keys())
print("Chaves do dicionario:", chaves)
print("Primeira chave:", chaves[0])
print("Segunda chave:", chaves[1])
print("Terceira chave:", chaves[2])
print("Quarta chave:", chaves[3])

# Metodo: values()
valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor:", valores[0])

# Metodo: items()
itens = list(pessoa.items())
print("Pares chaves-valor do dicionario:", itens)
print("Primeiro chave-valor: %s = %s" % (itens[0][0], itens [0][1]))
