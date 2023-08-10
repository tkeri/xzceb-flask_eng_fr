'''
Translater functions
'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    Translate the english text to french.
    '''
    return MyMemoryTranslator(source='english', target='french').translate(english_text)

def french_to_english(french_text):
    '''
    Translate the french text to english.
    '''
    return MyMemoryTranslator(source='french', target='english').translate(french_text)
