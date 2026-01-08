def Adicionar_contato(contato, nome_contato):
    contato = {"contato": nome_contato, "favorito": False}
    contatos.append(contato)
    print(f"O {nome_contato} foi adicionado a lista de contatos")
    return

def Ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate (contatos, start=1):
        status = "★" if contato["favorito"] else ""
        nome_contato = contato["contato"]
        print (f"{indice}. [{status}] {nome_contato}") 
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato = int(indice_contato) - 1
    contatos[indice_contato]["favorito"] = True
    print(f"Contato {indice_contato} favoritado com sucesso!")
    return

def desfavoritar_contato(contatos, indice_contato):
    indice_contato = int(indice_contato) - 1
    contatos[indice_contato]["favorito"] = False
    print(f"contato {indice_contato} desfavoritado com sucesso!")
    return

def Ver_favoritos(contatos):
    encontrou_favorito = True
    print("\nLista de contatos favoritados:")
    for indice, contato in enumerate (contatos, start=1):
        if contato["favorito"]:
            nome_contato = contato["contato"]
            print(f"{indice}. [★]  {nome_contato}")
    if not encontrou_favorito:
        print("Nenhum contato favorito foi encontrado")
    return

def Deletar_contatos_nao_favoritos(contatos):
    for contato in contatos:
        if contato["favorito"] == False:
            contatos.remove(contato)
        print("Contato(s) não favoritados removido(s)")
    return

contatos = []
while True:
    
    print("\nAgenda de contatos") 
    print("1. Adicionar contato")    # Adicionar contato
    print("2. Ver contatos")    # Visualizar contatos
    print("3. Favoritar contato")    # Favoritar contato
    print("4. Desfavoritar contato")    # Desfavoritar contato
    print("5. Visualizar favoritos")    # Visualizar contatos favoritos
    print("6. Deletar contatos não favoritados")    # Deletar contatos nao favoritados
    print("7. sair")    # Sair

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do seu contato: ")
        Adicionar_contato(contatos, nome_contato)

    elif escolha == "2":
        Ver_contatos(contatos)

    elif escolha == "3":
        Ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "4":
        Ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja desfavoritar: ")
        desfavoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        Ver_favoritos(contatos)

    elif escolha == "6":
        Deletar_contatos_nao_favoritos(contatos)
        Ver_favoritos(contatos)

    elif escolha == "7":
        break

print("Agenda finalizado")