import pandas as pd
from pathlib import Path

# Leitura dos dados
data_path = Path('dataset/clientes.csv')
df = pd.read_csv(data_path)

# Verificar os primeiros registros
# Como está vazio, mostra os 5 primeiros
print(df.head().to_string())

# Últimos registros
# Como está vazio, mostra os 5 últimos
print(df.tail().to_string())

# Verificar a quantidade de linhas e colunas
print('Qtd: ', df.shape)

# Verificar tipos de dados
# Identifica se cada coluna contém int, float, object (texto), datetime, etc.
print('Tipagem: \n', df.dtypes)

# Verifica e conta quantos valores nulos
print('Valores nulos: \n', df.isnull().sum())