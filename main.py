import csv
import pandas as pd

# Comando para ler o arquivo csv
df = pd.read_csv('data-test-analytics_5 (1).csv')
#Comando serve para alocar uma nova coluna no final da sua planilha csv
df.loc[:,'regiao'] = ''
#Criado para facilitar a manipulação de dados listad separando as informações por regiões geograficas
sudeste = ['SP','RJ','BH','ES']
centro_oeste =['DF', 'GO', 'MT', 'MS']
sul =['PR', 'RS' ,'SC']
nordeste =['AL', 'BA', 'CE', 'MA', 'PB', 'PE' ,'PI', 'RN' ,'SE']
norte=['AC', 'AP', 'AM' ,'PA' ,'RO', 'RR', 'TO']

for linha in df.index:
    state = (df['state'][linha])
    if state in sudeste:
        df.loc[linha,'regiao'] = 'Sudeste'
    elif state in sul:
        df.loc[linha, 'regiao'] = 'Sul'
    elif state in nordeste:
        df.loc[linha, 'regiao'] = 'Nordeste'
    elif state in centro_oeste:
        df.loc[linha, 'regiao'] = 'Centro-Oeste'
    elif state in norte:
        df.loc[linha, 'regiao'] = 'Norte'

print(df.to_string())

writer = pd.ExcelWriter('dados_assinantes.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Assinantes', index=False)
writer._save()
writer.close()

