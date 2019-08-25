import json
import traceback
import difflib

def loadData():
  return json.load(open('data.json'))

def printDefinitions(wordList):
  for i in wordList:
    print(f'* {i}')
  print()

def menuInput(wordList):
  choice = input('Enter your choice: ')
  try:
    choice = int(choice) - 1
    if choice < 0 or choice > len(wordList):
      raise IndexError('Choice entered does not exists. Enter a valid choice.')
    choice = wordList[choice]
  except ValueError:
    try:
      choice = checkList(wordList, choice)
    except KeyError:
      raise KeyError('Word entered is not found in the list of options.')
  return choice

def closeMatchMenu(wordList):
  if len(wordList) == 0:
    raise Exception()
  counter = 1
  for i in wordList:
    print(f'{counter}: {i}')
    counter = counter + 1
  return menuInput(wordList)

def checkKey(dict, word):
  value = ''
  try:
    checkList(dict.keys(), word)
    value = dict[word]
  except KeyError:
    raise KeyError()
  return value

def checkList(lst, word):
  value = ''
  for i in lst:
    if i.lower() == word.lower():
      value = i
  if value == '':
    raise KeyError()
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
      #traceback.print_exc()
      raise Exception('** ERROR: This word doesn\'t exist. Please check the word. **')
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
      try:
        definitions = definition(data, word)
        printDefinitions(definitions)
      except Exception as e:
        print(e)


if __name__ == '__main__': main()