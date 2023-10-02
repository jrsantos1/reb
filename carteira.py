import pandas as pd 

class Carteira: 
    __df_carteira_precos: pd.DataFrame = None
    __df_carteira_retornos: pd.DataFrame = None
    __date = pd.Series
    
    def __init__(self, ativos: list):
        self.__monta_carteira(ativos)
    
    @property
    def precos(self):
        return self.__df_carteira_precos
    
    @property
    def retornos(self):
        return self.__df_carteira_retornos
    
    @property
    def date(self):
        return self.__date
    
    def __monta_carteira(self, ativos):
        df_aux = pd.read_excel('dados/resultado.xlsx')
        df_aux['Date'] = pd.to_datetime(df_aux['Date'], format='%Y-%m-%d')
        self.__df_carteira_precos = df_aux.drop(index=0).reset_index(drop=True).drop('Date', axis=1)
        self.__df_carteira_retornos = df_aux[df_aux.columns[1:]].pct_change().dropna().reset_index(drop=True)
        self.__date = df_aux['Date']
    
    
    
    
    
    