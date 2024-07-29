{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0\c87059;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # app.py\
from flask import Flask, request, render_template, jsonify\
import speech_recognition as sr\
from googletrans import Translator\
from gtts import gTTS\
import tempfile\
import os\
import platform\
\
app = Flask(__name__)\
\
# Dictionary to map spoken language names to language codes\
language_map = \{\
    'afrikaans': 'af', 'albanian': 'sq', 'arabic': 'ar', 'armenian': 'hy', 'bengali': 'bn', 'bosnian': 'bs',\
    'catalan': 'ca', 'chechen': 'ce', 'chichewa': 'ny', 'chinese simplified': 'zh-cn', 'chinese traditional': 'zh-tw',\
    'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo',\
    'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',\
    'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he',\
    'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'interlingua': 'ia', 'interlingue': 'ie',\
    'inuktitut': 'iu', 'irish': 'ie', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk',\
    'khmer': 'km', 'kinyarwanda': 'ki', 'korean': 'ko', 'kurdish': 'ku', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',\
    'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malayalam': 'ml', 'maltese': 'mt',\
    'maori': 'mi', 'marathi': 'mr', 'myanmar': 'my', 'mongolian': 'mn', 'nepali': 'my', 'norwegian': 'no', 'odia': 'or',\
    'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro',\
    'russian': 'ru', 'samoan': 'sm', 'sango': 'sg', 'sanskrit': 'sa', 'sardinian': 'sc', 'serbian': 'sr', 'sesotho': 'st',\
    'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',\
    'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tagalog': 'tl', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',\
    'thai': 'th', 'tigrinya': 'ti', 'tonga': 'to', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'vietnamese': 'vi',\
    'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'\
\}\
\
def get_language_code(language_name):\
    """Convert spoken language name to language code."""\
    language_name = language_name.lower()\
    return language_map.get(language_name, None)\
\
def speak_text(text, lang_code):\
    """Convert text to speech and play it directly."""\
    tts = gTTS(text=text, lang=lang_code)\
    with tempfile.NamedTemporaryFile(delete=True, suffix='.mp3') as temp_file:\
        tts.save(temp_file.name)\
        if platform.system() == "Windows":\
            os.system(f"start \{temp_file.name\}")\
        elif platform.system() == "Darwin":\
            os.system(f"afplay \{temp_file.name\}")\
        else:  # Assume Linux\
            os.system(f"mpg123 \{temp_file.name\}")\
\
@app.route('/')\
def index():\
    return render_template('index.html')\
\
@app.route('/process_audio', methods=['POST'])\
def process_audio():\
    # Retrieve audio file from the request\
    audio_file = request.files['audio'].read()\
    target_language_code = request.form['language_code']\
\
    # Initialize recognizer and translator\
    recognizer = sr.Recognizer()\
    translator = Translator()\
\
    # Use the audio file as the source for input\
    audio = sr.AudioData(audio_file, 16000, 2)\
\
    try:\
        # Recognize the speech using Google Web Speech API\
        text = recognizer.recognize_google(audio)\
        print(f"Text recognized: \{text\}")\
\
        # Translate the recognized text\
        translated_text = translator.translate(text, dest=target_language_code).text\
        print(f"Translated text: \{translated_text\}")\
\
        # Convert the translated text to speech and play it\
        speak_text(translated_text, target_language_code)\
\
        # Return success response\
        return jsonify(\{'status': 'success', 'translated_text': translated_text\})\
\
    except sr.RequestError as e:\
        print(f"Could not request results; \{e\}")\
        return jsonify(\{'status': 'error', 'message': str(e)\})\
    except sr.UnknownValueError:\
        print("Could not understand the audio")\
        return jsonify(\{'status': 'error', 'message': 'Could not understand the audio'\})\
\
if __name__ == '__main__':\
    app.run(debug=True)\
}