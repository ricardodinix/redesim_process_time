#python3.10.4

import pandas as pd
from unidecode import unidecode

def first_word(string):
    text = str(string)
    text = unidecode(text)
    text = text.replace('.','_').replace(' ','_')
    return text.lower()

class SpreadSheet:

    def __init__(self, path_spreadsheet: str, skiprows: int, nrows:int):
        self.path_spreadsheet = path_spreadsheet
        self.skiprows = skiprows
        self.nrows = nrows
    


    def read_xlsx(self):
        df = pd.read_excel(self.path_spreadsheet, skiprows=self.skiprows,nrows=self.nrows)
        return df
    
    def drop_cnae_secundaria(self):
        df = self.read_xlsx()
        df = df[df.columns.drop(list(df.filter(regex='CNAE SECUNDARIA')))]
        return df
    
    def drop_forma_atuacao(self):
        df = self.drop_cnae_secundaria()
        df = df[df.columns.\
            drop(list(df.filter(regex='FORMA ATUACAO')))]
        return df
    
    def create_data_deferimento(self):
        df = self.drop_forma_atuacao()
        df['data_deferimento'] = pd.to_datetime(df['DATA DEFERIMENTO'],format='%d/%m/%Y', errors='ignore')
        return df
    
    def clear_names_columns(self):
        df = self.create_data_deferimento()
        df.columns = [first_word(i) for i in df.columns]
        return df

if __name__=='__main__':
    spread_sheet = SpreadSheet(path_spreadsheet='databases/xlsx/tempos-abertura-Brasil12019.xlsx',skiprows=1, nrows=100).clear_names_columns()
    print(spread_sheet)
