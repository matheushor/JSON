import json

# Carregando os dados do arquivo JSON
with open('faturamento.json') as f:
    dados = json.load(f)

# Calculando o menor e o maior faturamento diário
menor_faturamento = min(dados.values())
maior_faturamento = max(dados.values())

# Calculando a média mensal de faturamento
dias_uteis = len(dados)
soma_faturamento = sum(dados.values())
media_mensal = soma_faturamento / dias_uteis

# Contando os dias em que o faturamento foi superior à média mensal
dias_acima_da_media = sum(faturamento > media_mensal for faturamento in dados.values())

# Exibindo os resultados
print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Média mensal de faturamento: R${media_mensal:.2f}")
print(f"Dias em que o faturamento foi superior à média mensal: {dias_acima_da_media}")
