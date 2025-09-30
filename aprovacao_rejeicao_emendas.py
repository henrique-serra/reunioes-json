import os
import json
from pprint import pprint

def formatDate(date):
  day = date[8:10]
  month = date[5:7]
  year = date[:4]
  return f'{day}/{month}/{year}'

def getMeetingsOfComission(meetings, comissionId):
  AgendaReuniao = meetings.get('AgendaReuniao')
  if AgendaReuniao:
    reunioes = AgendaReuniao.get('reunioes')
    if reunioes:
      meetingArray = reunioes.get('reuniao', [])
      if meetingArray:
        meetingsOfComission = [
          r for r in meetingArray
          if r.get('colegiadoCriador', {}).get('codigo') == comissionId
        ]
        return meetingsOfComission
  return

def getPLsAprovaRejeitaEmendas(meetings, comisisonId):
  meetingsOfComission = getMeetingsOfComission(meetings, comisisonId)
  
  if not meetingsOfComission:
    return
  
  pls = []

  def listOrDict(obj, callback):
    if isinstance(obj, list):
      for el in obj:
        callback(el)
    elif isinstance(obj, dict):
      callback(obj)

  for meeting in meetingsOfComission:
    partes = meeting.get('partes')
    
    def processItem(item):
      nome = item.get('nome')
      isAprovaRejeitaEmendas = 'Pela aprovação' in item.get('relatorio')

      if isAprovaRejeitaEmendas:
        pls.append(nome)

    def processParte(parte):
      if meeting.get('realizada') == 'true'and parte and parte.get('isDeliberativa') == 'true':      
        for item in parte.get('itens'):
          listOrDict(item, processItem)
      
    listOrDict(partes, processParte)

  return pls

def process_file(filepath):
  with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

  resultado = getPLsAprovaRejeitaEmendas(data, '59')
  return resultado

for filename in os.listdir('.'):
  if filename.endswith('json'):
    print(f"🔎 Processando {filename}...")
    resultado = process_file(filename)
    print(f"✅ Resultado para {filename}: {resultado}\n")