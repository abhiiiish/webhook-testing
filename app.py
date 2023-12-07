from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/show', methods=['GET','POST'])
def request_post():
    
    url = "https://brain.predis.ai/predis_api/v1/create_content/"
    
    payload = {
      "brand_id": "656890e90866e3d38a426d4f",
      "text": "All our dreams can come true if we have the courage to pursue them",
      "media_type": "single_image",
      "author": "Walt Disney",  # optional
      "template_ids": [],  # pass template_ids if you want quotes in specific design
      "post_type": "quotes"
    }
    
    headers = {"Authorization": "k5esldhz7TkrK9rYqN69RbzifYTd9u2J"}
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    if response.status_code == 200:
        json_response = response.json()
        # post_id = response.get("post_id")
        # post_status = response.get("status")
    
    else:
        print("Error occurred - {}".format(response.text))

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

