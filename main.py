from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

TRANSLATION_API_URL = 'https://655.mtis.workers.dev/translate'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_languages', methods=['GET'])
def get_languages():
    languages = [
        {"code": "en", "name": "English"},
        {"code": "fr", "name": "French"},
        {"code": "es", "name": "Spanish"},
        {"code": "de", "name": "German"},
        {"code": "it", "name": "Italian"},
        {"code": "pt", "name": "Portuguese"}
    ]
    return jsonify(languages)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    if data:
        text = data.get('text')
        source_lang = data.get('source_lang')
        target_lang = data.get('target_lang')

        if not text or not source_lang or not target_lang:
            return jsonify({"error": "Invalid input"}), 400

        params = {
            'text': text,
            'source_lang': source_lang,
            'target_lang': target_lang
        }
        url = f"{TRANSLATION_API_URL}?text={params['text']}&source_lang={params['source_lang']}&target_lang={params['target_lang']}"

        response = requests.get(url)
        
        if response.status_code == 200:
            json_response = response.json().get("response")
            print(response.json())
            translated_text = json_response.get("translated_text", "")
            return jsonify({"translatedText": translated_text})

    return jsonify({"error": "Translation failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
