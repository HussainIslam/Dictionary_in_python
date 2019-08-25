import json
import traceback
import difflib

def loadData():
  return json.load(open('data.json'))

def printDefinitions(wordList):
  for i in wordList:
    print(f'* {i}')
  print()

def closeMatchMenu(wordList):
  counter = 1
  for i in wordList:
    print(f'{counter}: {i}')
    counter = counter + 1
  choice = input('Enter your choice: ')
  return wordList[int(choice) - 1]

def checkKey(dict, word):
  value = ''
  for i in dict.keys():
    if i.lower() == word.lower():
      value = dict[i]
  if value == '':
    raise KeyError('Key not found in the dictionary')
  return value

def definition(dict, word):
  retValue = ''
  try:
    retValue = checkKey(dict, word)
  except KeyError:
    try:
      actualWord = closeMatchMenu(difflib.get_close_matches(word, dict.keys()))
      retValue = checkKey(dict, actualWord)
    except:
      traceback.print_exc()
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
      definitions = definition(data, word)
      printDefinitions(definitions)


if __name__ == '__main__': main()