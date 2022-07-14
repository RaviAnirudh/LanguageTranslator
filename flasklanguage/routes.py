from flask import render_template, url_for, request, redirect, abort
import googletrans
from flasklanguage import app
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS


@app.route("/")
def home():
    return render_template('home.html', tittle="Home")


@app.route("/text")
def text():

    return render_template('text.html', tittle="Text")


@app.route("/translate", methods=['POST'])
def translate():
    trans = Translator()

    s = request.form['input_text']
    l = request.form['input_language']
    l = str(l)
    s = str(s)
    dict = googletrans.LANGUAGES
    dict = {value: key for key, value in dict.items()}
    l = l.lower()
    dest_val = ""
    if l == "chinese":
        dest_val = dict["chinese (traditional)"]
    else:
        for i in dict:
            if i == l:
                dest_val = dict[i]
                break
    t = trans.translate(s, dest=dest_val)
    text = t.text
    return render_template('text.html', output_text=text)


@app.route("/translator", methods=['GET','POST'])
def translator():
    r = sr.Recognizer()
    translator = Translator()
    audiovar = request.files['audiovar']

    with sr.AudioFile(audiovar) as source:
        audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, language="en-IN"))
            print('Phrase to be Tranlated: ' + text)
            text_to_translate = translator.translate(text, src='en', dest='hi')
            text1 = text_to_translate.text
            print(text1)
            speak = gTTS(text=text1, lang='hi', slow=False)
            speak.save("captured_voice.mp3")

        except:
            print('Sorry.. run again..')

    return render_template('voice.html', output_voice_text=text1)


@app.route("/voice")
def voice():
    return render_template('voice.html', title='Voice')
