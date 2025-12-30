## METODOS
nome = "Eduardo"
sobrenome = "Mendes"
nome_completo = "Eduardo Mendes"

# Retorna a string em letra maiuscula
nome.upper()
# Retorna a string em letra minuscula
nome.lower()

nome.encode()
nome.encode().decode 

# Substitui letra
nome_completo.replace("E", "A")

# A cada caractere tem um traço ou qualquer coisa
"-".join("Eduardo")
# metodo de separação
nome_completo.split(" ")

# Tratamento de variavel, quando quer tratar texto quando tem ruidos na partes mais adjacentes
nome1 = "xEduardo Mendesx"
# Remove o alvo (x)
nome.strip("x")

# Esquerda e Direita
nome.rstrip("x")
nome.lstrip("x")

# Comparadores muito utilizaveis

# Verifica se começa com (alvo)
# Entrega true or false
nome_completo.startswith("Ed")
# Verifica se termina com (alvo)
nome_completo.endswith("es")

# se alvo existi  na variavel entrega true or false
"es" in nome_completo

# se alvo não existi  na variavel entrega true or false
"es" not in nome_completo



