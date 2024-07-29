# speech_translator.py
import speech_recognition as sr
import time
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
import platform

# Dictionary to map spoken language names to language codes
language_map = {
    'afrikaans': 'af', 'albanian': 'sq', 'arabic': 'ar', 'armenian': 'hy', 'bengali': 'bn', 'bosnian': 'bs',
    'catalan': 'ca', 'chechen': 'ce', 'chichewa': 'ny', 'chinese simplified': 'zh-cn', 'chinese traditional': 'zh-tw',
    'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo',
    'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
    'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he',
    'hindi': 'hi', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'interlingua': 'ia', 'interlingue': 'ie',
    'inuktitut': 'iu', 'irish': 'ie', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk',
    'khmer': 'km', 'kinyarwanda': 'ki', 'korean': 'ko', 'kurdish': 'ku', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
    'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malayalam': 'ml', 'maltese': 'mt',
    'maori': 'mi', 'marathi': 'mr', 'myanmar': 'my', 'mongolian': 'mn', 'nepali': 'my', 'norwegian': 'no', 'odia': 'or',
    'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro',
    'russian': 'ru', 'samoan': 'sm', 'sango': 'sg', 'sanskrit': 'sa', 'sardinian': 'sc', 'serbian': 'sr', 'sesotho': 'st',
    'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
    'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tagalog': 'tl', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',
    'thai': 'th', 'tigrinya': 'ti', 'tonga': 'to', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'vietnamese': 'vi',
    'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
}

def get_language_code(language_name):
    """Convert spoken language name to language code."""
    language_name = language_name.lower()
    return language_map.get(language_name, None)

def speak_text(text, lang_code):
    """Convert text to speech and play it directly."""
    tts = gTTS(text=text, lang=lang_code)
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        tts.save(temp_file.name)
        os.system(f"start {temp_file.name}" if platform.system() == "Windows" else f"afplay {temp_file.name}" if platform.system() == "Darwin" else f"mpg123 {temp_file.name}")

def real_time_speech_recognition(target_language_code):
    """Perform real-time speech recognition and translate text to speech in target language."""
    recognizer = sr.Recognizer()
    translator = Translator()

    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Microphone calibrated. Start speaking...")

        while True:
            print("Listening...")
            audio = recognizer.record(source, duration=3.5)

            try:
                text = recognizer.recognize_google(audio)
                print(f"Text recognized: {text}")

                # Translate the recognized text
                translated_text = translator.translate(text, dest=target_language_code).text
                print(f"Translated text: {translated_text}")

                # Convert the translated text to speech and speak it
                speak_text(translated_text, target_language_code)

                if "stop program" in text.lower():
                    print("Stop command recognized. Exiting program.")
                    break
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.UnknownValueError:
                print("Could not understand the audio")

            time.sleep(0.10)

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please tell the language in which you want to translate:")
        audio = recognizer.listen(source)
    
    try:
        spoken_language = recognizer.recognize_google(audio)
        print(f"Language spoken: {spoken_language}")
        target_language_code = get_language_code(spoken_language)

        if target_language_code is None:
            print("Unsupported language. Exiting program.")
        else:
            real_time_speech_recognition(target_language_code)
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Could not understand the audio")

