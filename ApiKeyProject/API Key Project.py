import requests
# pip install requests
from googletrans import Translator
import json

# pip install googletrans==3.1.0a0

translator = Translator()
# word dictionary
API_KEY = 'api'
base_url = "https://api.dictionaryapi.dev/"

# Enter the dictionary language
# For example: English = en, Chinese = zh-CN
# https://developers.google.com/admin-sdk/directory/v1/languages
language = input('Enter a Language code: \n')

# word to define
word = input("Enter the Word: \n")

# website address to open dictionary
complete_url = base_url + API_KEY + "/v2/entries/en/" + word
response = requests.get(complete_url).json()

# to translate the words and sentences
def translate(i):
    out = translator.translate(i, dest=language)
    return out.text

# to define a word
def definition():
    try:
        for i in range(len(response[0]['meanings'])):
            print(str(i + 1))
            print(translate("Part Of Speech") + ": " + translate(message[0]['meanings'][i]["partOfSpeech"]))
            print(translate("Definitions") + ": " + translate(message[0]['meanings'][i]["definitions"][0]["definition"]))
    except:
        try:
            print(message["title"])
            print(message["message"])
        except:
            return None

# calling out the word with translate
def word():
    try:
        print(translate("Word") + ": " + translate(message[0]["word"]))
    except:
        print("(The Word or Language code is not exist)")

# calling out the phonetic that how word is pronounce
def phonetic():
    try:
        print(translate("Phonetic") + ": " + message[0]["phonetics"][0]["text"])
    except:
        return None

# pronounce audio link
def audio():
    try:
        print(translate("Audio") + ": " + message[0]["phonetics"][0]["audio"])
    except:
        return None

# The example of word use in sentence
def example():
    try:
        print("\n")
        for i in range(len(response[0]['meanings'])):
            print(translate("example") + " " + str(i + 1) + ". " + translate(message[0]['meanings'][i]["definitions"][0]["example"]))
    except:
        return None

# open the file and write the dictionary to the file
with open('API.json', 'w') as file:
    json.dump(response, file)

# read the data from file
with open('API.json') as file:
    message = json.load(file)

# the title
print("Dictionary")

# calling out function
num = 0

word()
phonetic()
audio()
definition()
example()