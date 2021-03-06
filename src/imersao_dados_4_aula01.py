# -*- coding: utf-8 -*-
"""imersao-dados-4-aula01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MZd5bibRnzIcAfB7kHWlfvIQrAElq4pd

# Aula 01
23/05 - 24/05

Desafios propostos pelos professores:

1) Realizar a média da metragem para cada um dos bairros\
2) Encontrar 2 formas de selecionar os dados por bairro (consultar os métodos na documentação do pandas)\
3) Explorar alguns gráficos na documentação e aplicar nas demais colunas do DataFrame, tentar colocar alguma conclusão\
4) Pegar outras estatísticas dos dados, média, mediana, min, max\
5) Descobrir quais são os bairros que não tem nome de rua
"""

import pandas as pd

url = 'https://gist.githubusercontent.com/tgcsantos/3bdb29eba6ce391e90df2b72205ba891/raw/22fa920e80c9fa209a9fccc8b52d74cc95d1599b/dados_imoveis.csv'
# Panda importa os dads em uma dataframe
dados = pd.read_csv(url)
# Mostra todos os dados
#dados
# Mostra os 5 primeiros registros
#dados.head()
dados.head(10)

# Pega 1 registro aleatório
dados.sample()

# Pega 10 registro aleatório
dados.sample(10)

# Tipo da variável
type(dados)

# Para pegar apenas uma coluna
dados['Bairro']

dados['Bairro'][6522]

# Informações sobre os dados, como o tipo de cada coluna
dados.info()

# Média de uma coluna com números
dados.Metragem.mean()

# Média de metragem dos imóveis do Bairro Vila Mariana
# Para descobrir se tem dados do bairro:
sum(dados['Bairro'] == 'Vila Mariana')
# Resultado = 184 imóveis

# Guarda uma tabela (series) com true (é Vila Mariana) ou false (não é)
tem_imoveis_vila_mariana = (dados['Bairro'] == 'Vila Mariana')
tem_imoveis_vila_mariana

# Retorna apenas as 184 linhas que pertencem a Vila Mariana
imoveis_vila_mariana = dados[tem_imoveis_vila_mariana]
imoveis_vila_mariana

# Por fim, retorna a média da metragem dos imoveis
imoveis_vila_mariana.Metragem.mean()

# Contabiliza o total de imóveis em cada bairro
dados['Bairro'].value_counts()

# Montar um gráfico com os 10 bairros com mais imóveis
n_imoveis_bairro = dados['Bairro'].value_counts()
n_imoveis_bairro.head(10).plot.bar()

