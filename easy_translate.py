from googletrans import Translator

# This script is intended to translate a text to multiple languages which can be used to improve search results.

text = 'How to convert some text to multiple languages'

destination_languages = {
    'Spanish': 'es',
    'Simplified Chinese': 'zh-CN',
    'Italian': 'it',
    'Hindi': 'hi',
    'Mongolian': 'mn',
    'Russian': 'ru',
    'Ukrainian': 'uk',
    'French': 'fr',
    'Indonesian': 'id',
    'Japanese': 'ja',
    'Slovak': 'sk'
}

translator = Translator()

for key, value in destination_languages.items():
    print(translator.translate(text, dest=value).text)
