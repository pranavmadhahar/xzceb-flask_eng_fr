from deep_translator import MyMemoryTranslator

ENGLISH_TEXT = 'Keep it up. You are awesome'

def english_tofrench(ENGLISH_TEXT):
    '''Function takes in english text as string argument & returns french translation as output'''
    french_text = MyMemoryTranslator(source='english', target='french').translate(ENGLISH_TEXT)
    return french_text

translated_text1 = english_tofrench("Hello")
print(translated_text1)

FR_TEXT = 'Bonjour le monde'

def french_toenglish(fr_text):
    '''Function takes in french text as string argument & returns english translation as output'''
    eng_text = MyMemoryTranslator(source='french', target='english').translate(fr_text)
    return eng_text

translated_text2 = french_toenglish("Bonjour")
print(translated_text2)

# disabling:
# C0304: Trailing newlines (trailing-newlines)
# pylint: disable=C0304
