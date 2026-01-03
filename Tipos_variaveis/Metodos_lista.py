# METODOS DE LISTA
minha_lista = [1, 2, 3, 4, 5, "Eduardo", True, False]
minha_lista_numerica = [3, 1, 2, 4, 10, 6, 18, 20]

# METODO #1 append():   Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# METODO #2 index:      Retorna o indice do primeiro elemento igual o valor especificado
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# METODO #3 insert:     Insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print("Após o insert(2,10):", minha_lista)

# METODO #4 pop:        Remove e retorna o elemento de um indice especifico
elemento_devido = minha_lista.pop(3)
print("Elemento removido:", elemento_devido)
print("Após pop(3):", minha_lista)

# METODO #5 remove:     Remove o primeiro elemento com o valor especificado
minha_lista.remove(False)
print("Após remove(False):", minha_lista)

# METODO #6 sort:       Organizar a lista em ordem crescente
minha_lista_numerica.sort()
print("Após sort():", minha_lista_numerica)
