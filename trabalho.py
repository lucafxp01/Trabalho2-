import numpy as np
import datetime 

# Carregar o csv em um array
array = np.genfromtxt("vendas.csv", delimiter=",", dtype=None, names=True, encoding="utf-8")
print(array)

# Conversão das colunas
datas = np.array([row[0] for row in array], dtype="str")
quantidade_vendida = np.array([row[3] for row in array], dtype="float")
preco_unitario = np.array([row[4] for row in array], dtype="float")
valores_totais = np.array([row[5] for row in array], dtype="float")

# Cálculos 
media_valor_total = np.mean(valores_totais)
mediana_valor_total = np.median(valores_totais)
desvio_padrao = np.std(valores_totais)
print(f"A média dos valores totais das vendas é de: {media_valor_total:.2f}")
print(f"A mediana do valor total das vendas é de: {mediana_valor_total:.2f}")
print(f"Desvio padrão do valor total das vendas: {desvio_padrao:.2f}")

# Produto com maior quantidade vendida e maior valor total de venda
produtos, indices = np.unique(array['Produto'], return_inverse=True)
quantidades_por_produto = np.bincount(indices, weights=quantidade_vendida)
valores_totais_por_produto = np.bincount(indices, weights=valores_totais)

produto_mais_vendido = produtos[np.argmax(quantidades_por_produto)]
produto_maior_valor_total = produtos[np.argmax(valores_totais_por_produto)]

print(f"Produto com a maior quantidade vendida: {produto_mais_vendido}")
print(f"Produto com o maior valor total de vendas: {produto_maior_valor_total}")

# Cálculo do valor total de vendas por região
regioes, indices_regioes = np.unique(array['Região'], return_inverse=True)
valores_totais_por_regiao = np.bincount(indices_regioes, weights=valores_totais)

# Exibir os valores totais por região
for regiao, valor_total in zip(regioes, valores_totais_por_regiao):
    print(f"Valor total de vendas na região {regiao}: {valor_total:.2f}")

# Venda média por dia
datas_unicas, indices_datas = np.unique(datas, return_inverse=True)
vendas_totais_por_dia = np.bincount(indices_datas, weights=valores_totais)
venda_media_por_dia = np.mean(vendas_totais_por_dia)

print(f"Venda média por dia: {venda_media_por_dia:.2f}")

# Análise Temporal
datas_datetime = np.array([datetime.datetime.strptime(data, '%Y-%m-%d') for data in datas])
dias_da_semana = np.array([data.weekday() for data in datas_datetime])
vendas_por_dia_da_semana = np.bincount(dias_da_semana, weights=valores_totais)

dia_mais_vendas = np.argmax(vendas_por_dia_da_semana)
print(f"Dia da semana com o maior número de vendas: {dia_mais_vendas} (0 = Segunda, ..., 6 = Domingo)")

# Variação diária no valor total de vendas
variacao_diaria_vendas = np.diff(vendas_totais_por_dia)

# Variação diária
print("Variação diária no valor total de vendas:")
for variacao in variacao_diaria_vendas:
    print(f"{variacao:.2f}")
