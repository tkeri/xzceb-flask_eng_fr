'''
Server side
'''

from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    '''
    English to french.
    '''
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    '''
    French to english.
    '''
    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    '''
    Render index.html.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
