from pathlib import Path
import os

#listando arquivos de uma pasta
#print(os.listdir(Path.cwd()))
#print(list(Path.cwd().glob('*')))  

#listando arquivos de uma determinada extensão
#print(list(Path.cwd().glob('*.py')))  

#listar tudo dentro de uma pasta
#print(list(Path.cwd().glob('**/*')))

#validando caminhos
nao_existe = Path.home() / 'nao_existe'
print(nao_existe.exists())  # Verifica se o caminho existe
#print(Path.home().exists())  # Verifica se o caminho existe

#verificando se é arquivo ou pasta
print(Path(__file__))
print(Path(__file__).is_file())  # Verifica se é um arquivo

print(Path(__file__).parent)   
print(Path(__file__).parent.is_file())   
print(Path(__file__).parent.is_dir())  