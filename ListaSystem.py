import re
import pandas as pd

# Lista para armazenar os nicks
nicks_list = []

# Padrão de expressão regular para encontrar nicks em linhas numeradas
nick_pattern = re.compile(r'^\d+\.\s+([^\[\]\n]+)')

# Caminho relativo para o arquivo texto
input_file_path = 'lista_completa.txt'

# Ler o arquivo texto
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Procurar por padrões de nicks em linhas numeradas
        match = re.search(nick_pattern, line)
        if match:
            # Adicionar nick à lista
            nicks_list.append(match.group(1))

# Criar um DataFrame com os nicks
nicks_df = pd.DataFrame({'nick': nicks_list})

# Remover possíveis duplicatas
nicks_df = nicks_df.drop_duplicates()

# Caminho relativo para o arquivo CSV
output_file_path = 'nicks.csv'

# Salvar os nicks em um novo arquivo CSV, sobrescrevendo o conteúdo existente
nicks_df.to_csv(output_file_path, index=False, header=False, mode='w')

print("Nicks salvos com sucesso em nicks.csv")
