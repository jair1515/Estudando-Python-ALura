# Cria um dicionário com chave x e valor x**2 para x de 1 a 5
numeros_quadrados = {x: x**2 for x in range(1, 6)}

# range(1, 6) → gera os números de 1 até 5 (6 não é incluído)
# x**2 → calcula o quadrado de x
# Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(numeros_quadrados)

## range(início, fim, passo) → função que gera uma sequência de números
# Exemplos:
# list(range(1, 6))      → [1, 2, 3, 4, 5]
# list(range(0, 10, 2))  → [0, 2, 4, 6, 8]
# list(range(5, 0, -1))  → [5, 4, 3, 2, 1]