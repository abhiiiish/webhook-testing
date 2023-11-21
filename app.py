from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/generate_content', methods=['POST'])
def generate_content():
    user_input = request.form.get('user_input')

    predis_ai_url = "https://brain.predis.ai/predis_api/v1/create_content/"
    payload = {
        "brand_id": "64a534aab378eaae3f312b25",
        "text": user_input,
        "media_type": "single_image",
        "template_ids": ["1"],
  }
    headers = {"Authorization": "VpHFDiBO9sIB7q4KRrtdiABJAxJgBAcm"}

    response = requests.post(predis_ai_url, data=payload, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        post_id = json_response.get("post_id")
        post_status = json_response.get("status")

        # Save the generated content (You may want to save it to a database)
        save_generated_content(json_response)

        return json_response
    else:
        error_message = "Error occurred - {}".format(response.text)
        return render_template('error.html', error_message=error_message)


@app.route('/result.html', methods=['GET','POST'])
def get_webhook_data():

    get_Data = generate_content()
    url = get_Data.get('url')

    return render_template('result.html', image = url)




if __name__ == '__main__':
    app.run(debug=True)

