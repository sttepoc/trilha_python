from pathlib import Path

#Script para encontrar um arquivo específico dentro da pasta home
caminho_home = Path.home()
#Loop tendo a estensão do arquivo como critério
'''
for arquivo in caminho_home.glob('**/*'):
    if arquivo.is_file():
        if arquivo.name == 'comandos_git.txt':
           print(arquivo)
#Loop sem ter a estensão do arquivo como critério
for arquivo in caminho_home.glob('**/*'):
    if arquivo.is_file():
        if arquivo.stem == 'comandos_git':
            print(arquivo)
'''
def encontrar_arquivo(caminho_home,nome_arquivo):
    for arquivo in caminho_home.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_arquivo:
                print(arquivo)

encontrar_arquivo(Path.cwd(), "fms.py")