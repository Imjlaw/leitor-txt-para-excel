import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore

# Lê os dados do arquivo .txt para um DataFrame do pandas
tabela = pd.read_csv('sla_1.txt' , sep = ';' , header = 0)

x = tabela['Nome'] # Seleciona a primeira coluna
y = tabela['Data'] # Seleciona a segunda coluna
z = tabela['Alt'] # Seleciona a terceira coluna

# Caminho para salvar o arquivo Excel
caminho_arquivo_excel = 'C:\\Users\\Jilso\\OneDrive\\Área de Trabalho\\projetos freela\\arquivo3.xlsx'

# Salva o DataFrame como um arquivo Excel
tabela.to_excel(caminho_arquivo_excel, index=False)

