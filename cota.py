import pandas as pd
import numpy as np
from carteira import Carteira

class Cota:
    
    __cota_reb_mensal: pd.DataFrame = None
    __cota_sem_reb: pd.DataFrame = None
    __cota_reb_diario = pd.DataFrame = None
    __carteira: Carteira
    
    def __init__(self, pesos, carteira) -> None:
        self.__carteira = carteira 
        self.__monta_cota_reb_mensal(carteira=carteira, pesos=pesos)
        self.__monta_cota_reb_diario(carteira=carteira, pesos=pesos)
        self.__monta_cota_sem_reb(carteira=carteira, pesos=pesos)
    
    @property
    def cota_reb_mensal(self):
        return self.__cota_reb_mensal
    
    @property
    def cota_sem_reb(self):
        return self.__cota_sem_reb
    
    @property
    def cota_reb_diario(self):
        return self.__cota_reb_diario
    
    def get_cota_norm(self, cota: pd.Series):
        cota_aux = cota.copy()
        for i, v in cota_aux.items(): 
            if i == 0:
                cota_aux.iloc[i] = 100
                continue
            cota_aux.iloc[i] = (cota_aux.iloc[i] + 1) * cota_aux.iloc[i-1]
        return cota_aux
            
            
        
    def __monta_cota_reb_mensal(self, pesos: list, carteira: Carteira):
        retornos = carteira.retornos
        proporcao = carteira.precos.copy()
        data_series = carteira.date
        
        for i, v in proporcao.iterrows():
            if i == 0:
                proporcao.iloc[i] = pesos
                continue
            if data_series[i].day ==  1:
                proporcao.iloc[i] = list(map(lambda x: x + 1 ,pesos)) * proporcao.iloc[i - 1]
            else: 
                proporcao.iloc[i] = (retornos.iloc[i] + 1) * proporcao.iloc[i - 1]
        
        proporcao = proporcao.div(proporcao.sum(axis=1), axis=0)
        rentabilidade = proporcao * retornos
        rentabilidade = rentabilidade.sum(axis=1)
        self.__cota_reb_mensal = rentabilidade
                
            
    def __monta_cota_sem_reb(self, pesos: list, carteira: Carteira):
        retornos = carteira.retornos
        proporcao = carteira.precos.copy()
        data_series = carteira.date
        
        for i, v in proporcao.iterrows():
            if i == 0:
                proporcao.iloc[i] = pesos
                continue
            if data_series[i].day ==  1:
                proporcao.iloc[i] = pesos
            else: 
                proporcao.iloc[i] = (retornos.iloc[i] + 1) * proporcao.iloc[i - 1]
        
        proporcao = proporcao.div(proporcao.sum(axis=1), axis=0)
        self.__cota_sem_reb = proporcao
        
    def __monta_cota_reb_diario(self, pesos: list, carteira: Carteira):
        retornos = carteira.retornos
        proporcao = carteira.precos.copy()
        data_series = carteira.date
        
        for i, v in proporcao.iterrows():
            if i == 0:
                proporcao.iloc[i] = pesos
                continue
            if data_series[i].day ==  1:
                proporcao.iloc[i] = pesos
            else: 
                proporcao.iloc[i] = (retornos.iloc[i] + 1) * proporcao.iloc[i - 1]
        
        proporcao = proporcao.div(proporcao.sum(axis=1), axis=0)
        self.__cota_reb_diario = proporcao
        
        
    