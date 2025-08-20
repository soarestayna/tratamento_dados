import pandas as pd


# Função para calcular o cubo de um número
# Essa função recebe um número x e retorna x³ (x elevado à terceira potência).
def eleva_cubo(x):
    return x ** 3

# Esse comando cria uma tabela com uma coluna, a variável df é onde guardamos uma estrutura.
df = pd.DataFrame({'numeros':[1,2,3,4,5,10]})

# Aqui está dizendo "para cada valor na coluna numeros, aplique a função eleva_cubo”.
# Isso gera uma nova coluna chamada cubo_funcao
df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)

# Aqui usamos uma função inline chamada lambda — ela faz o mesmo que eleva_cubo, mas sem ter que definir a função antes.
# Criamos outra coluna chamada cubo_lambda com os cubos
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)
print(df)


