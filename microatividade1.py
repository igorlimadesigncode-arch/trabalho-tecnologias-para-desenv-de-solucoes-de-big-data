# Microatividade 1 - Ler um arquivo CSV com Pandas
import pandas as pd

df = pd.read_csv("dados.csv", sep=";", engine="python", encoding="utf-8")
print(df)

# Microatividade 2 - Criar um subconjunto de dados
subconjunto = df[["ID", "Duration", "Calories"]]

print("\nSubconjunto de dados (ID, Duration, Calories):")
print(subconjunto)

# Microatividade 3 - Configurar o número máximo de linhas exibidas
pd.set_option("display.max_rows", 9999)

print("\nConjunto de dados original com to_string():")
print(df.to_string())

# Microatividade 4 - Exibir as primeiras e últimas N linhas
print("\nPrimeiras 10 linhas do conjunto de dados original:")
print(df.head(10))

print("\nÚltimas 10 linhas do conjunto de dados original:")
print(df.tail(10))

# Microatividade 5 - Exibir informações gerais do conjunto de dados
print("\nInformações gerais do conjunto de dados original:")
df.info()