
# Desafio:
#Você faz parte da equipe de Analytics de uma grande marca de vestuário com mais de 25 lojas espalhadas em Shoppings de todo o Brasil.
#Toda semana você precisa enviar para a diretoria um relatorico atualizado com as 25 lojas contendo as seguintes informações:
#- Ranking com maior faturamento
#- Faturamento de cada Loja
#- Quantidade de Produtos Vendidos de cada Loja
#- Ticket Médio dos Produto de cada Loja
#- Esse relatório é sempre enviado como um resumo de todos os dados disponíveis no ano.

#Para resolver o desafio vamos seguir a seguinte lógica:
#- Passo 1 - Importar a base de Dados
#- Passo 2 - Visualizar a Base de Dados para ver se precisamos fazer algum tratamento
#- Passo 3 - Calcular os indicadores de todas as lojas: Faturamento por Loja Quantidade de Produtos Vendidos por Loja Ticket Médio dos Produto por Loja
#- Passo 4 - Calcular os indicadores de cada loja
#- Passo 5 - Enviar e-mail para a diretoria



# pip3 install wheel
# pip3 install pandas
# pip3 install xlrd
# pip3 install openpyxl



# Passo 1: Importar a base de dados

import pandas as pd

tabela_vendas = pd.read_excel('Vendas.xlsx', engine='openpyxl')


#Passo 2: Calcular o faturamento da Loja
tabela_faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
tabela_faturamento = tabela_faturamento.sort_values(by="Valor Final",ascending=False)

# Passo 3: Calcular a quantidade de produtos vendida em cada Loja
tabela_quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
tabela_quantidade = tabela_quantidade.sort_values(by="Quantidade",ascending=False)

# Passo 4 Calcular o ticket medio
ticket_medio = (tabela_faturamento["Valor Final"] / tabela_quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Medio"})
ticket_medio = ticket_medio.sort_values(by="Ticket Medio",ascending=False)

# Função enviar e-mail:
def enviar_email(nome_da_loja, tabela):
  import smtplib
  import email.message

  server = smtplib.SMTP('smtp.gmail.com:587')
  corpo_email = f'''
  <p> Prezados, </p>
  <p> Segue relatório de vendas</p>
  {tabela.to_html()}
  <p>Qualquer dúvida estou à disposição </p>
  ''' #Vamos editar

  msg = email.message.Message()
  msg['Subject'] = f"Relatorio de Vendas - {nome_da_loja}" #Vamos editar

  # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
  # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
  # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha

  msg['From'] = '' #Vamos editar coloque seu endereço de email
  msg['To'] = '' #Vamos editar coloque o endereço para quem deseja enviar o email
  password = "" #Vamos editar coloque a senha do seu email
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_email )

  s = smtplib.SMTP('smtp.gmail.com: 587')
  s.starttls()
  # Login Credentials for sending the mail
  s.login(msg['From'], password)
  s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
  print('Email enviado')

# Passo 5: Enviar o e-mail
tabela_completa = tabela_faturamento.join(tabela_quantidade).join(ticket_medio)
enviar_email("Diretoria", tabela_completa)





#
