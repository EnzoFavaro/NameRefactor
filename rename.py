import os
import csv

path = r"D:\Usuário\Documents\Trabalho\Azuton\Alterar pastas migração\teste"
directory_list = os.listdir(path)

arquivo = open('empresas.csv', encoding="ISO-8859-1")
client_list = csv.DictReader(arquivo)

for client in client_list:

    for file in directory_list:
        if file == client['cliente_id']:
            os.rename(os.path.join(path, file),
                      os.path.join(path, client['nome']))
            break
        if len(file) <= 3:
            novo_nome = file + " (Essa empresa não existe mais)"
            os.rename(os.path.join(path, file),
                      os.path.join(path, novo_nome))
