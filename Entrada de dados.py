idade = int(input("Quantos anos você tem?"))
print("Exemplo de comando if")
if idade >= 18: # Maior ou igual
    print("Voce é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else: # Exemplo de "else"
    print("Voce é menor de idade.")

# Exemplão
mensagem = "Você pode tirar a CNH." if idade >= 18 else "Voce não pode tirar a CNH."
print(mensagem)