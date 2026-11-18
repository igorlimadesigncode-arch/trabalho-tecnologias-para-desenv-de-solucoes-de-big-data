`markdown
# Trabalho Prático: Limpeza de Dados com Pandas

Disciplina **DGT2823 - Tecnologias para desenvolvimento de soluções de big data**.

Este projeto realiza a limpeza de um conjunto de dados de atividades físicas em Python com a biblioteca **Pandas**, deixando-o apto para tarefas de mineração e análise de dados.

## Conjunto de dados

O arquivo `dados.csv` possui 32 registros e 6 colunas, separadas por `;`:

| Coluna | Descrição |
|---|---|
| ID | Identificador do registro |
| Duration | Duração da atividade (minutos) |
| Date | Data da atividade |
| Pulse | Pulsação média |
| Maxpulse | Pulsação máxima |
| Calories | Calorias gastas |

O arquivo contém inconsistências propositais: valores nulos em `Calories` (linhas 18 e 28) e em `Date` (linha 22), e uma data em formato diferente (`20201226`, linha 26).

## Estrutura do repositório

- `dados.csv`: conjunto de dados original.
- `microatividade1.py`: Microatividades 1 a 5 (leitura do CSV, subconjunto, `max_rows` com `to_string()`, `head`/`tail` e `info()`).
- `trabalho_pratico.py`: script do Trabalho Prático (limpeza dos dados).

## Como executar

1. Instale o Python 3.13 e o Pandas:
bash py -3.13 -m pip install pandas


2. Execute o script na pasta do projeto:
bash py -3.13 .\trabalho_pratico.py

## Etapas de tratamento

1. Leitura do CSV com `sep=";"`, `engine="python"` e `encoding="utf-8"`.
2. Verificação da importação com `info()`, `head()` e `tail()`.
3. Criação de uma cópia do conjunto original (`df_limpo`).
4. Substituição dos nulos de `Calories` por `0`.
5. Substituição dos nulos de `Date` por `1900/01/01`.
6. Remoção das aspas simples das datas, que o CSV traz como texto.
7. Primeira tentativa de `to_datetime`, que gera erro de formato.
8. Substituição de `1900/01/01` por `NaN` e nova tentativa de conversão.
9. Conversão específica do valor `20201226` com `replace` e `to_datetime`.
10. Conversão final de toda a coluna `Date` para `datetime`.
11. Remoção do registro com `Date` nulo (índice 22) com `dropna`.

## Resultado

- O conjunto passa de **32 para 31 registros**.
- `Date` fica no tipo `datetime64`.
- `Calories` fica sem valores nulos (as linhas 18 e 28 recebem `0.0`).
- O registro de índice 22 é removido; os demais mantêm o índice original.

## Observação sobre as versões

Nesta versão do Pandas (3.x), o primeiro `to_datetime` já falha no valor `20201226`, e não em `1900/01/01`, como descrito no roteiro. O tratamento seguinte (substituir por `NaN` e converter o valor especial) segue o enunciado normalmente. Além disso, a coluna de texto aparece como `str` no `info()`, e não como `object`.

## Ambiente

- Python 3.13
- Pandas 3.1.1
- VS Code e Windows

## Autor

Igor Lima