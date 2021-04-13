"""from translate import Translator
translator= Translator(from_lang="turkish",to_lang="english")
translation = translator.translate("rendelenmiş")
print (translation)"""

from googletrans import Translator
translator = Translator()
result = translator.translate('kuzu but')

print(result.src)
print(result.dest)
print(result.text)