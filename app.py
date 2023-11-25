from flask import Flask, render_template, request, jsonify, abort
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def generate_content():
    try:
        user_input = request.form.get('user_input', '')  # Get user_input from the form

        predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
        payload = {
            "brand_id": "65609012ab1e2fa91d82cce9",
            "text": user_input,
            "media_type": "video",
            "video_duration": "long",
        }
        headers = {"Authorization": "ObzQ8v2MtY13bSB4vOGUa87kovoGYWDc"}

        response = requests.post(predis_ai_url, data=payload, headers=headers)
        responseText = response.text
        return jsonify(responseText )
    
    except Exception as e:
        abort(500)

def result():
    if request.method == 'POST':
        pritn( request.get_json())

        return 'success', 200
    else :
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)

