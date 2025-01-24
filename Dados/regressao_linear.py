import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

arquivo_excel = 'Dados/base_de_dados_Regressão.xlsx'
dados = pd.read_excel(arquivo_excel)

print(dados.head())

X = dados['Temperatura (Graus Celsius)'] 
y = dados['Vendas de Sorvete (Quantidade)']

X = sm.add_constant(X)

modelo = sm.OLS(y, X).fit()

print("\nResumo da Regressão Linear:")
print(modelo.summary())

y_pred = modelo.predict(X)

residuos = y - y_pred


plt.figure(figsize=(8,6))
plt.scatter(X['Temperatura (Graus Celsius)'], residuos, color='blue')
plt.axhline(y=0, color='red', linestyle='--')  
plt.title('Gráfico de Resíduos')
plt.xlabel('Temperatura (Graus Celsius)')
plt.ylabel('Resíduos')
plt.show()
