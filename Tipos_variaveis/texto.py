# Declaração de um tipo texto
nome_completo = "Eduardo Mendes"

nome_completo_aspas = """Eduardo 
Mendes"""

nome_completo_quebra = "Eduardo \
Mendes"

nome = "Eduardo"
sobrenome = "Mendes"

# Formatação

# -----------------------------
# FORMAS DIFERENTES DE USAR O print
# -----------------------------

# 1) Usando vírgula
# O print adiciona automaticamente um espaço entre os valores
print("Nome completo (1a forma):", nome_completo)

# 2) Usando o sinal de +
# O + apenas junta os textos, NÃO adiciona espaço
print("Nome completo (2a forma):" + nome_completo)

# 3) Concatenando várias strings sem espaço
# Como não existe espaço em nenhuma string, tudo fica grudado
print("Nome completo (3a forma):" + "Eduardo" + "Mendes")

# 4) Misturando + com vírgula
# O + junta strings
# A vírgula faz o print adicionar um espaço automático
print("Nome completo (4a forma):" + "Eduardo", "Mendes")

# 5) Usando variável com vírgula
# Novamente, a vírgula garante o espaço automático
print("Nome completo (5a forma):", nome_completo_aspas)

# 6) String com quebra de linha
# O \n faz o texto ser exibido em duas linhas
print("Nome completo (6a forma):", nome_completo_quebra)

# 7) Usando %s (formatação antiga)
# %s é um "lugar reservado" que será substituído pela variável
print("Nome completo (7a forma): %s" % nome_completo)

# 8) Vários %s
# Cada %s recebe um valor, na ordem em que aparecem
# O Python converte tudo para string automaticamente
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))

# 9) f-string (forma moderna e recomendada)
# As variáveis ficam visíveis dentro do texto, facilitando a leitura
print(f"Nome completo (9a forma): {nome} {sobrenome}")

# 10) Usando .format()
# Os {} são preenchidos pelos valores passados no format()
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))

# Retorna a string em letra maiuscula
nome.upper()
# Retorna a string em letra minuscula
nome.lower()

nome.encode()
nome.encode().decode 

# Substitui letra
nome_completo.replace("E", "A")