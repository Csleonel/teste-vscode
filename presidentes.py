import numpy as np
import pandas as pd
import csv 

data = pd.read_csv("presidentes.csv")
#print(data.head())

altura = np.array(data["Altura(cm)"])
#print (altura)

nome = np.array(data["Nome Completo"])
#print(nome)

print("Média de altura dos presidentes =", altura.mean())
print("Média de variação de altura =", altura.std())
print("Menor altura =", altura.min ())
print("Maior altura =", altura.max())
print("Median =", np.median(altura))
print("percentual do 25º presidente =", np.percentile(altura, 25))

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

plt.hist(altura)
plt.title("Distribuição da altura dos presidentes do Brasil")
plt.xlabel("Altura(cm)")
plt.ylabel("Número")
plt.show()