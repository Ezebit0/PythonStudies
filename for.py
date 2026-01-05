print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

print("For utilizando dicionario - chaves")
pessoa = {"Nome": "Eduardo", "Sobrenome": "Mendes", "idade": 18, "cidade": "São Paulo"}
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo numérico
# [0,1,2,3,4,5,6,7,8,9]
print("\nFor utilizando a função range()")
for numero in range (5):
    print("Numero:", numero )

print("\nFor utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice])
'''
    if indice == 3:
        lista[indice] = 5
''' 

# Enumerate 
lista_enumerate = ["a", "b", "c", "d"]
for indice, valor in enumerate():
    print(f"{indice}, {valor}")
'''
    if indice == 1:
        print("Indice 1")
''' 
