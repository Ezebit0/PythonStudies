# Exemplo
def Saudacao(nome):
    print(f"Olá, boa tarde {nome}!")

print("\n Chamando a função saudação:")
Saudacao("Alice")
Saudacao("Bob")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado")
numero = int(input("Digite o numero para ficar ao quadrado:"))
resultado_quadrado = quadrado(numero)
print("O resultado da função quadrado:", resultado_quadrado)

# Função com multiplos parametros
def soma(numero1, numero2):
    return numero1 + numero2
numero1 = int(input("Primeiro numero:",))
numero2 = int(input("Segundo numero:",))
resultado = soma(numero1, numero2)

print("O resultado da soma é: ", resultado)