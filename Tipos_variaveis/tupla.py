# Uma coleção ordenada e imutavel de elementos

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 3, 4, 4, 5)

print("Minha tupla:", minha_tupla)
print("Minha tupla[0]:", minha_tupla[0]) # elemento 0
print("Minha tupla[0]:", minha_tupla[5]) # elemento 5
print("Minha tupla[1:7]:", minha_tupla[1:7]) # elemento de 1 a 6 (7)
print("Minha tupla[:6]:", minha_tupla[:6]) # todos elementos antes de 6
print("Minha tupla[3:]:", minha_tupla[3:]) # todos elementos após o 3
print("Minha_tupla[-1]:", minha_tupla[-1]) # ultimo elemento

# Metodos
# count
contagem = minha_tupla.count(4)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

# index
indice = minha_tupla.index(3)
print("Indice da primeira ocorrência do elemento 3:", indice)