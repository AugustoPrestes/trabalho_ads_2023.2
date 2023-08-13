"""
Extração de dados da WEB
Autor: Augusto Prestes da Silva
Data: 13/06/2023
"""
# Importes
import pandas as pd
import basedosdados as bd

# Extraindo os dados do site base dos dados
df = bd.read_table(dataset_id='br_tse_eleicoes',
                   table_id='receitas_candidato',
                   billing_project_id='eleicoes-380622',
                   limit=100000)

# Transformando os dados
tabela_receitas = pd.DataFrame(df)

# Salvando a tabela como arquivo .csv
tabela_receitas.to_csv('receita.csv', header=True, index=True)

