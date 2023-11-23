from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def generate_content():
    try:
        user_input = request.form.get('user_input', '')  # Get user_input from the form

        predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
        payload = {
            "brand_id": "64a534aab378eaae3f312b25",
            "text": user_input,
            "media_type": "video",
            "video_duration": "long",
        }
        headers = {"Authorization": "VpHFDiBO9sIB7q4KRrtdiABJAxJgBAcm"}

        response = requests.post(predis_ai_url, data=payload, headers=headers)

        return response.text  # Return the response from the Predis AI API
    except Exception as e:
        print('Error generating content:', e)
        return 'Internal Server Error', 500

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
         caption = data.get('caption')[0]['caption']
         media_url = data.get('generated_media')[0]['url']
        
        # video_url = data.post('videoUrl', '')  
        # Assuming 'videoUrl' is present in the request JSON
        # Process the video URL as needed
        # print('Received video URL:', video_url)
        # Example: Send a response to the webhook URL
        # response = requests.post('https://webhook-test-f8cd.onrender.com/webhook', json={'message': 'Video URL received successfully'})

        return jsonify( text = caption, url = media_url ) 
        
    except Exception as e:
        print('Error processing webhook:', e)
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
