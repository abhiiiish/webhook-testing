from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])   
def generate_content(user_input):
    predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
    payload = {
        "brand_id": "64a534aab378eaae3f312b25",
        "text": user_input,
        "media_type": "video",
        "video_duration": "long",
    }
    headers = {"Authorization": "VpHFDiBO9sIB7q4KRrtdiABJAxJgBAcm"}

    response = requests.post(predis_ai_url, data=payload, headers=headers)

    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        video_url = data.get('videoUrl', '')  
        # Assuming 'videoUrl' is present in the request JSON

        # Process the video URL as needed
        print('Received video URL:', video_url)

        # Example: Send a response to the webhook URL
        response = requests.post('https://webhook-test-f8cd.onrender.com/webhook', json={'message': 'Video URL received successfully'})

        return 'OK', 200
    except Exception as e:
        print('Error processing webhook:', e)
        return 'Internal Server Error', 500


if __name__ == '__main__':
    app.run(debug=True)


