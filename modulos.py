print("Exemplo de importação de um módulo padrão:")
from math import sqrt

Digite_numero = int(input("Digite o numero:"))
raiz_quadrada = sqrt(Digite_numero)
print(f"A raiz quadrada de {Digite_numero} é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um modulo personalizado")
from Meu_modulo import saudacao, dobro

nome = str(input("Qual é o seu nome?"))
mensagem = saudacao(nome)
print(mensagem)
numero = int(input("Digite o numero para dobrar:"))
resultado_dobro = dobro(numero)
print(f"O dobro de {numero} é {resultado_dobro}")