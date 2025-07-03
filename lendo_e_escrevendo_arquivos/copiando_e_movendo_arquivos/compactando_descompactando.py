from pathlib import Path
import shutil   

#compactando arquivos
'''
pasta_atual = Path(__file__).parent
pasta_a_ser_compactada = pasta_atual 
nome_arquivo = pasta_atual / 'compactado'
shutil.make_archive(nome_arquivo, 'zip', pasta_a_ser_compactada)
'''
#descompactando arquivos
pasta_atual = Path(__file__).parent
pasta_a_ser_descompactada = pasta_atual /'compactado.zip'
pasta_descompactada = pasta_atual / 'descompactado'
shutil.unpack_archive(pasta_a_ser_descompactada, pasta_descompactada, 'zip')