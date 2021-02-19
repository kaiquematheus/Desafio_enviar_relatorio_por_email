# Instalação por Gerenciadores de Pacotes


Para instalar o Python 3, digite em um terminal:
```
$ sudo apt-get install python3
```

Para instalar o gerenciador de pacotes pip, digite em um terminal:
```
$ sudo apt-get install python3-pip
```

Python
> Uma vez que o Python estiver instalado em seu computador, você estará pronto para criar e executar seu primeiro programa! Para criar um programa Python, crie um arquivo com a extensão .py, contendo o código do seu programa. Após salvar o arquivo, abra o terminal (ou o prompt de comando), navegue para a pasta onde você criou o arquivo, e digite:

```
$ python nomeDoArquivo.py
```

Comandos para usar a biblioteca pandas

```
# pip3 install wheel
# pip3 install pandas
# pip3 install xlrd
# pip3 install openpyxl
```

# Desafio:
Você faz parte da equipe de Analytics de uma grande marca de vestuário com mais de 25 lojas espalhadas em Shoppings de todo o Brasil.
Toda semana você precisa enviar para a diretoria um relatório atualizado com as 25 lojas contendo as seguintes informações:
- Ranking com maior faturamento
- Faturamento de cada Loja
- Quantidade de Produtos Vendidos de cada Loja
- Ticket Médio dos Produto de cada Loja
- Esse relatório é sempre enviado como um resumo de todos os dados disponíveis no ano.

Para resolver o desafio vamos seguir a seguinte lógica:
- Passo 1 - Importar a base de Dados
- Passo 2 - Visualizar a Base de Dados para ver se precisamos fazer algum tratamento
- Passo 3 - Calcular os indicadores de todas as lojas: Faturamento por Loja Quantidade de Produtos Vendidos por Loja Ticket Médio dos Produto por Loja
- Passo 4 - Calcular os indicadores de cada loja
- Passo 5 - Enviar e-mail para a diretoria
