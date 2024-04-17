import numpy as np
import matplotlib.pyplot as plt # type: ignore
import pandas as pd

# Lê os dados do arquivo .txt para um DataFrame do pandas
tabela = pd.read_csv('sla_1.txt' , sep = ';', header = 0)

x = tabela['Nome'] # Seleciona a primeira coluna
y = tabela['Data'] # Seleciona a segunda coluna
z = tabela['Alt'] # Seleciona a terceira coluna

plt.scatter(x,y, color = 'black', label = 'Legenda')

plt.legend(loc='best')

plt.xlabel('nome do eixo x', size = 10)
plt.ylabel('nome do eixo y', size = 10)
plt.title('Título do Gráfico', size = 15)

# Caminho para salvar o arquivo Excel
caminho_arquivo_excel = 'C:\\Users\\Jilso\\OneDrive\\Área de Trabalho\\projetos freela\\arquivo2.xlsx'

# Salva o DataFrame como um arquivo Excel
tabela.to_excel(caminho_arquivo_excel, index=False)