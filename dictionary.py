import json
import traceback
import difflib

def loadData():
  return json.load(open('data.json'))

def closeMatchMenu(wordList):
  counter = 1
  for i in wordList:
    print(f'{counter}: {i}')
    counter = counter + 1

def definition(dict, word):
  retValue = ''
  try:
    retValue = dict[word.lower()]
  except KeyError:
    try:
      closeMatches = difflib.get_close_matches(word, dict.keys())
      closeMatchMenu(closeMatches)
    except:
      retValue = '** ERROR: This word doesn\'t exist. Please check the word. **'
  except:
    print("Unexpected error.")
  return retValue

def main():
  data = loadData()
  exit = True
  while True:
    word = input('Enter Word (:exit to quit): ')
    if word == ':exit':
      break
    else:
      print(definition(data, word))


if __name__ == '__main__': main()