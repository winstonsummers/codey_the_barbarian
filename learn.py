import sys
import os.path
import json

order = 3

def readArguments():
	numArugments = len(sys.argv) - 1
	dictionaryFile = "dictionary.json"
	inputFile = ""

	if numArugments >= 1:
		dictionaryFile = sys.argv[1]
	if numArugments >= 2:
		inputFile = sys.argv[2]

	return dictionaryFile, inputFile

def loadDictionary(filename):
	if not os.path.exists(filename):
		file = open(filename, 'w')
		json.dump( {}, file)
		file.close()

	file = open(filename, 'r')
	dictionary = json.load(file)
	file.close()
	return dictionary

def learn(dict, input):
	tokens = input.split(" ")
	for word in range(0, len(tokens)-order):
		currentWord = " ".join(tokens[word:word+order])
		nextWord = " ".join(tokens[word+order:word+1+order])

		if currentWord not in dict:
			#create new word in dictionary
			dict[currentWord] = { nextWord: 1 }
		else:
			#current word already in dictionary
			allNextWords = dict[currentWord]

			if nextWord not in allNextWords:
				#add new next state
				dict[currentWord][nextWord] = 1
			else:
				#already exists add one
				dict[currentWord][nextWord] += 1

	return dict

def updateFile(filename, dictionary):
	file = open(filename, "w")
	json.dump(dictionary, file)
	file.close()

def main():
	dictionaryFile, inputFile = readArguments()
	dictionary = loadDictionary(dictionaryFile)

	if inputFile == '':
		#make things interactive
		while True:
			userInput = input(">> ")
			if userInput == '':
				break

			dictionary = learn(dictionary, userInput)
			updateFile(dictionaryFile, dictionary)
	else:
		#read the file
		print("This may take a minute...")
		book = open(inputFile, 'r')
		content = book.read().replace('.', '').replace(',', '')
		dictionary = learn(dictionary, content)
		updateFile(dictionaryFile, dictionary)
		book.close()

main()