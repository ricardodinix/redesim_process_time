import pandas as pd
import os
import warnings
from unidecode import unidecode
from layout.capitais import capitais

warnings.filterwarnings('ignore')

# parte 1: ler e converter os arquivos xlsx em csv

class ConvertXlsx:
    def __init__(self, dir_origin: str, dir_destinarion:str):
        self.dir_origin = dir_origin
        self.dir_destinarion = dir_destinarion
    
    def __archives(self):
        return os.listdir(self.dir_origin)
        
    def load_data_excel(name_archive):
        new_name_archive = name_archive[0:-5]
        path_origin = self.dir_origin + name_archive
        path_destination = self.dir_destinarion + new_name_archive+'.csv'
        print(f'Lendo o arquivo {name_archive}')
        df = pd.read_excel(path_origin, skiprows=1)
        print(f'Exportando o arquivo {new_name_archive}.csv')
        df.to_csv(path_destination,index=False,sep=';')
        linhas_processadas = df.shape[0]
        print(f'Foram processadas {linhas_processadas} linhas')
        print('-----------------------')


archives = os.listdir('databases/xlsx')

def load_data_excel(name_archive):
    
    new_name_archive = name_archive[0:-5]
    path_origin = 'databases/xlsx/'+name_archive
    path_destination = 'databases/csv/'+new_name_archive+'.csv'

    print(f'Lendo o arquivo {name_archive}')

    df = pd.read_excel(path_origin, skiprows=1)

    print(f'Exportando o arquivo {new_name_archive}.csv')
    df.to_csv(path_destination,index=False,sep=';')
    linhas_processadas = df.shape[0]
    print(f'Foram processadas {linhas_processadas} linhas')
    print('-----------------------')

count = 0
for i in archives:
    load_data_excel(i)
    count+=1
    print(f'{count}/{len(archives)}')

