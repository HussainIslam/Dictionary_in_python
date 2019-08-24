import json


def loadData():
  data = json.load(open('data.json'))
  print(data['rainn'])

loadData()