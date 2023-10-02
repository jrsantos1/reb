from carteira import Carteira

class AssetAllocation:
    
    
    @classmethod
    def get_pesos_otimos(cls, carteira: Carteira):
        df_carteira = carteira.precos
        return [.25 for i in range(4)]