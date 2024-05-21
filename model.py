from deep_translator import GoogleTranslator
import json

with open('languages.json') as json_file:
    data = json.load(json_file)
    lang1 = data['Language1']
    lang2 = data['Language2']

def translate_from(text):
    translated_text = GoogleTranslator(source='auto', target=lang1).translate(text)
    return translated_text

def translate_to(text):
    translated_text = GoogleTranslator(source=lang1, target=lang2).translate(text)
    return translated_text
