# python3.10.4

import pandas as pd

class SpreadSheet:

    def __init__(self, path_spreadsheet: str, skiprows: int):
        self.path_spreadsheet = path_spreadsheet
        self.skiprows = skiprows

    def read_xlsx(self):
        df = pd.read_excel(self.path_spreadsheet, self.skiprows)
        return df


class ETLSpreadSheet:

    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def __drop_cnae_secundaria(self):
        return self.dataframe[self.dataframe.columns.drop(list(\
            self.dataframe.filter(regex='CNAE SECUNDARIA')))]

    def __filter_forma_atuacao(self):
        return self.__drop_cnae_secundaria()[self.__drop_cnae_secundaria().columns.\
            drop(list(self.__drop_cnae_secundaria().filter(regex='FORMA ATUACAO')))]
    
    def __create_data_deferimento(self):
        df = self.__filter_forma_atuacao()['DATA DEFERIMENTO'] = \
            pd.to_datetime(self.__filter_forma_atuacao()['DATA DEFERIMENTO'],format='%d/%m/%Y', errors='ignore')
        return df

if __name__=='__main__':
    spread_sheet = SpreadSheet(path_spreadsheet='databases/xlsx/tempos-abertura-Brasil12019.xlsx',skiprows=1)
    etl_spread_sheet = ETLSpreadSheet(dataframe=spread_sheet)
    etl_spread_sheet_process = etl_spread_sheet.__create_data_deferimento()
    print(etl_spread_sheet_process)


    

