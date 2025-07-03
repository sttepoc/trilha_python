from pathlib import Path
import shutil
#criando pasta
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino4'
caminho_pasta_destino.mkdir(exist_ok=True)
'''
#criando pasta com todas as pastas anteriores necessárias
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino5' / 'subpasta51'
caminho_pasta_destino.mkdir(parents=True)
'''

#copiando pastas
'''
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'destino5', pasta_atual / 'destino1' / 'destino5')
'''

#deletando pastas vazias
'''
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino5' / 'subpasta51'
pasta_remover.rmdir()  # Deleta a pasta se estiver vazia
'''
'''
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1' 
pasta_remover.rmdir()  # Deleta a pasta se estiver vazia
'''
#deletando pastas com conteúdo

pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1' 
shutil.rmtree(pasta_remover)  # Deleta a pasta e todo o seu conteúdo