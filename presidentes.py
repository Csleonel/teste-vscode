#PRIMEIRO NÓS VAMOS IMPORTAR AS BIBLIOTECAS NUMPY E PANDAS,
#QUE SÃO FERRAMENTAS DE ANÁLISE DE DADOS,
#RÁPIDAS E FÁCEIS DE ALTO DESEMPENHO.
import numpy as np
import pandas as pd
import csv 

#SELECIONAR O ARQUIVO .CSV NO QUAL ESTÁ A NOSSA ESTRUTURA DE DADOS
data = pd.read_csv("presidentes.csv")
print(data.head())

#COMANDO PARA SELECIONAR COLUNA DENTRO DO ARQUIVO .CSV
altura = np.array(data["Altura(cm)"])
print (altura)

#COMANDO PARA SELECIONAR COLUNA DENTRO DO ARQUIVO .CSV
nome = np.array(data["Nome Completo"])
print(nome)

#INFORMAÇÕES SOBRE A ALTURA E ANALISE DOS DADOS QUE JÁ TEMOS
print("Média de altura dos presidentes =", altura.mean())
print("Média de variação de altura =", altura.std())
print("Menor altura =", altura.min ())
print("Maior altura =", altura.max())
print("Median =", np.median(altura))
print("percentual do 25º presidente =", np.percentile(altura, 25))

#A BIBLIOTECA MATPLOTLIB TORNA POSSIVEL A APRESENTAÇÃO DE INSIGHTS
#FAZ A CRIAÇÃO DE GRAFICOS 2D e 3D
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#USANDO A FERRAMENTA PLT PARA A CRIAÇÃO DO GRÁFICO
plt.hist(altura) #DADOS QUE SERÃO USADOS
plt.title("Distribuição da altura dos presidentes do Brasil") #TÍTULO DO GRÁFICO
plt.xlabel("Altura(cm)") #LINHA X
plt.ylabel("Número") #LINHA Y
plt.show() 