from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import json

app = Flask(__name__)
app.debug = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# Set up application context
with app.app_context():
    # Create tables in the database
    db.create_all()

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



# Initialize the migration
migrate = Migrate(app, db)


# Add a route to display the profiles
@app.route('/')
def index():
    # Display profiles from the database
    profiles = Profile.query.all()
    return render_template('index.html', profiles=profiles)


@app.route('/send', methods=['POST'])
def generate_content():
    
    user_input = request.form.get('user_input')

    url = "https://brain.predis.ai/predis_api/v1/create_content/"

    payload = {
      "brand_id": "64e86b35de4590305093c2b3",
      "text": "3 tips for a healthy morning breakfast",
      "media_type": "single_image",
      "color_palette_type": "ai_suggested"
  
    }
    headers = {"Authorization": "ayUWiVk7cLb8UR6aWNrDzeh5k41tU3cF"}
    response = requests.request("POST", url, data=payload, headers=headers)
    return jsonify(response.json)




# Add a route to receive the webhook data
@app.route('/index.html', methods=['POST'])
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
    app.run()

app.app_context().push()


