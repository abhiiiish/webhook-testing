from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html',methods=['POST'])
def generate_content():
    user_input = request.form.get('user_input')

    predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
    payload = {
        "brand_id": "64a534aab378eaae3f312b25",
        "text": user_input,
        "media_type": "single_image",
        #"template_ids": ["1"],
  }
    headers = {"Authorization": "VpHFDiBO9sIB7q4KRrtdiABJAxJgBAcm"}

    response = requests.post(predis_ai_url, data=payload, headers=headers)
    json_response = response.json()
    
    return json_response



if __name__ == '__main__':
    app.run(debug=True)

