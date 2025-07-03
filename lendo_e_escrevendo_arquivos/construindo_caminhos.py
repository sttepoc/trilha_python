from pathlib import Path

caminho = Path('C:\\Users\\vicen\OneDrive\Documentos\\trilha_python\\lendo_e_escrevendo_arquivos')

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)

print(Path.home()) 