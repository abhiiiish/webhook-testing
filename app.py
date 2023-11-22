from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Configured webhook URL
webhook_url = "https://webhook-test-f8cd.onrender.com/index.html"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html', methods=['POST'])
def generate_content():
    user_input = request.form.get('user_input')

    predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
    payload = {
        "brand_id": "64a534aab378eaae3f312b25",
        "text": user_input,
        "media_type": "single_image",
    }
    headers = {"Authorization": "VpHFDiBO9sIB7q4KRrtdiABJAxJgBAcm"}

    response = requests.post(predis_ai_url, data=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        caption = data.get("caption")[0].get("caption")
        generated_media = data.get("generated_media")[0].get("url")

        # Save the POST response to the configured webhook URL
        save_to_webhook(caption, generated_media)

        return jsonify(caption=caption, image=generated_media)
    else:
        return jsonify(error="Failed to generate content"), 500

def save_to_webhook(caption, generated_media):
    # Prepare data to send to the webhook
    webhook_data = {
        "caption": caption,
        "image": generated_media
    }

    # Send POST request to the webhook URL
    webhook_response = requests.post(webhook_url, json=webhook_data)

    # Print the webhook response for debugging (you can handle this differently)
    print("Webhook Response:", webhook_response.text)


@app.route('/get_saved_data')
def get_saved_data():
    # You might want to retrieve the saved data from your database or another source
    saved_data = {
        "caption": "Saved Caption",
        "image": "https://example.com/saved_image.jpg"
    }
    return jsonify(saved_data)


if __name__ == '__main__':
    app.run(debug=True)
