def adicionar_tarefa(tarefas, nome_tarefa):

    # Tarefa: Nome da tarefa
    # Completada: Indicar se essa tarefa foi completada ou não
    tarefa = {"tarefa:": nome_tarefa, "completada": False}
    tarefas.append(tareaf)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

tarefas = []


while True:
    print("\nMenu do gerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")

    
    print("2. ver tarefa")

    print("3. Atualizar tarefa")

    print("4. Completar tarefa")

    print("5. Deletar tarefas completadas")

    print("6. Sair")
    escolha = input("Digite a sua escolha: ")


    if escolha == "1":
        nome_tarefa = input ("Digite o nome da tarefa que deseja adicionar:")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "6":
        break

print("Programa finalizado")