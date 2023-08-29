from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        username = data['username']  # Extract username

        user = auth.create_user(email=email, password=password)
        # Additional actions after successful signup

        # Update the user's display name
        auth.update_user(
            user.uid,
            display_name=username
        )

        return jsonify({"message": "User created successfully"}), 201
    except KeyError as e:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": "Signup failed"}), 500


# Route for user login
@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    try:
        user = auth.get_user_by_email(email)
        # Additional actions after successful login
        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

# Route for user registration with Facebook
@app.route('/signup/facebook', methods=['POST'])
def signup_facebook():
    try:
        data = request.get_json()
        facebook_token = data['facebook_token']  # Token received from frontend
        # Authenticate with Facebook token and create the user
        # Additional actions after successful Facebook registration
        return jsonify({"message": "Facebook registration successful"}), 201
    except KeyError as e:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": "Facebook registration failed"}), 500

# Route for user registration with Google
@app.route('/signup/google', methods=['POST'])
def signup_google():
    try:
        data = request.get_json()
        google_token = data['google_token']  # Token received from frontend
        # Authenticate with Google token and create the user
        # Additional actions after successful Google registration
        return jsonify({"message": "Google registration successful"}), 201
    except KeyError as e:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": "Google registration failed"}), 500

if __name__ == '__main__':
    app.run()
