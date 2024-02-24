# Dicionário existente
companies = {
    "raizen": "tecnology",
    "amdn": "administration",
    "castle": "contability"
}

# Adiciona nova empresa ao dicionário
companies["forecast"] = "data analysis"

# Mostra o dicionário atualizado
print(companies)

# Itera sobre o dicionário e imprime cada chave-valor
for symbol in companies:
    print(symbol, companies[symbol])

# Imprime todas as chaves do dicionário
print(companies.keys())

# Imprime todos os valores do dicionário
print(companies.values())

# Tenta remover a chave com a escrita correta
companies.pop('forecast')  # Use 'forecast' em vez de 'Forecast' para corresponder à chave adicionada

# Mostra o dicionário após a remoção
print(companies)

# Verificação da existência da chave 'forecast' após a remoção
if "forecast" in companies:
    print('sim')
else:
    print('não')
