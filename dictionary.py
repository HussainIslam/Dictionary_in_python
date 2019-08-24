import json



def loadData():
  return json.load(open('data.json'))



def main():
  data = loadData()
  exit = True
  while True:
    word = input('Enter Word (:exit to quit): ')
    if word == ':exit':
      break
    else:
      print(data[word])


if __name__ == '__main__': main()