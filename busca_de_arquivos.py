import os
def busca_arquivo(nome, diretorio):
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio , arquivo)) and arquivo == nome:
            return(True)
    return(False)
nome_arq = input("Entre com o nome do arquivo: ")
nome_dir = input("Entre com o nome do diretório: ")

if busca_arquivo(nome_arq, nome_dir):
    print(nome_arq, "foi encontrado em", nome_dir)
else:
    print(nome_arq, "não foi encontrado em", nome_dir)
