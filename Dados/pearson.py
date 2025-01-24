import pandas as pd
from scipy.stats import pearsonr

arquivo_excel = ('Dados/base_de_dados_Regressão.xlsx')

dados = pd.read_excel(arquivo_excel)

print(dados.head())

temperaturas = dados['Temperatura (Graus Celsius)']
vendas_sorvete = dados['Vendas de Sorvete (Quantidade)']

correlacao, _ = pearsonr(temperaturas, vendas_sorvete)

print(f"Coeficiente de correlação de Pearson: {correlacao:.4f}")