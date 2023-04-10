#importação 
import pandas as pd
from twilio.rest import Client

# ID da sua conta no twilio
account_sid = "AC1e50d1dfb03526306b7adb18fedf67c9"
# ID da sua conta no twilio
auth_token  = "2916beaf76fa9ead8edc9cc6307d8f9e"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if(tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas{vendas}')
        message = client.messages.create(
            to="+5591983942532", 
             from_="+15074172272",
            body=f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas{vendas}')
        print(message.sid)
       

