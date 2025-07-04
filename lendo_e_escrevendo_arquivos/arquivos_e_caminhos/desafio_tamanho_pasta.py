from pathlib import Path
import os
 
#desafio tamanho de uma pasta


def retorna_tamanho_dos_diretorios(caminho: Path, profundidade=1, tamanho_linha=0):
    for diretorio in caminho.glob('*'):
        if  diretorio.is_dir() and not diretorio.name.startswith('.'):   
            tamanho_diretorio = 0
            for arquivo in diretorio.glob('**/*'):
                if arquivo.is_file():
                    tamanho_diretorio += os.path.getsize(arquivo)  
            print("--" * tamanho_linha, diretorio.name, round(tamanho_diretorio / 1024 / 1024,2), 'mb')
            if profundidade > 1:
                retorna_tamanho_dos_diretorios(diretorio, profundidade - 1, tamanho_linha + 1)
   
caminho = Path.home() / 'OneDrive'

retorna_tamanho_dos_diretorios(caminho, profundidade=3)