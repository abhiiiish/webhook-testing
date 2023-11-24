from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html', methods=['POST'])
def generate_content():
    try:
        user_input = request.form.get('user_input', '')  # Get user_input from the form

        predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
        payload = {
            "brand_id": "655b548ce8c5caef9d9455b6",
            "text": user_input,
            "media_type": "video",
            "video_duration": "long",
        }
        headers = {"Authorization": "RmntK5qqhRFlg6mcUDmLg4xArPINE6fv"}
        response = requests.post(predis_ai_url, data=payload, headers=headers)
        
        return response.text 
    

    except Exception as e:
        abort(500)

@app.route('/', methods=['POST'])
def result():
    if request.method == 'POST':
        data = request.json()
        print("Received data:", data)  # Print data to the console

        return jsonify({'status': 'success'}), 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)
