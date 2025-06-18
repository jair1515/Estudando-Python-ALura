import string
from collections import Counter

# Frase de exemplo
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."

# Converte tudo para minúsculas e remove pontuação
frase_limpa = frase.lower().translate(str.maketrans("", "", string.punctuation))

# Separa as palavras
palavras = frase_limpa.split()

# Conta a frequência de cada palavra
contagem_palavras = Counter(palavras)

# Exibe o resultado de forma legível
for palavra, contagem in contagem_palavras.items():
    print(f"{palavra}: {contagem}")
