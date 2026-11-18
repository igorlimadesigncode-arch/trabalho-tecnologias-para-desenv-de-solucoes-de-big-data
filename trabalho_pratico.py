# Trabalho Prático - Limpeza de dados com Pandas
import pandas as pd

# 1. Leitura do CSV (separador ';', engine python e encoding utf-8)
df = pd.read_csv("dados.csv", sep=";", engine="python", encoding="utf-8")

# 2. Verificação da importação
print("Informações gerais:")
df.info()

print("\nPrimeiras 5 linhas:")
print(df.head())

print("\nÚltimas 5 linhas:")
print(df.tail())

# 3. Cópia do conjunto original
df_limpo = df.copy()

# 4. Calories: nulos -> 0
df_limpo["Calories"] = df_limpo["Calories"].fillna(0)
print("\nApós substituir nulos de Calories por 0:")
print(df_limpo.to_string())

# 5. Date: nulos -> '1900/01/01'
df_limpo["Date"] = df_limpo["Date"].fillna("1900/01/01")
print("\nApós substituir nulos de Date por '1900/01/01':")
print(df_limpo.to_string())

# 6. Remover as aspas simples das datas (o CSV as traz como texto)
df_limpo["Date"] = df_limpo["Date"].astype(str).str.replace("'", "", regex=False)

# 7. Primeira tentativa de to_datetime (gera erro, conforme o enunciado)
# Observação: nesta versão do Pandas, o primeiro to_datetime já falha no valor
# '20201226' (e não em '1900/01/01', como descrito no roteiro). O tratamento
# seguinte (substituir por NaN e converter o valor especial) segue o enunciado.
try:
    df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
except ValueError as erro:
    print("\nPrimeiro erro de conversão:", erro)

# 8. Substituir '1900/01/01' por NaN e repetir a transformação
df_limpo["Date"] = df_limpo["Date"].replace("1900/01/01", float("nan"))
try:
    df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
except ValueError as erro:
    print("\nSegundo erro de conversão (20201226):", erro)

# 9. Converter especificamente o valor '20201226'
df_limpo["Date"] = df_limpo["Date"].replace(
    "20201226", pd.to_datetime("20201226", format="%Y%m%d").strftime("%Y/%m/%d")
)

# 10. Transformação final de toda a coluna Date
df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
print("\nApós converter Date para datetime:")
print(df_limpo.to_string())
df_limpo.info()

# 11. Remover registros com valores nulos (linha 22)
df_limpo = df_limpo.dropna(subset=["Date"])
print("\nConjunto de dados final (sem nulos):")
print(df_limpo.to_string())
df_limpo.info()