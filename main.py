from carteira import Carteira
from asset_allocation import AssetAllocation
from cota import Cota

ativos = ['BOVA11.SA', 'IRFM11.SA', 'SPXI11.SA', 'IMAB11.SA']

carteira_teorica = Carteira(ativos=['BOVA11.SA', 'IRFM11.SA', 'SPXI11.SA', 'IMAB11.SA'])
pesos = AssetAllocation.get_pesos_otimos(carteira=carteira_teorica)
cota = Cota(carteira=carteira_teorica, pesos=pesos)
cota.cota_reb_mensal
preco_normalizado = cota.get_cota_norm(cota.cota_reb_mensal)
print(preco_normalizado)




