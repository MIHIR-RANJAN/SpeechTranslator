import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
import platform
import time

class SpeechTranslator:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.is_running = False
        self.language_map = {
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

    def get_language_code(self, language_name):
        return self.language_map.get(language_name.lower(), None)

    def speak_text(self, text, lang_code):
        tts = gTTS(text=text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            tts.save(temp_file.name)
            os.system(f"start {temp_file.name}" if platform.system() == "Windows" else f"afplay {temp_file.name}" if platform.system() == "Darwin" else f"mpg123 {temp_file.name}")

    def start_translation(self, target_language, output_messages):
        target_language_code = self.get_language_code(target_language)
        if target_language_code is None:
            output_messages.append("Unsupported language. Exiting program.")
            return

        self.is_running = True
        with sr.Microphone() as source:
            output_messages.append("Please wait. Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            output_messages.append("Microphone calibrated. Start speaking...")
            output_messages.append("click on reset to select different language.")

            while self.is_running:
                output_messages.append("Listening...")
                audio = self.recognizer.record(source, duration=2.5)

                try:
                    text = self.recognizer.recognize_google(audio)
                    output_messages.append(f"Text recognized: {text}")

                    if "stop program" in text.lower():
                        output_messages.append("Stop command recognized. Exiting program.")
                        self.is_running = False
                        break

                    translated_text = self.translator.translate(text, dest=target_language_code).text
                    output_messages.append(f"Translated text: {translated_text}")

                    self.speak_text(translated_text, target_language_code)

                except sr.RequestError as e:
                    output_messages.append(f"Could not request results; {e}")
                except sr.UnknownValueError:
                    output_messages.append("Could not understand the audio")

                time.sleep(0.05)

    def stop_translation(self):
        self.is_running = False