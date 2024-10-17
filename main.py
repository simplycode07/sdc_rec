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
        {"code": "af", "name": "Afrikaans"},
        {"code": "sq", "name": "Albanian"},
        {"code": "am", "name": "Amharic"},
        {"code": "ar", "name": "Arabic"},
        {"code": "hy", "name": "Armenian"},
        {"code": "az", "name": "Azerbaijani"},
        {"code": "ba", "name": "Bashkir"},
        {"code": "be", "name": "Belarusian"},
        {"code": "bn", "name": "Bengali (Bangla)"},
        {"code": "bs", "name": "Bosnian"},
        {"code": "br", "name": "Breton"},
        {"code": "bg", "name": "Bulgarian"},
        {"code": "my", "name": "Burmese"},
        {"code": "ca", "name": "Catalan"},
        {"code": "zh", "name": "Chinese"},
        {"code": "hr", "name": "Croatian"},
        {"code": "cs", "name": "Czech"},
        {"code": "da", "name": "Danish"},
        {"code": "nl", "name": "Dutch"},
        {"code": "en", "name": "English"},
        {"code": "et", "name": "Estonian"},
        {"code": "fi", "name": "Finnish"},
        {"code": "fr", "name": "French"},
        {"code": "ff", "name": "Fula, Fulah, Pulaar, Pular"},
        {"code": "gl", "name": "Galician"},
        {"code": "gd", "name": "Gaelic (Scottish)"},
        {"code": "ka", "name": "Georgian"},
        {"code": "de", "name": "German"},
        {"code": "el", "name": "Greek"},
        {"code": "gu", "name": "Gujarati"},
        {"code": "ht", "name": "Haitian Creole"},
        {"code": "ha", "name": "Hausa"},
        {"code": "he", "name": "Hebrew"},
        {"code": "hi", "name": "Hindi"},
        {"code": "hu", "name": "Hungarian"},
        {"code": "is", "name": "Icelandic"},
        {"code": "ig", "name": "Igbo"},
        {"code": "id", "name": "Indonesian"},
        {"code": "ga", "name": "Irish"},
        {"code": "it", "name": "Italian"},
        {"code": "ja", "name": "Japanese"},
        {"code": "jv", "name": "Javanese"},
        {"code": "kn", "name": "Kannada"},
        {"code": "kk", "name": "Kazakh"},
        {"code": "km", "name": "Khmer"},
        {"code": "ko", "name": "Korean"},
        {"code": "lo", "name": "Lao"},
        {"code": "lv", "name": "Latvian (Lettish)"},
        {"code": "ln", "name": "Lingala"},
        {"code": "lt", "name": "Lithuanian"},
        {"code": "lg", "name": "Luganda, Ganda"},
        {"code": "lb", "name": "Luxembourgish"},
        {"code": "mk", "name": "Macedonian"},
        {"code": "mg", "name": "Malagasy"},
        {"code": "ms", "name": "Malay"},
        {"code": "ml", "name": "Malayalam"},
        {"code": "mr", "name": "Marathi"},
        {"code": "mn", "name": "Mongolian"},
        {"code": "ne", "name": "Nepali"},
        {"code": "no", "name": "Norwegian"},
        {"code": "oc", "name": "Occitan"},
        {"code": "or", "name": "Oriya"},
        {"code": "ps", "name": "Pashto, Pushto"},
        {"code": "fa", "name": "Persian (Farsi)"},
        {"code": "pl", "name": "Polish"},
        {"code": "pt", "name": "Portuguese"},
        {"code": "pa", "name": "Punjabi (Eastern)"},
        {"code": "ro", "name": "Romanian"},
        {"code": "ru", "name": "Russian"},
        {"code": "sr", "name": "Serbian"},
        {"code": "tn", "name": "Setswana"},
        {"code": "sd", "name": "Sindhi"},
        {"code": "si", "name": "Sinhalese"},
        {"code": "ss", "name": "Siswati"},
        {"code": "sk", "name": "Slovak"},
        {"code": "sl", "name": "Slovenian"},
        {"code": "so", "name": "Somali"},
        {"code": "es", "name": "Spanish"},
        {"code": "su", "name": "Sundanese"},
        {"code": "sw", "name": "Swahili (Kiswahili)"},
        {"code": "ss", "name": "Swati"},
        {"code": "sv", "name": "Swedish"},
        {"code": "tl", "name": "Tagalog"},
        {"code": "ta", "name": "Tamil"},
        {"code": "th", "name": "Thai"},
        {"code": "tr", "name": "Turkish"},
        {"code": "uk", "name": "Ukrainian"},
        {"code": "ur", "name": "Urdu"},
        {"code": "uz", "name": "Uzbek"},
        {"code": "vi", "name": "Vietnamese"},
        {"code": "cy", "name": "Welsh"},
        {"code": "wo", "name": "Wolof"},
        {"code": "fy", "name": "Western Frisian"},
        {"code": "xh", "name": "Xhosa"},
        {"code": "yi", "name": "Yiddish"},
        {"code": "yo", "name": "Yoruba"},
        {"code": "zu", "name": "Zulu"}
    ]
    # languages = [
    #     {"code": "en", "name": "English"},
    #     {"code": "fr", "name": "French"},
    #     {"code": "es", "name": "Spanish"},
    #     {"code": "de", "name": "German"},
    #     {"code": "it", "name": "Italian"},
    #     {"code": "pt", "name": "Portuguese"}
    # ]
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
