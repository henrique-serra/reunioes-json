import requests
import json

months = [
   '01',
   '02',
   '03',
   '04',
   '05',
   '06',
   '07',
   '08',
   '09',
   '10',
   '11',
   '12',
]

def fetchMeetings(year, month):
  url = f'https://legis.senado.leg.br/dadosabertos/comissao/agenda/mes/{year}{month}.json'
  filename = f'{year}{month}-reunioes.json'
  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    with open(filename, 'w', encoding='utf-8') as file:
      json.dump(data, file, indent=2, ensure_ascii=False)

    print(f'File saved successfully')

  except requests.exceptions.RequestException as e:
      print(f'Erro na requisição: {e}')
  except json.JSONDecodeError as e:
      print(f'Erro ao decodificar JSON: {e}')
  except Exception as e:
      print(f'Erro inesperado: {e}')

for i in range(12):
  fetchMeetings('2023', months[i])