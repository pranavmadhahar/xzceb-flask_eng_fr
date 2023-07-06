from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text_1 = 'textToTranslate'
    textToTranslate = request.args.get(text_1)
    translatedText1 = translator.english_tofrench(textToTranslate)
    return translatedText1

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_2 = 'textToTranslate'
    textToTranslate = request.args.get(text_2)
    translatedText2 = translator.french_toenglish(textToTranslate)
    return translatedText2

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
