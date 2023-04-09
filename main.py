#importação 
import pandas as pd

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

tabela_vendas = pd.read_excel('janeiro.xlsx')
print(tabela_vendas)