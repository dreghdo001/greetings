from list import greetings
from translate import Translator


translator = Translator(to_lang='pt')

st = ""
for g in greetings:
    print(translator.translate(g))


