from flask import Flask, render_template, request, jsonify
from speech_translator import SpeechTranslator
import threading

app = Flask(__name__)
translator = SpeechTranslator()
output_messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_translation', methods=['POST'])
def start_translation():
    target_language = request.json['target_language']
    threading.Thread(target=translator.start_translation, args=(target_language, output_messages)).start()
    return jsonify({"status": "started"})

@app.route('/get_messages')
def get_messages():
    return jsonify(output_messages)

@app.route('/stop_translation', methods=['POST'])
def stop_translation():
    translator.stop_translation()
    return jsonify({"status": "stopped"})

if __name__ == '__main__':
    app.run(debug=True)