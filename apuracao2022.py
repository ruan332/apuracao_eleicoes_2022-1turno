import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

json_data = json.loads(data.content)

candidato = []
numero = []
votos = []
porcentagem = []
eletio = []

for informacoes in json_data['cand']:
    
    if informacoes['seq'] in ['1', '2', '3', '4']:
        numero.append(informacoes['n'])
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])
        eletio.append(informacoes['st'])
        
df_eleicao = pd.DataFrame(list(zip(numero, candidato, votos, porcentagem, eletio)), columns = [
    'Nº', 'Candidato', 'Nº de Votos', 'Porcentagem', 'Eleito?'
])

print(df_eleicao)
