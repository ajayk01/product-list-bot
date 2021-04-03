from googletrans import Translator

translator = Translator()
print(translator.detect("ரெட்மி தொலைபேசி 64 எம்பி கேமரா 6 ஜிபி ராம்"))

translated = translator.translate('ரெட்மி தொலைபேசி 64 எம்பி கேமரா 6 ஜிபி ராம்', src='tamil', dest='hindi')

print(translated.text)