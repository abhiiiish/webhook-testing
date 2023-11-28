from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.String(50), nullable=False)
    post_id = db.Column(db.String(50), nullable=False)
    caption = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    media_url = db.Column(db.String(200), nullable=True)
    media_type = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"Profile(id={self.id}, brand_id={self.brand_id}, post_id={self.post_id}, caption={self.caption[:50]}, status={self.status}, media_url={self.media_url}, media_type={self.media_type})"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/db', methods=['POST'])
def get_db_data():
    profiles = Profile.query.all()
    return jsonify({'profiles': profiles})

@app.route('/index', methods=['POST'])
def generate_content():
    user_input = request.form.get('user_input')

    url = "https://brain.predis.ai/predis_api/v1/create_content/"
    payload = {
        "brand_id": "64e86b35de4590305093c2b3",
        "text": user_input,  # Use user input here
        "media_type": "single_image",
        "color_palette_type": "ai_suggested"
    }
    headers = {"Authorization": "ayUWiVk7cLb8UR6aWNrDzeh5k41tU3cF"}
    response = requests.post(url, data=payload, headers=headers)

    return jsonify({'text': response.json})

@app.route('/index/webhook', methods=['POST'])
def webhook_data():
    data = request.json

    # Save data to the database
    new_profile = Profile(
        brand_id=data['brand_id'],
        post_id=data['post_id'],
        caption=data['caption'][0]['caption'],
        status=data['status'],
        media_url=data['generated_media'][0]['url'] if 'generated_media' in data else None,
        media_type=data['media_type'] if 'media_type' in data else None
    )
    db.session.add(new_profile)
    db.session.commit()

    return jsonify({"message": "Webhook data received and saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)
