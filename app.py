from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Configured webhook URL for saving responses
save_response_url = "https://webhook-test-f8cd.onrender.com/index.html"

@app.route('/')
def index():
    return render_template('index.html')
    
def generate_content(user_input):
    predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
    payload = {
        "brand_id": "64a534aab378eaae3f312b25",
        "text": user_input,
        "media_type": "single_image",
    }
    headers = {"Authorization": "VpHFDiBO9sIB7q4KRrtdiABJAxJgBAcm"}

    response = requests.post(predis_ai_url, data=payload, headers=headers)

    return response

def save_to_configured_url(data):
    headers = {"Content-Type": "application/json"}
    response = requests.post(save_response_url, json=data, headers=headers)

    return response

def fetch_and_save_response():
    response = requests.get(save_response_url)

    # Assuming the response is JSON, you can save it or process it accordingly
    if response.status_code == 200:
        data = response.json()
        # Save or process the data as needed
        print("Fetched response:", data)
    else:
        print("Failed to fetch response from the configured URL")

    return response

@app.route('/index.html', methods=['POST'])
def display():
    user_input = request.form.get('user_input')
    result = generate_content(user_input)

    if result.status_code == 200:
        data = result.json()
        caption = data.get("caption")[0].get("caption")
        generated_media = data.get("generated_media")[0].get("url")

        # Save the response to the configured URL
        save_to_configured_url({"caption": caption, "image": generated_media})

        # Fetch and save the response from the configured URL
        fetch_and_save_response()

        return jsonify(caption=caption, image=generated_media)

    else:
        return jsonify(error="Failed to generate content"), 500

if __name__ == '__main__':
    app.run(debug=True)
