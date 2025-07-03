from pathlib import Path
import os
'''
#Retornando caminho absoluto do diretório atual
print(Path.cwd())

#Esse caminho é absoluto
print(Path.cwd().is_absolute())

#Retornando caminho da primeira pasta
print(Path('primeira_pasta'))

#Esse caminho é absoluto
print(Path('primeira_pasta').is_absolute())

#Transformando caminho relativo em absoluto
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())  # Verifica se a pasta existe

os.chdir(Path.home())
print((Path.cwd() / 'primeira_pasta').exists())
'''
'''
#Garantindo que estamos retornando o caminho para a pasta do script
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent)

print((Path(__file__).parent / 'primeira_pasta').exists())
'''
#Trabalhando com partes de um caminho
caminho_arquivo = Path(__file__)

print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(caminho_arquivo.parent)    
print(caminho_arquivo.parent.parent)    
print(caminho_arquivo.name)
print(caminho_arquivo.stem)  # Nome do arquivo sem extensão
print(caminho_arquivo.suffix)  # Extensão do arquivo
print(caminho_arquivo.drive)    # Unidade de disco (apenas no Windows)

print(caminho_arquivo.parents[2])  # Caminho do diretório dois níveis acima